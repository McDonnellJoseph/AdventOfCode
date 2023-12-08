with open("input.txt") as f:
    input = f.read()


class Monkey:
    def __init__(self, start_items, operation, test_nb, true_monkey, false_monkey):
        self.items = start_items
        self.operation = operation
        self.test_nb = test_nb

        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

        self.round_counter = 0

        self.n_inspections = 0

    def test(self, item):
        worry = self.operation(item)
        return (worry % self.test_nb) == 0

    def turn(self):
        for item in self.items:
            if self.test(item):
                self.true_monkey.items.append(item)
            else:
                self.false_monkey.items.append(item)
            self.items.remove(item)


monkeys = []
for line in input.split("\n\n"):
    info = line.splitlines()
    start_items = [int(el.strip(",")) for el in info[1].split(":")[1].split()]

    a, operator, b = info[2].split()[-3:]
    a_is_old = False
    b_is_old = False
    if a == "old":
        a_is_old = True
    elif b == "old":
        b_is_old = True

    if operator == "+":
        if a_is_old and b_is_old:

            def func(x):
                return x + x

        elif a_is_old:

            def func(x):
                return x + int(b)

        elif b_is_old:

            def func(x):
                return int(a) + x

    elif operator == "*":
        if a_is_old and b_is_old:

            def func(x):
                return x * x

        elif a_is_old:

            def func(x):
                return x * int(b)

        elif b_is_old:

            def func(x):
                return int(a) * x

    test_nb = int(info[3].split()[-1])
    true_monkey = int(info[4].split()[-1])
    false_monkey = int(info[5].split()[-1])
    monkey = Monkey(
        start_items=start_items,
        operation=func,
        test_nb=test_nb,
        true_monkey=true_monkey,
        false_monkey=false_monkey,
    )

    monkeys.append(monkey)


def play_turn(monkey: Monkey, monkeys: list[Monkey]):
    print("Items at start of turn", monkey.items)
    for item in monkey.items:
        level = monkey.operation(item) // 3
        print("this the worry level", monkey.operation(item))
        level = level % monkey.test_nb
        if level == 0:
            monkeys[monkey.true_monkey].items.append(item)
            print("Throwing to monkey", monkey.true_monkey)
            print("True monkey items", monkeys[monkey.true_monkey].items)
        else:
            monkeys[monkey.false_monkey].items.append(item)
            print("Throwing to monkey", monkey.false_monkey)
            print("False monkey items", monkeys[monkey.false_monkey].items)
        monkey.n_inspections += 1
    monkey.items = []
    print("Items at end of Turn", monkey.items)


for i in range(1):
    for j, monk in enumerate(monkeys):
        print(f"Turn of monkey {j}")
        play_turn(monk, monkeys)

for monk in monkeys:
    print(monkey.n_inspections)
