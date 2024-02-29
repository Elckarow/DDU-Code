transform connect_four_piece(y):
    subpixel True alpha 0.0 yoffset y
    ease_cubic 0.5 alpha 1.0
    easein_bounce 0.8 yoffset 0.0

transform connect_four_winning_piece:
    animation
    matrixcolor BrightnessMatrix(0.0)

    pause 0.5
    block:
        pause 0.8
        easein_quad 0.45 matrixcolor BrightnessMatrix(0.8)
        easeout_quad 0.45 matrixcolor BrightnessMatrix(0.0)
        repeat

init python in connect_four:
    from renpy import store
    from store import Color, Null, At, connect_four_piece, Solid, CircleDisplayable, connect_four_winning_piece, ui
    import threading

    COLS = 7
    ROWS = 6

    PIECE_SIZE = 50
    GRID_SPACING = 17

    INFINITY = float("inf")
    MAX_DEPTH = 7

    def show(
        xanchor=0.5, xpos=0.5,
        yanchor=1.0, ypos=0.75,
        zoom=1.0,
        color1="#fbff2a", color2="#ff2626",
        player_moves_first=True,
    ):
        player_moves_first = bool(player_moves_first)
        global _player; _player = player_moves_first
        global board; board = Board(color1, color2, player_moves_first)
        
        renpy.show_screen("connect_four",
            xanchor=xanchor,
            xpos=xpos,
            yanchor=yanchor,
            ypos=ypos,
            zoom=zoom
        )
        # renpy.show_screen("_connect_four_compute_ai_move")
    
    def hide():
        global board; board = None
        renpy.hide_screen("connect_four")
        # renpy.hide_screen("_connect_four_compute_ai_move")
    
    def place(col):
        global board, _player
        board.add_piece(col - 1)
        _player = not _player
    
    def interact():
        store._window_hide()

        global _interact; _interact = True
        col = ui.interact()
        _interact = False

        store._window_auto = True
        place(col + 1)
    
    def ai_place():
        global board, _player
        board.ai_add_piece()
        _player = not _player
    
    # _ai_move_lock = threading.Lock()

    # code can be optimized but fuck off :)
    class Board(renpy.display.layout.Grid):
        def __init__(self, color1, color2, first):
            global COLS, ROWS
            super(Board, self).__init__(COLS, ROWS, style="connect_four_grid")
            self.first = first

            global PIECE_SIZE
            self.piece_size = PIECE_SIZE
            self.null = Null(PIECE_SIZE, PIECE_SIZE)

            l = self.cols * self.rows
            for _ in range(l):
                self.add(self.null)
            
            self.pieces = [None] * l

            self.winning_pieces = set()

            self.player_color = Color(color1)
            self.opponent_color = Color(color2)

            self.state = State(0, 0)
            # self.next_ai_state = State(0, 0)
        
        def get_status(self):
            return self.state.get_status()

        def add_piece(self, col):
            self._add_piece(col)

            new_game_position = self.state.make_move(self.state.game_position, col)
            self.state = State(self.state.opponent_position, new_game_position, self.state.depth + 1)
        
        def ai_add_piece(self):
            position = self.state.opponent_position if not _player else self.state.player_position

            # with _ai_move_lock:
                # new_state = self.next_ai_state 
            
            new_state = self.state.alphabeta_search(self.first)

            col = position ^ (new_state.opponent_position if not _player else new_state.player_position)
            col = (col.bit_length() - 1) // self.cols

            self._add_piece(col)
            self.state = new_state

        def _add_piece(self, col):
            cols = self.cols
            rows = self.rows

            if not 0 <= col <= cols - 1:
                raise Exception("not a valid column: {}".format(col + 1))

            color = self.player_color if _player else self.opponent_color

            for i, child in enumerate(reversed(self.children[col::cols])): # iterating over the `col`th column, from bottom to top
                if child is self.null:
                    row = rows - i - 1
                    piece_index = col + row * cols

                    y = -((row + 1) * (self.piece_size + self.style.spacing))
                    self.children[piece_index] = At(PieceDisplayable(color, self.piece_size), connect_four_piece(y))
                    
                    self.pieces[piece_index] = Piece(_player)
                    self.update_piece_neighbours(col, row)

                    for similars in self.get_piece_similar_neighbours(col, row):
                        if len(similars) < 4: continue
                        
                        for s_piece in similars:
                            s_index = self.pieces.index(s_piece)
                                
                            if s_index in self.winning_pieces: continue
                            self.winning_pieces.add(s_index)

                            self.children[s_index] = At(self.children[s_index], connect_four_winning_piece)
                    
                    self.update()
                    break

            else:
                raise Exception("column {} is full".format(col + 1))
        
        def update_piece_neighbours(self, col, row):
            index = col + row * self.cols
            pieces = self.pieces
            piece = pieces[index]

            leftmost_col  = col == 0
            rightmost_col = col == self.cols - 1
            top_row       = row == 0
            bottom_row    = row == self.rows - 1

            def set_neighbour(neighbour, coords_to_neighbour):
                if neighbour is None: return
                piece.set_neighbour(neighbour, coords_to_neighbour)
                neighbour.set_neighbour(piece, piece.OPPOSITE[coords_to_neighbour])

            if not leftmost_col:
                if not top_row:
                    set_neighbour(pieces[index - self.cols - 1], piece.TOP_LEFT)
                set_neighbour(pieces[index - 1], piece.MIDDLE_LEFT)
                if not bottom_row:
                    set_neighbour(pieces[index + self.cols - 1], piece.BOTTOM_LEFT)
            
            if not rightmost_col:
                if not top_row:
                    set_neighbour(pieces[index - self.cols + 1], piece.TOP_RIGHT)
                set_neighbour(pieces[index + 1], piece.MIDDLE_RIGHT)
                if not bottom_row:
                    set_neighbour(pieces[index + self.cols + 1], piece.BOTTOM_RIGHT)
            
            if not bottom_row:
                set_neighbour(pieces[index + self.cols], piece.BOTTOM_CENTER)

        def get_piece_similar_neighbours(self, col, row):
            piece = self.pieces[col + row * self.cols]

            # no need to check for above
            vertical_bottom = set(piece.get_similar_neighbours(piece.BOTTOM_CENTER))
            vertical = vertical_bottom | {piece}
            
            horizontal_left = set(piece.get_similar_neighbours(piece.MIDDLE_LEFT))
            horizontal_right = set(piece.get_similar_neighbours(piece.MIDDLE_RIGHT))
            horizontal = horizontal_left | {piece} | horizontal_right

            diag_top_left = set(piece.get_similar_neighbours(piece.TOP_LEFT))
            diag_bottom_right = set(piece.get_similar_neighbours(piece.BOTTOM_RIGHT))
            diag_top_left_bottom_right = diag_top_left | {piece} | diag_bottom_right

            diag_top_right = set(piece.get_similar_neighbours(piece.TOP_RIGHT))
            diag_bottom_left = set(piece.get_similar_neighbours(piece.BOTTOM_LEFT))
            diag_top_right_bottom_left = diag_top_right | {piece} | diag_bottom_left

            return [vertical, horizontal, diag_top_left_bottom_right, diag_top_right_bottom_left]

    def PieceDisplayable(color, size):
        return CircleDisplayable(color=color, radius=size / 2)

    class Piece(object):
        TOP_LEFT   = (0, 0)
        TOP_CENTER = (1, 0)
        TOP_RIGHT  = (2, 0)

        MIDDLE_LEFT  = (0, 1)
        MIDDLE_RIGHT = (1, 1)

        BOTTOM_LEFT   = (0, 2)
        BOTTOM_CENTER = (1, 2)
        BOTTOM_RIGHT  = (2, 2)

        OPPOSITE = {
            TOP_LEFT  : BOTTOM_RIGHT,
            TOP_CENTER: BOTTOM_CENTER,
            TOP_RIGHT : BOTTOM_LEFT,

            MIDDLE_LEFT : MIDDLE_RIGHT,
            MIDDLE_RIGHT: MIDDLE_LEFT,

            BOTTOM_LEFT  : TOP_RIGHT,
            BOTTOM_CENTER: TOP_CENTER,
            BOTTOM_RIGHT : TOP_LEFT,
        }
        
        def __init__(self, player):
            self.player = bool(player)

            self.neighbours = [
                [None, None, None],
                [None,       None],
                [None, None, None]
            ]
        
        def set_neighbour(self, piece, coords):
            current_neighbour = self.get_neighbour(coords)
            if current_neighbour is piece: return

            if current_neighbour is not None:
                raise Exception("already has a neighbour piece (coords: {})".format(coords))

            x, y = coords
            self.neighbours[y][x] = piece
        
        def get_neighbour(self, coords):
            x, y = coords
            return self.neighbours[y][x]
        
        def get_similar_neighbours(self, coords):
            neighbour = self.get_neighbour(coords)
            
            if neighbour is not None and neighbour.player is self.player:
                yield neighbour
                for n in neighbour.get_similar_neighbours(coords):
                    yield n
    
    class State(object):
        LOSS = 0
        WIN  = 1
        DRAW = 2

        def __init__(self, opponent_position, game_position, depth=0):
            self.opponent_position = opponent_position
            self.game_position = game_position
            self.depth = depth

        @property
        def player_position(self):
            return self.opponent_position ^ self.game_position

        def generate_children(self, who_went_first):
            """
            For each column, generate a new `State` if the new position is valid.
            """
            for i in range(COLS):
                # select column starting from the middle and then to the edges (m, m-1, m+1, m-2, m+2, etc...)
                column = COLS // 2 + ((1 - 2 * (i % 2)) * (i + 1)) // 2
                if not self.is_column_full(self.game_position, column):
                    new_game_position = self.make_move(self.game_position, column)

                    if self.depth % 2 == who_went_first:
                        new_opponent_position = self.player_position ^ new_game_position
                    else:
                        new_opponent_position = self.opponent_position

                    yield State(new_opponent_position, new_game_position, self.depth + 1)

        def calculate_heuristic(self):
            status = self.get_status()
            d, m = divmod(self.depth, 2)

            if status is None:
                return INFINITY if m == 0 else -INFINITY
            
            if status == self.LOSS:
                # AI Wins
                return 22 - d
            elif status == self.WIN:
                # Player Wins
                return -1 * (22 - d)
            # Draw
            return 0

        def alphabeta_search(self, turn):
            cutoff_search = (lambda state, depth: depth > MAX_DEPTH or state.get_status() is not None)  

            def max_value(state, alpha, beta, depth):
                if cutoff_search(state, depth):
                    return state.calculate_heuristic()  

                v = -INFINITY

                for child in state.generate_children(turn):
                    if child in seen: continue  

                    v = max(v, min_value(child, alpha, beta, depth + 1))
                    seen[child] = alpha

                    if v >= beta: return v  

                    alpha = max(alpha, v)   

                if v == -INFINITY: return INFINITY  

                return v    

            def min_value(state, alpha, beta, depth):
                if cutoff_search(state, depth): return state.calculate_heuristic()  

                v = INFINITY    

                for child in state.generate_children(turn):
                    if child in seen: continue  

                    v = min(v, max_value(child, alpha, beta, depth + 1))
                    seen[child] = alpha

                    if v <= alpha: return v 

                    beta = min(beta, v) 

                if v == INFINITY: return -INFINITY
                return v      

            seen = { }

            best_score = -INFINITY
            beta = INFINITY
            best_action = None  

            for child in self.generate_children(turn):
                v = min_value(child, best_score, beta, 1)
                if v > best_score:
                    best_score = v
                    best_action = child 

            return best_action
        
        @staticmethod
        def is_winning_state(position):
                    # --    \         /         |
            for i in (COLS, COLS - 1, COLS + 1, 1):
                m = position & (position >> i)
                if m & (m >> i * 2): return True

            return False

        @staticmethod
        def is_column_full(position, column):
            return position & (1 << (COLS * column + ROWS - 1))
        
        def is_draw(self, position):
            return all(self.is_column_full(position, column) for column in range(COLS))

        def get_status(self):
            if self.is_winning_state(self.opponent_position):
                return self.LOSS
            
            if self.is_winning_state(self.player_position):
                return self.WIN
            
            if self.is_draw(self.game_position):
                return self.DRAW
            
            return None

        @staticmethod
        def make_move(game_position, col):
            return game_position | (game_position + (1 << (col * COLS)))

        def __hash__(self):
            return hash((self.opponent_position, self.game_position, self.depth % 2))

        def __eq__(self, other):
            return (
                (self.opponent_position, self.game_position, self.depth % 2)
                ==
                (other.opponent_position, other.game_position, other.depth % 2)
            )

