"""

This is a mutli-lined comment

Python: https://www.python.org/downloads/
PyCharm: https://www.jetbrains.com/pycharm/download/#section=windows


main.py
Hello World and Strings
Dynamic typing
lists, tuples, sets, dicts
By: Dominick Velardo

"""


def hello_world():
    str = 'Hello World '
    print(str)
    print(str*2)
    print('{} University offers the best {}'.format('Rowan', 'education'))

    name, age = 'Dom', 20
    print(f'Hello, I am {name}. I am {age} years old!')



def dynamic_typing():
    varA = 5
    print(varA)
    varA = 'hello'
    print(varA)
    varA = [1, 'a', 'string']
    print(varA)


list = []
tup = ()
set = {}
dict = {}
def data_structs():
    # Lists are ordered and changeable
    # Duplicates allowed
    print('Lists')
    list1 = ['a', 'b', 'c', 'd']
    list2 = ['d', 'c', 'b', 'a']
    #print(list1, list2[1])
    #print(list1 == list2)
    list2.append('d')
    #print(list2, '\n')
    list3 = [x for x in range(5)]
    #print(list3)

    # Tuples are ordered and unchangable
    # Duplicates allowed
    print('Tuples')
    tup1 = ('a', 'b', 'c', 'd')
    tup2 = ('d', 'c', 'b', 'a')
    #print(tup1, tup2[1])
    #print(tup1 == tup2, '\n')

    # Sets are unordered and unindexed
    # Duplicates not allowed
    print('Sets')
    set1 = {'a', 'b', 'c', 'd'}
    set2 = {'d', 'c', 'b', 'a'}
    #print(set1, set2)
    #print(set1 == set2)
    set2.add('a')
    #print(set2)

    # Dictionaries are ordered and changeable
    # Duplicated not allowed
    print('Dictionaries')
    dict1 = {'a':1, 'b':2, 'c':3, 'd':4}
    dict2 = {'d':4, 'c':3, 'b':2, 'a':1}
    #print(dict1, dict2['d'])
    #print(dict1 == dict2)
    dict2['e'] = 5
    #print(dict2)


if __name__ == '__main__':
    hello_world()
    # dynamic_typing()
    # data_structs()