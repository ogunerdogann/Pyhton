import random
for i in range(5):
    print(random.random()) 
# We called a function which named random() in a module which named random
# random() function generates float numbers between 0 and 1

for i in range(5):
    print(random.uniform(10,30))
# uniform() function generates random float numbers between the intervals, that we give.

for i in range(3):
    print(random.randrange(10,30,3))
# randrange() function generates integer numbers between the interval and step that we give.
# But we don't have to give step.

for i in range(3):
    print(random.randint(1,5))
# randint() function generate integer numbers in intervals that we give.

list_colors = ["Black","Grey","Yellow","Red","Blue"]
print(random.choice(list_colors))
# choise() function picks randomly an element of a list.

random.shuffle(list_colors) 
print(list_colors)
# shuffle() function shuffles our list elements.

print(random.sample(list_colors,3))
# sample() function take samples froma list. In this case, we take 3 samples from our list.

# Lets make an example
dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} # keys are the numbers on a dice, values are probability of them.
for i in range(1000000):              # dice 1000000 times
    number_dice = random.randint(1,6)   
    dice[number_dice] += 1            # how many times a number was on dice(for example how many times came 1)

for j in dice:
    print(f"probability of to come {j} on a dice is {dice[j] / 1000000}")

# Mathematically the probability is 1/6. The results are too close.
# if we dice more than 1000000 times, the results will even closer.

# Lets calculate what is the probability of to come 6-6?
six_six = 0
for i in range(1000000):
    number_dice = random.randint(1,6)
    number_dice2 = random.randint(1,6)
    if number_dice == 6 and number_dice2 == 6:
        six_six += 1
print(f"Probability of to come 6-6 on two dice is {six_six/1000000}")
# Matematically the probability is 1/36 and the results are too close.