default connect_four._player = True
default connect_four.board = None
default connect_four._interact = False

screen connect_four(
    xanchor, xpos,
    yanchor, ypos,
    zoom
):
    style_prefix "connect_four"

    fixed at Flatten:
        at transform:
            on show:
                alpha 0.0 yoffset 100
                easein 0.4 alpha 1.0 yoffset 0.0
            on hide:
                easeout 0.4 alpha 0.0 yoffset 100

        vbox:
            at transform:
                subpixel True zoom zoom anchor (xanchor, yanchor) pos (xpos, ypos)

            hbox xalign 0.5:
                for i in range(connect_four.COLS):
                    showif connect_four._interact:
                        button:
                            at transform:
                                subpixel True alpha 0.0
                                parallel:
                                    on show:
                                        linear 0.3 alpha 1.0
                                    on hide:
                                        linear 0.3 alpha 0.0
                                parallel:
                                    on idle:
                                        matrixcolor BrightnessMatrix(0.0)
                                    on hover:
                                        matrixcolor BrightnessMatrix(0.2)

                            action Return(i)
                            add "#f00"

            frame:
                add connect_four.board

style connect_four_fixed is empty

style connect_four_frame is empty:
    background Solid("#0004ff")
    padding (10, 10)

style connect_four_grid:
    spacing connect_four.GRID_SPACING

style connect_four_hbox is empty:
    spacing connect_four.GRID_SPACING

style connect_four_button is empty:
    xysize (connect_four.PIECE_SIZE, connect_four.PIECE_SIZE)