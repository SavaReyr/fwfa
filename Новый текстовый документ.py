nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f','h',False],
    [1, 2, None],
]

class Iterator:

    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.list_iterator = iter(self.lst)
        self.nested_list = []
        self.position = -1
        return self

    def __next__(self):
        self.position += 1
        if len(self.nested_list) == self.position:
            self.nested_list = None
            self.position = 0
            while not self.nested_list:
                self.nested_list = next(self.list_iterator)
        return self.nested_list[self.position]

def generator(my_list):
    for sub_list in my_list:
        for elem in sub_list:
            yield elem

if __name__ == "__main__":
    flat_list = [item for item in Iterator(nested_list)]
    print(flat_list)

    print("--------------")

    for item in Iterator(nested_list):
        print(item)

    print("--------------")

    for item in generator(nested_list):
        print(item)