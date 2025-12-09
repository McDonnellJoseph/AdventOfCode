import random
class Range:
    def __init__(self,min, max):
        self.min = min 
        self.max = max

    @classmethod
    def from_str(cls, str_repr):
        a, b= str_repr.split("-")
        return cls(int(a), int(b))
    def __eq__(self, other_range):
        return self.min == other_range.min and self.max == other_range.max

    def __repr__(self):
        return f"{self.min}-{self.max}"
    
    def __len__(self):
        return self.max + 1 - self.min

    def __contains__(self, obj):
        if isinstance(obj, Range):
            if self.min <= obj.min and self.max >= obj.max:
                return True
            return False
        return self.min <= obj and self.max >= obj

    def overlaps(self, other_range):
        if min(self.max, other_range.max) - max(self.min, other_range.min ) >= 0:
            return True
        return False

    def overlaped_range(self, other_range):
        if other_range in self:
            return Range(self.min, self.max)

        if self.overlaps(other_range):
            return Range(min(self.min, other_range.min), max(self.max, other_range.max))
        return False


def test():
    base_range = Range(5, 10)

    # fully inclusive
    inside = Range(6, 8)
    assert inside in base_range
    assert  base_range.overlaped_range(inside) == base_range

    # bottom inclusive
    bottom = Range(3, 7)
    assert bottom not in base_range
    assert base_range.overlaped_range(bottom) == Range(3, 10)
    assert bottom.overlaped_range(base_range) == Range(3, 10)

    # top inclusive
    top = Range(8, 11)
    assert base_range.overlaped_range(top) == Range(5, 11)
    assert top.overlaped_range(base_range) == Range(5, 11)


    assert Range(3, 5).overlaps(Range(2,3))

test()


with open("input.txt") as f:
    ipt = f.read()
ranges, ids = ipt.split("\n\n")


ranges = [Range.from_str(line) for line in ranges.splitlines()] # type: ignore

count = 0
for id in ids.splitlines():
    for rng in ranges:
        if int(id) in rng:
            count += 1
            break

print("Part 1")
print(count)


prev_len = len(ranges) + 1
print("Initial Ranges")
print(ranges)

def merge_ranges(ranges):
    if len(ranges) == 0:
        return []
    if len(ranges) == 1:
        return [ranges[0]]
    if len(ranges) == 2:
        res = ranges[0].overlaped_range(ranges[1])
        if res:
            return [res]
        else:
            return [ranges[0], ranges[1]]

    
    return merge_ranges(ranges[:len(ranges)//2]) + merge_ranges(ranges[len(ranges)//2:]) 

prev_len = len(ranges) + 1

def merge(ranges):
    prev_len = len(ranges) + 1
    CAC = 0
    while prev_len > len(ranges):
        if CAC == 0:
            key_func = lambda x: x.min
            CAC = 1
        if CAC == 1:
            key_func = lambda x: x.max
            CAC = 0


        ranges = sorted(ranges, key=key_func)

        prev_len = len(ranges)
        ranges = merge_ranges(ranges)

    return ranges

def check(ranges):
    for range in ranges:
        for test_range in ranges:
            if not (range is test_range) and (range.overlaps(test_range)):
                return False
    return True

while not check(ranges):

    #random.shuffle(ranges)
    ranges = merge(ranges)
check(ranges)


print(sum(len(r) for r in ranges))