import random
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
bl3point = ['A', 'B', 'C', 'D', 'E', 'F']
rg3point = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
bl1point = [['B'], ['A'], ['D'], ['C'], ['F'], ['E']]
rg1point = [['H', 'I'], ['G', 'I'], ['G', 'H'], ['K'], ['J'], ['M'], ['L'], []]


def note(blSet, rgSet):
    total = 0
    for (a,b) in zip(bl3point, blSet):
        if a == b:
            total += 3
    for (a,b) in zip(rg3point, rgSet):
        if a == b:
            total += 3
    for (alist, b) in zip(bl1point, blSet):
        if b in alist:
            total += 1
    for (alist, b) in zip(rg1point, rgSet):
        if b in alist:
            total += 1
    return total


frequence = [0] * 43
total = 0
for i in range(100000):
    a = note(random.sample(bl3point, 6), random.sample(rg3point, 8))
    total += a
    frequence[a] += 1

print(total)
print(frequence)
