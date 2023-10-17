import random


def simulation(path_length=15, num_iterations=30):
    position = path_length // 2
    for _ in range(num_iterations):
        position += random.choice([1, -1])
        if position < 0:
            print("HOSPODA")
            return
        elif position >= path_length:
            print("DOMOV")
            return
        print("".join(["X" if i == position else "." for i in range(path_length)]))
    print("USNUL")


simulation()
