init python:
    class TeamCredit(object):
        def __init__(self, name, text):
            self.name = name
            self.text = text
    
    team_credits_idk = (
        TeamCredit(
            "Tiffany",
            _("""\
has been the project's lead for the longest time, helping direct everything and making sure everyone contributed. He's also one of the main writers, having written a good portion of the script.""")
        ),

        TeamCredit(
            "Kasumi Sato,",
            _("""\
or Sumi for short, is the team's musician, as well as a prominent writer. He's helped set the theme for this project, as well as maintain quality assurance.""")
        ),

        TeamCredit(
            "Arcannite,",
            _("""\
lovingly referred to as Arcy, is the team's concept artist. While he may be a little snarky, he's helped with not just art, but also writing and coding.""")
        ),

        TeamCredit(
            "Staticquit,",
            _("""\
or Static for short, is the team's main artist, contributing both CGs and sprites to the project, as well as lightening the mood for everyone around her.""")
        ),

        TeamCredit(
            "Pivot Whiteground Lever,",
            _("""\
or Pivot for short, is the team's proofreader and project organiser. She helps keep things up to date and readily accessible, but she's also contributed with writing and editing, among other trades.""")
        ),

        TeamCredit(
            "Elckarow",
            _("""\
is the team's coder, the one who brought the project to life in mod form. Without his help, there wouldn't be a mod to play!""")
        ),

    TeamCredit(
            _("Full Credits"),
            _("""\
A more detailed list of those who contributed to this project can be found on our website.

Click {a=https://undercurrentsmod.weebly.com/credits.html}HERE{/a} to open it in your browser.""")
        )
    )

screen credits():
    tag menu
    
    default mt = (len(team_credits_idk) - 1) // 2
    default t = 0

    python:
        # lasagna code
        team_credit = tuple(iterPage(team_credits_idk, t, 2))
        l = len(team_credit)
        if l != 2:
            team_credit += (TeamCredit("", ""),) * (2 - l)
        
        credit_1, credit_2 = team_credit
        # do not steal

    use game_menu(CreditsMenuInfo, menu_style="book"):
        style_prefix "credit"
        
        hbox:
            frame style "credit_page_1":
                vbox:
                    text "[credit_1.name]" style "credit_name"

                    viewport:
                        draggable True
                        mousewheel True

                        text "[credit_1.text!t]"

            frame style "credit_page_2":
                vbox:
                    text "[credit_2.name]" style "credit_name"

                    viewport:
                        draggable True
                        mousewheel True
                        
                        text "[credit_2.text!t]"

        use book_turn_page(
            If(
                t != 0,
                true=(SetLocalVariable("t", t - 1), With(game_menu_transition))
            ),
            If(
                t != mt,
                true=(SetLocalVariable("t", t + 1), With(game_menu_transition))
            )
        )

style credit_hbox is game_menu_book_hbox_page

style credit_page_1 is game_menu_book_page_1
style credit_page_2 is game_menu_book_page_2

style credit_name is book_title
style credit_text is book_text:
    hyperlink_functions hyperlink_functions_style("credit_hyperlink_text")

style credit_hyperlink_text is book_text:
    underline True
    hover_color "#fff"

style credit_vbox is book_title_vbox