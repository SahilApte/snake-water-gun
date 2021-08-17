import random
comp_points = 0
user_points = 0

def func1():
    contents = ['s', 'w', 'g']
    comp_input = random.choice(contents)
    chances = 0
    # user_input = input("enter s: snake, w: water, g: gun:\n")
    comp_points = 0
    user_points = 0
    # while chances >= 10:
    while chances < 10:
        chances = chances + 1

        if chances > 10:
            print("game over")

            def scorecard():
                global user_points
                global comp_points
                if user_input == comp_input:

                    print("its a tie mann")

                elif user_points > comp_points:
                    print("you win buddy")

                elif comp_points > user_points:

                    print("compu wins")

            scorecard()

            break
        else:
            user_input = input("enter s: snake, w: water, g: gun:\n")

        if user_input == 's' and comp_input == 'w':
            print("congratulations you win !!", )
            user_points += 1
            print("chances left are", (10 - chances))
            continue
        elif user_input == 'w' and comp_input == 'g':
            print("congratulations you win")
            user_points += 1
            print("chances left are", (10 - chances))
            continue
        elif user_input == 'g' and comp_input == 's':
            print("congratulations you win")
            user_input += 1
            print("chances left are", (10 - chances))
            continue
        elif user_input == 's' and comp_input == 'w':
            print("congratulations you win !!")
            user_points += 1

            print("chances left are", (10 - chances))
            continue
        elif user_input == 's' and comp_input == 'g':
            # b = b + 1
            print("sorry you were shot by the gun", )
            comp_points += 1

            print("chances left are", (10 - chances))

            continue
        elif user_input == 's' and comp_input == 's':
            # c = +1
            print("Its a tie", )
            print("chances left are", (10 - chances))

            continue

        elif user_input == 'w' and comp_input == 's':
            # b = b + 1
            print("sorry snake drank your water", )
            comp_points += 1
            print("chances left are", (10 - chances))

            continue
        elif user_input == 'w' and comp_input == 'g':
            # a = a + 1
            print("congratulations you win", )
            user_points += 1
            print("chances left are", (10 - chances))

            continue
        elif user_input == 'w' and comp_input == 'w':
            print("Its a tie", )
            print("chances left are", (10 - chances))

            continue

        elif user_input == 'g' and comp_input == 's':
            # a = a + 1
            print("congratulations you win", )
            user_points += 1
            print("chances left are", (10 - chances))

            continue
        elif user_input == 'g' and comp_input == 'w':
            # b = b + 1
            print("sorry the gun drowned into water", )
            comp_points += 1
            print("chances left are", (10 - chances))

            continue
        elif user_input == 'g' and comp_input == 'g':
            print("Its a tie", )
            print("chances left are", (10 - chances))

            continue


func1()
