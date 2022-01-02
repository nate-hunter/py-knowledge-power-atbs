import random 


# 1. Generate a list of randomly slected 'heads' and 'tails' values
# 2. Check if there is a streak of (6) H or T's in the list

def generateCoinFlips(numberOfFlips):
    results = []
    outcomes = ['H', 'T']
    while len(results) < numberOfFlips:
        coinFlip = random.choice(outcomes)
        results.append(coinFlip)
    return results

def checkIfStreakExists(coinFlips, targetStreak):
    streaks = 0 
    inARowCount = 1
    previousFlip = coinFlips[0]
    for i in range(1, len(coinFlips)):
        flip = coinFlips[i] 
        if flip == previousFlip:
            inARowCount += 1
            if inARowCount == targetStreak:
                streaks += 1
        else:
            inARowCount = 1
        previousFlip = flip   
    return streaks

def app():
    numberOfStreaks = 0
    for experimentNumber in range(1000):
        # 1.
        createdFlips = generateCoinFlips(100)
        # 2.
        numberOfStreaks += checkIfStreakExists(createdFlips, 6)
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))

# Runs program
app()