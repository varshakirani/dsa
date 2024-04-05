from pytest import fixture

@fixture
def linkedlist_input_data1():
    return [1, 2, 3, 4, 5, 6]

@fixture
def linkedlist_input_data2():
    return [1]

@fixture
def linkedlist_input_data3():
    return []


@fixture
def linkedlist_output_data1():
    return 1

@fixture
def linkedlist_output_data2():
    return 1

@fixture
def linkedlist_output_data3():
    return None