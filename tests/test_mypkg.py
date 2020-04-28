from overload import overload


def test_funct(first, second):
    """
    return the sum of 2 ints
    >>> test_funct(10, 20)
    30
    """
    return first + second


class StaticAndOverloads:
    worker_name = "some name"

    @staticmethod
    def do_work():
        print("static work")

    def sing_a_song(self):
        """
        >>> obj.sing_a_song()
        'some name is singing'
        """
        return "%s is singing" % StaticAndOverloads.worker_name

    @overload
    def print_data(self, first, second):
        print(str(first) + ", " + str(second))

    @print_data.add
    def print_data(self, first: int, second: int):
        """
        return the sum of 2 ints
        >>> obj.print_data(10, 20)
        30
        """
        return first + second


if name == 'main':
    import doctest

    doctest.testmod(verbose=True, extraglobs={"obj": StaticAndOverloads()})
    my_object = StaticAndOverloads()
    my_object.print_data(23, 45)
    my_object.print_data("34", "78")
    print(my_object.sing_a_song())
