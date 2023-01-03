#Yusuf Emir Cömert - 2220765023
import sys
playfields = {}
playfields[1] = {}
playfields[2] = {}
letters = ["C", "B", "D", "S", "P"]         #first letters of the ships names
plural = ["-", ""]

ships = {}
ships[1] = {}
ships[2] = {}
winner = 0
output_file = open("Battleship.out", "w")


def write(text, ending):     #This function is hard to explain so I explained it in the report
    toprint = "".join(text)
    if ending:
        print(toprint, end="")
        print(toprint, end="", file=output_file)
    else:
        print(toprint)
        print(toprint, file=output_file)


def read():
    global player1
    global player2
    player1 = open(sys.argv[1], 'r')
    player2 = open(sys.argv[2], 'r')
    while True:
        line1 = player1.readlines()
        line2 = player2.readlines()
        for a in range(len(line1)):
            readline(line1[a], a + 1, 1)
            readline(line2[a], a + 1, 2)
        if not line2:
            break


def optional():             #this is an important function which groups the ships from the optionalplayer inputs files
    optional1 = open("OptionalPlayer1.txt", 'r')
    optional2 = open("OptionalPlayer2.txt", 'r')
    while True:
        line1 = optional1.readlines()
        line2 = optional2.readlines()
        for a in range(len(line1)):
            ship1 = line1[a].split(":")[0]
            playfields[1][ship1] = {}
            formation1 = line1[a].strip("\n").split(":")[1]
            firsttile1 = formation1.split(";")[0].split(",")[1] + formation1.split(";")[0].split(",")[0]
            direction1 = formation1.split(";")[1]

            ship2 = line2[a].split(":")[0]
            playfields[2][ship2] = {}
            formation2 = line2[a].strip("\n").split(":")[1]
            firsttile2 = formation2.split(";")[0].split(",")[1] + formation2.split(";")[0].split(",")[0]
            direction2 = formation2.split(";")[1]

            if ship1[0] == "B":
                plural.append(ship1[0])
                try:
                    letters.remove(ship1[0])
                except:
                    pass
                length1 = 4
            elif ship1[0] == "P":
                plural.append(ship1[0])
                try:
                    letters.remove(ship1[0])
                except:
                    pass
                length1 = 2
            playfields[1][ship1][firsttile1] = ship1[0]
            for a in range(length1 - 1):
                if direction1 == "right":               #at the optional text this makes group through right way for player1
                    playfields[1][ship1][chr(ord(firsttile1[0]) + a + 1) + firsttile1[1:]] = ship1[0]
                else:
                    playfields[1][ship1][firsttile1[0] + str(int(firsttile1[1]) + a + 1)] = ship1[0]
            #--------------------------------------------------------------------------------------------------------------
            if ship2[0] == "B":
                plural.append(ship2[0])
                try:
                    letters.remove(ship2[0])
                except:
                    pass
                length2 = 4
            elif ship2[0] == "P":
                plural.append(ship2[0])
                try:
                    letters.remove(ship2[0])
                except:
                    pass
                length2 = 2
            playfields[2][ship2][firsttile2] = ship2[0]
            for a in range(length2 - 1):
                if direction2 == "right":               #at the optional text this makes group through right way for player2
                    playfields[2][ship2][chr(ord(firsttile2[0]) + a + 1) + firsttile2[1:]] = ship2[0]
                else:
                    playfields[2][ship2][firsttile2[0] + str(int(firsttile2[1]) + a + 1)] = ship2[0]
        if not line2:
            break
    for a in range(len(letters)):
        playfields[1][letters[a]] = {}
        playfields[2][letters[a]] = {}

optional()


def readline(line, row, player):
    column = line.strip("\n").split(";")
    playfields[player][row] = {}
    for a in range(len(column)):
        playfields[player][row][chr(a + 65)] = column[a]            #chr command translates numbers to binary characters
        if playfields[player][row][chr(a + 65)] not in plural:      #Capital "A" 's binary number is 65; B-C-D-E... Goes like 66-67-68-69...
            playfields[player][playfields[player][row][chr(a + 65)]][chr(a+65) + str(row)] = playfields[player][row][chr(a + 65)]
        playfields[player][row][chr(a + 65)] = "-"


