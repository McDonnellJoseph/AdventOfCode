from functools import lru_cache

with open("full_input.txt", "r") as f:
    input = f.read()

bricks = input.splitlines()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self) -> str:
        return f"{(self.x, self.y)}"



class Brick:
    def __init__(self, brick_string) -> None:
        self.brick_string = brick_string
        self.set_brick_coords(brick_string)
        self.segment = self.set_segment_on_plane()
        self.visited = False

        # Graph Problem 
        self.parents = set()
        self.children = set()

    def set_brick_coords(self, brick_string):
        start_coords, end_coords = brick_string.split("~")
        start_x, start_y, start_z = [
            int(coord) for coord in start_coords.split(",")
        ]
        end_x, end_y, end_z = [int(coord) for coord in end_coords.split(",")]

        self.x = (start_x, end_x)
        self.y = (start_y, end_y)
        self.z = (start_z, end_z)


    def set_segment_on_plane(self):
        self.A = Point(self.x[0], self.y[0])
        self.B = Point(self.x[1], self.y[1])

    @property
    def can_disintigrate(self):
        if self.children == set():
            return True

        for child in self.children:
            if len(child.parents) < 2:
                return False
        return True


    def nb_falling_bricks(self, already_fallen):
        already_fallen.add(self)
        for child in self.children:
            if child.parents - already_fallen == set():
                already_fallen.add(child)
                already_fallen = already_fallen | child.nb_falling_bricks(already_fallen)
        return already_fallen
       

    def __repr__(self) -> str:
        return f"<{self.x[0]}, {self.y[0]}, {self.z[0]}~{self.x[1]}, {self.y[1]}, {self.z[1]}>"

test_brick_a = Brick("1,0,1~1,2,1")
# assert test_brick_a.size == 3

test_brick_b = Brick("0,0,2~2,0,2")
# assert test_brick_b.size == 3

test_brick_c = Brick("0,2,3~2,2,3")
# assert test_brick_c.size == 3
test_brick_d = Brick("0,0,4~0,2,4")
test_brick_f = Brick("0,1,6~2,1,6")
test_brick_g = Brick("1,1,8~1,1,9")
bricks = [Brick(brick) for brick in input.splitlines()]

# Example usage
# For any given brick we want to be able to list all bricks directly above
# Question do we intersect along (x, y)
@lru_cache(maxsize=None)
def brick_intersect(brick_a, brick_b):
    S1 = {(x,y) for x in range(brick_a.x[0], brick_a.x[1] + 1) for y in range(brick_a.y[0], brick_a.y[1]+1)}
    S2 = {(x,y) for x in range(brick_b.x[0], brick_b.x[1] + 1) for y in range(brick_b.y[0], brick_b.y[1]+1)}
    return len(S1.intersection(S2)) > 0

# brick_a = (1, 0), (1, 2)
# brick_c = (0, 2), (2, 2)
test_brick_1 = Brick("7,2,268~7,3,268")
test_brick_2 = Brick("4,7,270~7,7,270")
test_brick_3 = Brick("4,6,276~4,9,276")
test_brick_4 = Brick("5,8,277~6,8,277")
assert brick_intersect(test_brick_f, test_brick_g) is True
assert brick_intersect(test_brick_3, test_brick_4) is False
assert brick_intersect(test_brick_1, test_brick_2) is False
assert brick_intersect(test_brick_a, test_brick_b) is True
assert brick_intersect(test_brick_a, test_brick_c) is True
assert brick_intersect(test_brick_b, test_brick_c) is False
assert brick_intersect(test_brick_c, test_brick_d) is True
# If we order the bricks by size 
bricks.sort(key= lambda x: x.z[0])
# Start from the bottom now we here
for i, brick in enumerate(bricks):
    # Else we find the next brick below
    candidates = []
    for brick_below in bricks[:i]:
        if brick_intersect(brick, brick_below):
            candidates.append(brick_below)
    if not candidates:
        assert brick.z[1] >= brick.z[0]
        brick.z = (1, brick.z[1] - brick.z[0] + 1)
        continue

    # height to drop is the diff between brick and highest candidate 
    best_candidate = max(candidates, key=lambda x: x.z[1])
    # Compute update 
    diff = (brick.z[0] - best_candidate.z[1] - 1)
    assert best_candidate.z[1] < brick.z[0]
    assert diff >= 0
    # Update 
    brick.z = (brick.z[0] -diff, brick.z[1] - diff)


bricks.sort(key = lambda x: x.z[0])

for i, brick in enumerate(bricks):
    # Else we find the next brick below
    candidates = []
    for brick_below in bricks[:i]:
        if brick_below.z[1] == brick.z[0] - 1 and brick_intersect(brick, brick_below):
            candidates.append(brick_below)

    brick.parents = candidates
    for candidate in candidates:
        candidate.children.add(brick)

for brick in bricks:
    brick.parents = set(brick.parents)
    
print(sum([brick.can_disintigrate for brick in bricks]))

# print(sum([len(brick.nb_falling_bricks) for brick in bricks if brick.z[0] == 1]))
print("ùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùù")
# print(bricks[0], len(bricks[0].nb_falling_bricks(set())))
sum = 0
for brick in bricks:
    sum += len(brick.nb_falling_bricks(set()) ) - 1

print(sum)

