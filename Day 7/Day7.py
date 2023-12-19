import functools
import re


def cardByCardCompare(card1, card2):
    cardVals = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13,
                'A': 14}

    card1Val = card1[0]
    card2Val = card2[0]
    char1 = card1[1]
    char2 = card2[1]

    if card1Val < card2Val:
        return -1
    elif card2Val < card1Val:
        return 1

    for i in range(len(char1)):
        if cardVals[char1[i]] < cardVals[char2[i]]:
            return -1
        elif cardVals[char1[i]] > cardVals[char2[i]]:
            return 1

    return 0

def day7p1():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    # card bid value
    cardsBids = {}
    cards = []

    for line in lines:
        x = line.split()
        cardsBids[x[0]] = int(x[1])

        charCount = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0,
                     'A': 0}
        chars = set()
        for char in x[0]:
            chars.add(char)
            charCount[char] += 1

        noChars = len(chars)
        value = 0
        if noChars == 5:
            value = 0

        elif noChars == 4:
            value = 1

        elif noChars == 3:
            for char in chars:
                if charCount[char] == 3:
                    value = 3
                elif charCount[char] == 2:
                    value = 2

        elif noChars == 2:
            for char in chars:
                if charCount[char] == 2:
                    value = 4
                elif charCount[char] == 3:
                    value = 4
                elif charCount[char] == 4:
                    value = 5

        else:
            value = 6

        cards.append([value, x[0]])

    sortedCards = sorted(cards, key=functools.cmp_to_key(cardByCardCompare))
    print(sortedCards)

    total = 0
    rank = 1
    for card in sortedCards:
        total += rank * cardsBids[card[1]]
        rank += 1
    # find weakest to strongest
    # weakest = no pairs so 23456 or 34567 45678
    return total



def day7p2():
    lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
    cards = []
    cardsBids = {}

    for line in lines:
        x = line.split()
        cardsBids[x[0]] = int(x[1])

        charCount = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, 'T': 0, 'J': 0, 'Q': 0, 'K': 0,
                     'A': 0}
        chars = set()
        for char in x[0]:
            chars.add(char)
            charCount[char] += 1

        noChars = len(chars)
        value = 0
        if noChars == 5:
            value = 0

        elif noChars == 4:
            value = 1

        elif noChars == 3:
            for char in chars:
                if charCount[char] == 3:
                    value = 3
                elif charCount[char] == 2:
                    value = 2

        elif noChars == 2:
            for char in chars:
                if charCount[char] == 2:
                    value = 4
                elif charCount[char] == 3:
                    value = 4
                elif charCount[char] == 4:
                    value = 5

        else:
            value = 6

        if value == 0:
            if charCount['J'] == 1:
                value = 1
        elif value == 1:
            if charCount['J'] == 1 or charCount['J'] == 2:
                value = 3
        elif value == 2:
            if charCount['J'] == 1:
                value = 4
            elif charCount['J'] == 2:
                value = 5
        elif value == 3:
            if charCount['J'] == 1 or charCount['J'] == 3:
                value = 5
        elif value == 4:
            if charCount['J'] == 2 or charCount['J'] == 3:
                value = 6
        elif value == 5:
            if charCount['J'] == 1 or charCount['J'] == 4:
                value = 6


        cards.append([value, x[0]])

    sortedCards = sorted(cards, key=functools.cmp_to_key(cardByCardCompare))
    print(sortedCards)

    total = 0
    rank = 1
    for card in sortedCards:
        total += rank * cardsBids[card[1]]
        rank += 1
    # find weakest to strongest
    # weakest = no pairs so 23456 or 34567 45678
    return total

print(day7p2())
