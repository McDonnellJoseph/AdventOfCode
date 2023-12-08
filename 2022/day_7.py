with open("input.txt", "rb") as f:
    input = f.read().decode("utf-8")


class FileSystem:
    def __init__(self, parent, name):
        self.parent = parent
        self.files = list()
        self.children = list()
        self.name = name
        self.is_ls = False
        self.size = 0

    def __str__(self):
        return self.name

    def deep_size(self):
        if self.children:
            return sum([child.deep_size() for child in self.children]) + self.size
        else:
            return self.size

    def sum_at_most(self, most):
        # stopping condition
        if self.deep_size() <= most:
            size = self.deep_size()
        else:
            size = 0
        if not self.children:
            return size

        # else
        else:
            return sum([child.sum_at_most(most) for child in self.children]) + size

    def find_smallest(self, mini, smallest):
        # if not self.children:
        #     return None
        # else:
        #     smallest = min(smallest, [child.deep_size() for child in self.children])
        #     return

        # We want to iterate to the root of the tree
        # Return the size
        # Then we append the size

        # if not
        if self.deep_size() >= mini and self.deep_size() < smallest:
            smallest = self.deep_size()

        if not self.children:
            return smallest
        else:
            sizes = []
            for child in self.children:
                sizes.append(child.find_smallest(mini, smallest))
            return min(sizes)


def check_dir_exists(fs, name):
    for i, dir in enumerate(current_dir.children):
        if dir.name == words[-1]:
            return dir
    return False


root = FileSystem(None, "/")
current_dir = root
for line in input.split("\n")[1:-1]:
    words = line.split()
    # This means we are in a command
    if words[0] == "$":
        if words[1] == "cd":
            if words[-1] == "..":
                current_dir = current_dir.parent
            else:
                child_dir = check_dir_exists(current_dir, words[-1])
                if child_dir:
                    current_dir = child_dir

                else:
                    new_dir = FileSystem(current_dir, words[-1])
                    current_dir.children.append(new_dir)
                    current_dir = new_dir
        else:
            current_dir.is_ls = True
    else:
        if words[0] == "dir":
            child_dir = check_dir_exists(current_dir, words[1])
            if not child_dir:
                current_dir.children.append(FileSystem(current_dir, words[1]))
        else:
            current_dir.size += int(words[0])
print(root.deep_size())
free_space = 70000000 - root.deep_size()
print(root.find_smallest(30000000 - free_space, root.deep_size()))
