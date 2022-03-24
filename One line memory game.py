# FCAI – Programming 1 
# Program Name: one line memory game.py
# Author :Abdelrhman sayed ali
print("\nWelcome, user\n") 
import random
import os
from time import sleep

# os.system('cls' if os.name == 'nt' else 'clear')

letter_locations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
char_list = ['A', 'B', 'A', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J']

print(f"letter locations :\n{letter_locations}")
print(f"char_list :\n{char_list}")
random.shuffle(char_list)

print(f"Meet the letters that are in random order :\n{char_list}")


def loop_game():
    global score_o_p1
    global score_o_p2
    score_o_p1 = 0
    score_o_p2 = 0

    while score_o_p1 + score_o_p2 != (len(char_list) / 2):
        sleep(5)
        os.system('cls')
        print("** PLAYER ONE ** ")
        c_o_i_1 = input("please player one  , Enter Choose the first place of the char from 0 to 19 in list : ")
        c_o_i_2 = input("please player one , Enter Choose the second place of the char from 0 to 19 in list  : ")
        if str(c_o_i_2).isdigit() == False or str(c_o_i_1).isdigit() == False:
            print("Please ,player one enter number from 0 to 19")
            continue
        elif int(c_o_i_2) >= 19 or int(c_o_i_1) >= 19:
            print("Please player one  ,Enter number from 0 to 19 :")
            continue
        elif int(c_o_i_2) < 0 or int(c_o_i_1) < 0:
            print("Please player one ,Enter number from 0 to 19 :")
            continue
        elif int(c_o_i_2) == int(c_o_i_1):
            print("Please player one ,Do not use the same number")
            continue

        elif char_list[int(c_o_i_1)] == char_list[int(c_o_i_2)]:

            char_list.pop(int(c_o_i_1))
            char_list.insert(int(c_o_i_1), '*')
            char_list.pop(int(c_o_i_2))
            char_list.insert(int(c_o_i_2), '*')
            score_o_p1 += 1

            for i in range(0, 20, 1):
                if int(c_o_i_1) != i and int(c_o_i_2) != i:
                    print(letter_locations[i], end=' ', )
                else:
                    print(char_list[i], end=' ')
            print(f"The score of player one is :{score_o_p1}")

        elif int(c_o_i_2) != int(c_o_i_1):
            for i in range(0, 20, 1):
                if int(c_o_i_1) != i and int(c_o_i_2) != i:
                    print(letter_locations[i], end=' ', )

                else:
                    print(char_list[i], end=' ')
            print(f"\nThe score of player one is :{score_o_p1}")
        sleep(5)
        os.system('cls')

        print("\n** PLAYER TWO ** ")

        c_o_i_3 = input("please player two  , Enter the first place of the char from 0 to 19 :")
        c_o_i_4 = input("please player two , Enter the second place of the char from 0 to 19 : ")
        if str(c_o_i_3).isdigit() == False or str(c_o_i_4).isdigit() == False:
            print("SORRY ,Please player two enter number from 0 to 19")
            continue

        elif int(c_o_i_3) >= 19 or int(c_o_i_4) >= 19:
            print("please player two ,Enter number from 0 to 19 :")
            continue
        elif int(c_o_i_3) < 0 or int(c_o_i_4) < 0:
            print("Please player two ,Enter number from 0 to 19 :")
            continue
        elif int(c_o_i_3) == int(c_o_i_4):
            print("Please player two ,Do not use the same number")
            continue
        elif char_list[int(c_o_i_3)] == char_list[int(c_o_i_4)]:
            char_list.pop(int(c_o_i_3))
            char_list.insert(int(c_o_i_3), '*')
            char_list.pop(int(c_o_i_4))
            char_list.insert(int(c_o_i_4), '*')
            score_o_p2 += 1

            for i in range(0, 20, 1):
                if int(c_o_i_1) != i and int(c_o_i_2) != i:
                    print(letter_locations[i], end=' ', )

                else:
                    print(char_list[i], end=' ')
            print(f"The score of player two is :{score_o_p2}")

        elif char_list[int(c_o_i_3)] != char_list[int(c_o_i_4)]:
            for i in range(0, 20, 1):
                if int(c_o_i_3) != i and int(c_o_i_4) != i:
                    print(letter_locations[i], end=' ')
                else:
                    print(char_list[i], end=' ')
            print(f"\nThe score of player two is :{score_o_p2}")
        sleep(5)
        os.system('cls')


loop_game()


def winner():
    global score_o_p1
    global score_o_p2
    if score_o_p1 > score_o_p2:
        print(f"Score of first player :{score_o_p1}\n")
        print(f"Score of second player :{score_o_p2}\n")
        print("***THE WINNER IS PLAYER ONE***")
    elif score_o_p1 < score_o_p2:
        print(f"Score of first player :{score_o_p1}\n")
        print(f"Score of second player :{score_o_p2}\n")
        print("***THE WINNER IS PLAYER TWO***")
    elif score_o_p1 == score_o_p2:
        print(f"Score of first player :{score_o_p1}\n")
        print(f"Score of second player :{score_o_p2}\n")
        print("Please ,Try again ***GAME IS DRAW***")
        loop_game()


winner()


