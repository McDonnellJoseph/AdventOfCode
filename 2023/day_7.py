from collections import Counter

with open("input.txt", "r") as f:
    input = f.read()

lines = input.splitlines()

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
    if "J" in hand_1:
        oc1_j = oc1.pop("J")
    else:
        oc1_j = 0

    if "J" in hand_2:
        oc2_j = oc2.pop("J")
    else:
        oc2_j = 0
    oc1_values, oc2_values = sorted(oc1.values(), reverse=True), sorted(
        oc2.values(), reverse=True
    )
    oc1_keys, oc2_keys = sorted(oc1, key=oc1.get, reverse=True), sorted(
        oc2, key=oc2.get, reverse=True
    )
    if len(oc1_values) == 0:
        oc1_values.append(0)

    if len(oc2_values) == 0:
        oc2_values.append(0)
    if oc1_values[0] + oc1_j > oc2_values[0] + oc2_j:
        return True
    if oc2_values[0] + oc2_j > oc1_values[0] + oc1_j:
        return False

    if oc1_values[0] + oc1_j < 5 and oc2_values[0] + oc2_j < 5:
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
