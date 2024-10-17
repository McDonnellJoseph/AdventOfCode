with open("input.txt") as f:
    input = f.read()

P = {0: "High Pulse", 1: "Low Pulse"}


class FlipFlop:
    def __init__(self, name, destinations):
        self.name = name.strip()
        self.destinations = [dest.strip() for dest in destinations]
        self.state = 0  # 0 off , 1 on

    def __repr__(self):
        return f"{self.name}"

    def receive(self, pulse, sender_name):
        if pulse == 1:  # 0 high pulse, 1 low pulse
            self.state = 1 - self.state  # Toggle between off and on
            if self.state == 0:  # Turns off and sends low pulse
                self.send(1)
            else:  # Turns on and sends a high pulse
                self.send(0)

    def send(self, pulse):
        for destination in self.destinations:
            print(f"{self} -{P[pulse]}-> {module}")
            Network[destination].receive(pulse, self.name)


class Conjunction:
    def __init__(self, name, connected_inputs):
        self.name = name
        # Defaults to low pulse for each connected input
        self.connected_inputs = {input.strip(): 1 for input in connected_inputs}

    def __repr__(self):
        return f"{self.name}"

    def receive(self, pulse, input):
        self.connected_inputs[input] = pulse

    def send(self):
        if sum(self.connected_inputs.values()) == 0:
            # send low pulse
            pass
        else:
            # send high pulse
            pass


class Broadcaster:
    def __init__(self, destinations):
        self.destinations = [dest.strip() for dest in destinations]

    def __repr__(self):
        return "broadcaster"

    def receive(self, pulse):
        # send pulse to all destinations

        self.send(pulse)

    def send(self, pulse):
        for module in self.destinations:
            print(f"{self} -{P[pulse]}-> {module}")
            Network[module].receive(pulse, "broadcaster")


Network = {}

# Parse input
for line in input.splitlines():
    name, destinations = line.split("->")
    name = name.strip()
    if name == "broadcaster":
        module = Broadcaster(destinations.split(","))
        Network[name] = module

    elif name[0] == "%":
        module = FlipFlop(name[1:], destinations.split(","))
        Network[name[1:]] = module

    elif name[0] == "&":
        module = Conjunction(name[1:], destinations.split(","))
        Network[name[1:]] = module

# Push Button
print("Pushing Button")
Network["broadcaster"].receive(1)
# We're gonna need some kind of priority stack
