#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
      __Author__: Ahmed khaled
      __email__ = "ahmed_khaled@zoho.com"
      __Last Update__: Wed Aug 15 17:32:20 EET 2018
      __license__ = "GPLv3" please read LICENSE file
      __maintainer__ = Abdallah Hesham

a Tic-tac-tao game written in python.
"""
# return 0 mean succesful
# reutrn 1 mean faild
# I will use these to handle errors


class TTT(object):
    """
    Tic-Tac-Tao class
    """
    # def __init__(self, player1, player2):
    def __init__(self):
        # self.player1 = player1
        # self.player2 = player2
        self.MAP = [                # MAP is the game board
            [1, 2, 3],              # it is di-diamention list
            [4, 5, 6],              # aka list of lists
            [7, 8, 9]
        ]

    def isWin(self):
        """
        Take a Map(list of lists)
        return winner if any row, col or X pattern contain same element
               otrherwise return False
        """
        def isEql(lst):
            """
            helper function which check every elemnt in the list is equal
            return the True if all element in the list is the same
                   otherwise return False
            """
            for ele in lst[1:]:
                if ele != lst[0]:
                    return False
            else:
                return True

        # X shape pattern list
        x1MAP = [self.MAP[0][0], self.MAP[1][1], self.MAP[2][2]]
        x2MAP = [self.MAP[0][2], self.MAP[1][1], self.MAP[2][0]]

        # result contain list of all samilar elemnt lists
        # aka if player win it will contain list of its compelete row
        #     otherwise it will be an empyt list
        result = list(filter(isEql, self.MAP)) or \
                 list(filter(isEql,
                             map(lambda x, y, z: [x, y, z],
                                 self.MAP[0],
                                 self.MAP[1],
                                 self.MAP[2]))) or \
                 list(filter(isEql, [x1MAP, x2MAP]))
        return False if not result else result[0][0]

    def change(self, sym, place):
        """
        Take a symbol(X or O)
           & a place (number from 1-9 represent which place
                      player want to play)
        return a new Map with place replaced with symbol
        """
        # first let's know which list of maps should we change
        # (aka, first row, snd or third)
        if place <= 3:
            lstNum = 0
        elif place <= 6:
            lstNum = 1
        else:
            lstNum = 2

        self.MAP[lstNum][(place % 3) - 1] = sym
        return 0

    def draw(self):
        """
        take a map (list of lists)
        and print it on the screen as gridl
        I will draw it as open Box, may change later
        """
        # TODO: print new line
        for lst in self.MAP:
            print(' | '.join(map(str, lst)))
            pass

        return 0
    pass


def playRound(game, player):
    """
    PlayRound funciton is impelemntation of 1 round play,
              it take a TTT object and a number(0 mean X otherise mean O)
              mutate TTT object's map
    """
    game.draw()
    if player == 0:
        game.change('X',
                    int(input("X player round: ")))
    elif player == 1:
        game.change('O',
                    int(input("O player round: ")))
    else:
        print("invalid Player number")
        return 1
    return 0


def playGame():
    """
    PlayGame is impelementation of a game, just one game
             it basicly do the follow.
             * init a TTT object.
             * trak 1. round number to know that map has valid space
                    2. game status aka: if player win or something else.
             * use playRound function to get users input change map
    """
    # get players names
    # player1 = input('X player name: ')
    # player2 = input("O player name: ")

    # init our game
    game = TTT()
    roundNum = 0    # To keep track the Round
    playerTurn = 0  # which player should play now
    while game.isWin() is False and roundNum < 9:
        playRound(game, playerTurn)
        playerTurn = (playerTurn + 1) % 2
        pass
    else:
        game.draw()            # Draw final result
        winner = game.iswin()
        if winner:             # chech if winner contain winner symbol or not
            print("%s Player win" % winner)
        else:
            return 1  # one here mean no one win
        return 0


    playGame()

# TODO: Formalize the code and make main function
# TODO: write TTT input function that show help or quite if user want
# TODO: make player score system and apply it