def listship(player):
    for key in playfields[player]:
        if isinstance(key, str):
            status = ""
            for a in playfields[player][key]:
                status += playfields[player][key][a]
            if status == "X"*len(playfields[player][key]):
                ships[player][key] = "X"
            else:
                ships[player][key] = "-"


def orderlist(listshow):                #For example There are 4 Patrol Boats and when third of the pb sinks, the output would be --x-
    listshow.sort()                     #To put x to the beginning, I sorted the list and "-"s came before "X"s
    listshow.reverse()                  #Then made it reverse to flip back


def show(round, player, over, winner):
    if over:
        if winner == 3:
            write(("\nIt's Draw!\n"), False)
            write(("Final Information\n"), False)
        else:
            write(("\nPlayer" + str(winner), " Wins!\n"), False)
            write(("Final Information\n"), False)
        for a in range(2):
            for b in playfields[a + 1]:
                if isinstance(b, str):
                    for x in playfields[a + 1][b]:
                        playfields[a + 1][int(x[1:])][x[0]] = playfields[a + 1][b][x]
    else:
        write(("\nPlayer", str(player) + "’s Move\n"), False)
        write(("Round :", "{0: <11}".format(round), "\t\tGrid Size: 10x10\n"), False)
    write(("Player1’s Hidden Board\t\tPlayer2’s Hidden Board"), False)                      #writing table's title
    write(("  A B C D E F G H I J\t\t  A B C D E F G H I J"), False)                        #writing table's letters
    for row in range(10):
        write(('{0: <2}'.format(row + 1)), True)
        for i in range(10):
            write(('{0: <2}'.format(playfields[1][row + 1][chr(i + 65)])), True)
        write(("\t\t"), True)
        write(('{0: <2}'.format(row + 1)), True)
        for i in range(10):
            write(('{0: <2}'.format(playfields[2][row + 1][chr(i + 65)])), True)
        write((""), False)

    carrier = [[],[]]
    bship = [[],[]]
    patrol = [[],[]]
    des = [[],[]]
    sub = [[],[]]

    for i in range(2):
        listship(i + 1)
        for key in playfields[i + 1]:
            if isinstance(key, str):
                if key[0] == "C":
                    carrier[i].append(ships[i+1][key])

                elif key[0] == "B":
                    bship[i].append(ships[i+1][key])

                elif key[0] == "D":
                    des[i].append(ships[i+1][key])

                elif key[0] == "S":
                    sub[i].append(ships[i+1][key])

                else:
                    patrol[i].append(ships[i+1][key])

        orderlist(carrier[i])
        carrier[i] = " ".join(carrier[i])
        orderlist(bship[i])
        bship[i] = " ".join(bship[i])
        orderlist(des[i])
        des[i] = " ".join(des[i])
        orderlist(sub[i])
        sub[i] = " ".join(sub[i])
        orderlist(patrol[i])
        patrol[i] = " ".join(patrol[i])

    write(("\n{0: <12}".format("Carrier"), carrier[0] +  "\t\t\t{0: <12}".format("Carrier"), carrier[1] +
          "\n{0: <12}".format("Battleship"), bship[0]+  "\t\t\t{0: <12}".format("Battleship"), bship[1] +
          "\n{0: <12}".format("Destroyer"), des[0] +    "\t\t\t{0: <12}".format("Destroyer"), des[1] +
          "\n{0: <12}".format("Submarine"), sub[0] +    "\t\t\t{0: <12}".format("Submarine"), sub[1] +
          "\n{0: <12}".format("Patrol Boat"), patrol[0] + "\t\t{0: <12}".format("Patrol Boat"), patrol[1],"\n"), False)


def gameover():
    for a in range(2):
        listship(a+1)
        i = 0
        for key in ships[a+1]:
            if ships[a+1][key] == "X":
                i += 1
            if i == len(ships[a+1]):
                over = True                         #game over
                winner = round(2 - (0.3 * (a+1)))   #I used this nonsense equation because round function is not working properly
                show(0,0, True, winner)
                breakgame = True
                return True


