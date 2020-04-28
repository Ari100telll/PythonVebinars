def add_sequence(sequence):
    # sequence.append("new string")
    sequence = sequence * 2
    print(sequence * 2)


def add_element_to_list_in_tuple(sequence: tuple):
    sequence[0].append(10)


def play_with_slicing():
    my_list = [3, "12", 3.2, 6, (2, 3), "12", "4"]
    print("slice_1: " + str(my_list[2:5]))
    print("slice_2: " + str(my_list[2:7:2]))


if __name__ == '__main__':
    # slicing
    play_with_slicing()

    test_list = [1, 2, 3, 4]
    print("before:" + str(test_list))
    add_sequence(test_list)
    print("after:" + str(test_list))
    if 2 in test_list:
        print("I`m happy")

    add_sequence(("first", "second"))

    # create tuple with lists
    new_tuple = ([1, 2], [3, 4])
    print("before:" + str(new_tuple))
    add_element_to_list_in_tuple(new_tuple)
    print("after:" + str(new_tuple))
