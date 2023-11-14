import random

def drunkard(distance, step_count):
    position = distance / 2
    home = 0 
    pub = distance 

    for step in range (step_count):
        step = [-1, 1] #step left (-1) step right (+1)
        opilec = random.choice(step) #drunkyard will make random steps either to the right or left
        position += opilec

        print("home", "." * int(position) + "*" + "." * int(distance - position), "pub") 

        if position == home:
            return "Ended up at home!"
        elif position == pub:
            return "Ended up in the pub again!"
        pass

    else:
        return "Simulace skončila po vyčerpání kroků"
    
result = drunkard(10, 25)
print(result)

