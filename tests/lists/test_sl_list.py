from data_structures.lists import SLList


def test_add_1():
    sl_list = SLList()
    sl_list.add(1, 0)

    assert sl_list.get(0) == 1


def test_add_2():
    sl_list = SLList(5)
    sl_list.add(10, 1)
    sl_list.add(15, 2)

    assert sl_list.get(0) == 5
    assert sl_list.get(1) == 10
    assert sl_list.get(2) == 15


def test_add_first_1():
    sl_list = SLList()
    sl_list.add_first(1)
    assert sl_list.get_first() == 1


def test_add_first_2():
    sl_list = SLList(1)
    sl_list.add_first(2)
    assert sl_list.get_first() == 2
    assert sl_list.get(1) == 1


def test_add_last_1():
    sl_list = SLList()
    sl_list.add_last(1)
    assert sl_list.get_first() == 1


def test_add_last_2():
    sl_list = SLList(1)
    sl_list.add_last(2)
    assert sl_list.get(1) == 2


def test_get():
    sl_list = SLList(1)
    assert sl_list.get(0) == 1


def test_get_first():
    sl_list = SLList(1)
    assert sl_list.get_first() == 1


def test_remove():
    sl_list = SLList(1)
    sl_list.add_first(2)
    assert sl_list.remove(1) == 1
    assert sl_list.remove(0) == 2


def test_remove_last():
    sl_list = SLList(1)
    sl_list.add_first(2)
    sl_list.add_first(3)
    assert sl_list.remove_last() == 1
    assert sl_list.remove_last() == 2
    assert sl_list.remove_last() == 3


def test_size():
    sl_list = SLList(1)
    sl_list.add_first(0)
    sl_list.add_first(0)
    assert sl_list.size() == 3