def sink():                                         #Checks for sinked ships
    player1 = open(sys.argv[3], 'r')
    player2 = open(sys.argv[4], 'r')
    moves = {}
    breakgame = False
    line1 = player1.read()
    line2 = player2.read()
    line1 = line1.replace("\n", "")
    line2 = line2.replace("\n", "")

    moves[1] = line1.strip("\n").strip(";").split(";")
    moves[2] = line2.strip("\n").strip(";").split(";")
    moveamount = [0,0,0]

    mistakes = [0,0,0]
    for a in range(len(moves[1]) + len(moves[2])):
        playerToAttack = abs(((a+1)%2)-2)       #at first it prints player1 and player0.In this equations now it prints player1 and player2. You can understand putting a 1 and 0
        playerGetAttacked = round(2 - (0.3 * playerToAttack))
        show(round(((a + 1) / 2) + 0.1), playerToAttack, False, 0)
        moveCount = round(((a + 1)/2) + 0.1) - 1
        try:
            if int(moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[0]) > 10:
                write(("AssertionError: Invalid Operation."), False)
                mistakes[playerToAttack] += 1
            elif ord(moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[1]) - 65 >= 10:
                write(("AssertionError: Invalid Operation."), False)
                mistakes[playerToAttack] += 1
            try:
                for i in range(2):
                    if moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[i] == "":
                        write(("“IndexError: One of the operands are missing"), False)
                tileToAttack = moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[1] + moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[0]
            except IndexError:
                write(("IndexError: One of the operands are missing"), False)

            write(("Enter your move: ", tileToAttack[1:] + "," + tileToAttack[0]), False)
        except IndexError:
            show(0, 0, True, 3)
            breakgame = True
        except ValueError:
            write(("ValueError: Tile Argument(s) is/are wrong"), False)
            mistakes[playerToAttack] += 1
            tileToAttack = moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[1] + moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[0]
        except TypeError:
            mistakes[playerToAttack] += 1
            tileToAttack = moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[1] + moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[0]
            write(("ValueError: Tile Argument(s) is/are wrong"), False)
        except:
            write(("kaBOOM: run for your life!"), False)
        try:
            x = (playfields[playerGetAttacked][int(tileToAttack[1:])][tileToAttack[0]])
        except KeyError:
            mistakes[playerToAttack] += 1
            tileToAttack = moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[1] + moves[playerToAttack][moveCount + mistakes[playerToAttack]].split(",")[0]
            write(("ValueError: Tile Argument(s) is/are wrong"), False)

        moveamount[playerToAttack] += 1
        try:
            for key in playfields[playerGetAttacked]:
                if isinstance(key, str) & (tileToAttack in playfields[playerGetAttacked][key]):
                    playfields[playerGetAttacked][int(tileToAttack[1:])][tileToAttack[0]] = "X"
                    playfields[playerGetAttacked][key][tileToAttack] = "X"
                elif isinstance(key, int) & (playfields[playerGetAttacked][int(tileToAttack[1:])][tileToAttack[0]] == "-"):
                    playfields[playerGetAttacked][int(tileToAttack[1:])][tileToAttack[0]] = "O"
        except:
            write(("ValueError: Tile Argument(s) is/are wrong"), False)
        if moveamount[1] == moveamount[2]:
            breakgame = gameover()
        if breakgame:
            break


def io():                                           #if IO error happens
    files = ["Player1.txt", "Player2.txt", "Player1.in", "Player2.in"]

    for a in range(len(sys.argv)-1):
        try:
            files.remove(sys.argv[a + 1])           #removing every inputs from files list and the rest will be our missing file
        except:
            pass

    missing = " ".join(files)                       #adding the rest to the missing, this will return playerx.xxx is not reachable
    write(("IOError: input file(s) ", missing, " is/are not reachable."), False)

    if missing == "":
        write(("Battle of Ships Game\n"), False)    #This is the title of the game and shows at the top of the output when we rund this file
        read()
        sink()
io()