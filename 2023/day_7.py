from collections import Counter

with open("input.txt", "r") as f:
    input = f.read()

lines = input.splitlines()[:10]

hands, bids = [], []

for line in lines:
    hand, bid = line.split()
    hands.append(hand)
    bids.append(bid)


ASSOCIATIONS = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "T": 3,
    "9": 4,
    "8": 5,
    "7": 6,
    "6": 7,
    "5": 8,
    "4": 9,
    "3": 10,
    "2": 11,
    "J": 12,
}


def is_greater(hand_1, hand_2):
    oc1, oc2 = Counter(hand_1), Counter(hand_2)
    oc1_values, oc2_values = sorted(oc1.values(), reverse=True), sorted(
        oc2.values(), reverse=True
    )

    if oc1_values[0] + oc1["J"] > oc2_values[0] + oc2["J"]:
        return True
    if oc2_values[0] + oc2["J"] > oc1_values[0] + oc1["J"]:
        return False
    if oc1_values[1] > oc2_values[1]:
        return True
    if oc2_values[1] > oc1_values[1]:
        return False
    for let1, let2 in zip(hand_1, hand_2):
        if ASSOCIATIONS[let1] < ASSOCIATIONS[let2]:
            return True
        if ASSOCIATIONS[let2] < ASSOCIATIONS[let1]:
            return False


def sort_hands(hands, bids):
    n = len(hands)
    for i in range(len(hands)):
        swapped = False

        for j in range(0, n - i - 1):
            # print("fozjf")
            # print(hands[j], hands[j + 1], is_greater(hands[j], hands[j + 1]))
            if is_greater(hands[j], hands[j + 1]):
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
                bids[j], bids[j + 1] = bids[j + 1], bids[j]
                swapped = True
        if swapped == False:
            break
    return hands, bids


sorted_hands, sorted_bids = sort_hands(hands, bids)

# print(sorted_hands)
# print(sorted_bids)

total = 0
print(sorted_hands)
for i in range(len(sorted_bids)):
    print(int(sorted_bids[i]))
    total += int(sorted_bids[i]) * (i + 1)
print(total)
