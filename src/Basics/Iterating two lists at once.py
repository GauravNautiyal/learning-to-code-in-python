from itertools import chain

test_list1 = [4, 5, 3, 6, 2]
test_list2 = [7, 9, 10, 0]

# one approach


def simpleapproach():
    for i in test_list1 + test_list2:
        print(i, end=" ")
        print()


simpleapproach()


##better approach


def chain_approach():
    for i in chain(test_list1, test_list2):
        print(i, end=" ")


chain_approach()
