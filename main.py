class TTT(object):
    """
    Tic-Tac-Tao class
    """
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.MAP = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def isWin(self):
        """
        Take a map(list of lists)
        return True if any list contain same element in row, col or X pattern
        """
        def isEql(lst):
            """
            helper function which check every elemnt in the list is equal
            return the Winner (X or O) if all element in the list is the same
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
        # return(False) if not result else return(result[0][0])
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
    # get players names
    player1 = input('X player name: ')
    player2 = input("O player name: ")

    # init our game
    game = TTT(player1, player2)
    roundNum = 0    # To keep track the Round
    playerTurn = 0  # which player should play now
    # while not game.isWin() and roundNum < 9:
    while game.isWin() is False and roundNum < 9:
        playRound(game, playerTurn)
        playerTurn = (playerTurn + 1) % 2
        pass
    else:
        game.draw()
        print("%s Player win" % game.isWin())
    return 0


playGame()

# TODO: Formalize the code and make main function
# TODO: write TTT input function that show help or quite if user want
# TODO: make player score system and apply it
