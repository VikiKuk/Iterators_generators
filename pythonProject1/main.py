class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter = 0
        self.flat_list = []
        for sublist in self.list_of_list:
            for item in sublist:
                self.flat_list.append(item)
        return self

    def __next__(self):
        if self.counter < len(self.flat_list):
            self.counter += 1
            return self.flat_list[self.counter-1]
        else:
            raise StopIteration



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print ('OK')


if __name__ == '__main__':
    test_1()