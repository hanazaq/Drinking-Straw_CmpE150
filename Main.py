glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
# ***********************************
# HW2
# Name: HANAA ZAQOUT
# Student No: 2020400381
# ***********************************

should_stop = False
# max number of printed glasses is glass_size+1
for glass in range(glass_size + 1):  # print many glasses

    # o
    #  o
    #   o
    #    o
    for straw in range(straw_pos):  # the num of lines
        for space_start in range(straw):  # spaces before o of straw
            print(" ", end="")
        print("o")

    space = 0  # space before the \ for both empty and full glasses

    # \        /
    #  \      /
    #   \    /
    #    \  /
    for empty in range(glass):  # 0 1 2
        for space2 in range(space):
            print(" ", end="")
        print("\\", end="")

        #drinking a line inside the glass

        ultimate_space = 2 * (glass_size - empty)  # \      / the total inner space including o

        # assign the variable before the loop; because when straw_pos=1,
        # before_space become undefind for the rest of the code and return an Error.

        before_space = -1
        for before_space in range(straw_pos - 1):  # \   o
            print(" ", end="")
        print("o", end="")

        after_space_ensure = ""  # will be used in the upcoming if condition, it simplifies the idea
        for after_space in range(ultimate_space - before_space - 2):  # o   / gives the number of the left required spaces
            print(" ", end="")
            after_space_ensure += " "

        if (len(after_space_ensure) <= 1):  # check if drinking should stop, as the straw hit the glass from inside
            should_stop = True

        #end drinking the line inside the glass

        print("/")
        space += 1

    # \********/
    #  \******/
    #   \****/
    #    \**/

    for juice in range(glass_size - glass, 0, -1):  # 3 2 1
        for space2 in range(space):
            print(" ", end="")
        print("\\", end="")

        for star in range(juice * 2):  # line full with juice
            print("*", end="")
        print("/")
        space += 1

    # --
    # ||
    # ||
    # ||

    for line in range(4):  # the last four lines
        for space_bottom in range(glass_size):  # the bottom part is in the center
            print(" ", end="")
        if line == 0:  # first line --
            for i in range(2):
                print("-", end="")
            print()
        else:  # 3 time ||
            for ii in range(2):
                print("|", end="")
            print()

    if should_stop == True: #stop drinking and stop printing
        break

#Enjoy drinking!!!
#Do you want another cup?

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
