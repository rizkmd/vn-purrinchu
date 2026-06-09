init python:
    import random
    import math

    class CardMatchGame(object):
        def __init__(self, pairs=6):
            self.pairs = pairs
            self.cards = list(range(pairs)) * 2
            random.shuffle(self.cards)
            self.revealed = [False] * (pairs * 2)
            self.first_pick = None
            self.second_pick = None
            self.matched = [False] * (pairs * 2)
            self.lock = False
            self.attempts = 0

        def pick(self, idx):
            if self.lock or self.revealed[idx] or self.matched[idx]:
                return
            if self.first_pick is None:
                self.first_pick = idx
                self.revealed[idx] = True
            elif self.second_pick is None and idx != self.first_pick:
                self.second_pick = idx
                self.revealed[idx] = True
                self.attempts += 1
                self.lock = True

        def check_match(self):
            if self.first_pick is None or self.second_pick is None:
                return
            if self.cards[self.first_pick] == self.cards[self.second_pick]:
                self.matched[self.first_pick] = True
                self.matched[self.second_pick] = True
            else:
                self.revealed[self.first_pick] = False
                self.revealed[self.second_pick] = False
            self.first_pick = None
            self.second_pick = None
            self.lock = False

        def is_complete(self):
            return all(self.matched)

        @property
        def cols(self):
            return 4

        @property
        def rows(self):
            return int(math.ceil((self.pairs * 2) / self.cols))


screen card_match_game(game):
    modal True

    if game.is_complete():
        timer 1.0 action Return(True)

    if game.lock:
        timer 0.7 action Function(game.check_match)

    add "#000000cc"

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)

        vbox:
            spacing 16
            xalign 0.5

            text "Cocokkan Kartu!" xalign 0.5 size 30
            text "Percobaan: [game.attempts]" xalign 0.5 size 20

            null height 10

            grid game.cols game.rows:
                spacing 8
                xalign 0.5
                for idx in range(game.pairs * 2):
                    if game.matched[idx]:
                        frame:
                            xsize 120
                            ysize 120
                            background "#228B2255"
                            text str(game.cards[idx] + 1) xalign 0.5 yalign 0.5 size 36 color "#ffffff"
                    elif game.revealed[idx]:
                        button:
                            xsize 120
                            ysize 120
                            background "#4488cc"
                            action NullAction()
                            text str(game.cards[idx] + 1) xalign 0.5 yalign 0.5 size 36 color "#ffffff"
                    else:
                        button:
                            xsize 120
                            ysize 120
                            background "#663399"
                            action Function(game.pick, idx)
                            text "?" xalign 0.5 yalign 0.5 size 36 color "#ffffff"

                for _pad in range((game.cols * game.rows) - (game.pairs * 2)):
                    null width 120 height 120

            null height 10

            textbutton "Menyerah" xalign 0.5 action Return(False)
