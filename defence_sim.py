import random
import matplotlib.pyplot as plt

des_atk = int(input("Nombre de des en attaque: "))
warbands_atk = int(input("Nombre de warbands attaquant: "))
des_dfs = int(input("Nombre de des en defence: "))
warbands_dfs = int(input("Nombre de warbands defence: "))

def roll_dice():
    return random.randint(1, 6)

def attack_rolls(n, warbands):
    s = {
        1: 1,
        2: 1,
        3: 1,
        4: 2,
        5: 2,
    }
    tot = 0
    for _ in range(n):
        roll = roll_dice()
        if roll == 6:
            if warbands > 0:
                warbands -= 1
                tot += 4
        else:
            tot += s[roll]

    return (tot//2) + warbands

def defence_rolls(n, warbands ):
    s = {
        1: 0,
        2: 0,
        3: 1,
        4: 1,
        5: 2
        }
    factor = 1
    tot = 0

    for _ in range(n):
        roll = roll_dice()
        if roll == 6:
            factor *= 2
        else:
            tot += s[roll]

    return tot*factor + warbands

defences = []
attaques = []
resultats = []

for _ in range(99999):
    defences.append(defence_rolls(des_dfs, warbands_dfs))
    attaques.append(attack_rolls(des_atk, warbands_atk))
    if attaques[-1] > defences[-1]:
        resultats.append(1)
    else:
        resultats.append(0)


def to_percent(c):
    return str(c*100)[:5]+"%"

win_rate = (sum(resultats) / len(resultats))
print(to_percent(win_rate))

# Print the average
# print("MEAN", sum(arr) / len(arr))
# print("LOW_ROLL", str(len(arr2)*100 / len(arr)) + "%")
# print("MEDIANE", str(arr[len(arr)//2]))


# # Plot the distribution
# plt.hist(arr, bins=30, edgecolor='black', alpha=0.75)
# plt.title("Distribution of `arr`")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
