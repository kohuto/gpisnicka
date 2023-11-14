import random, time

PATH_LENGHT = 11
path = ["." for x in range(PATH_LENGHT)]

current_pos = PATH_LENGHT // 2

steps = 0
MAX_STEPS = 15

def print_path(path):
    print(f"home {' '.join(path)} pub")


def ending(current_pos, steps, max_steps):
    if current_pos < 0:
        print("MATTY made it home!")
    elif current_pos >= PATH_LENGHT:
        print("MATTY ended in the pub again!")
    elif steps == max_steps:
        print("MATTY has fallen asleep.")


def game(steps, max_steps, path, current_pos):
    # print path without making a move first
    path[current_pos] = "M" # M which stands for Matty
    print_path(path)

    # main loop
    while PATH_LENGHT > current_pos >= 0 and steps < max_steps:
        steps += 1
        path[current_pos] = "."
        
        random_number = random.choice([-1, 1])
        current_pos += random_number

        # if you got home or to the pub
        if PATH_LENGHT > current_pos >= 0:
            path[current_pos] = "M" 
        else:
            break

        print_path(path)
        time.sleep(0.5)

    ending(current_pos, steps, max_steps)


game(steps, MAX_STEPS, path, current_pos)