from data_structures.lists import DLList


def test_add():
    dl_list = DLList()
    dl_list.add(1, 0)
    assert dl_list.get(0) == 1


def test_add_first():
    dl_list = DLList()
    dl_list.add_first(1)
    assert dl_list.get(0) == 1


def test_add_last():
    dl_list = DLList(1)
    dl_list.add_last(2)
    assert dl_list.get(0) == 1
    assert dl_list.get(1) == 2


def test_get():
    dl_list = DLList()
    dl_list.add(2, 0)
    dl_list.add_first(1)
    dl_list.add_last(3)
    assert dl_list.get(0) == 1
    assert dl_list.get(1) == 2
    assert dl_list.get(2) == 3


def test_get_first():
    dl_list = DLList()
    dl_list.add_first(1)
    assert dl_list.get_first() == 1


def test_remove():
    dl_list = DLList()
    dl_list.add_first(1)
    dl_list.add_last(2)
    assert dl_list.remove(1) == 2
    assert dl_list.remove(0) == 1


def test_remove_last():
    dl_list = DLList(1)
    dl_list.add_last(2)
    assert dl_list.remove_last() == 2
    assert dl_list.remove_last() == 1


def test_size():
    dl_list = DLList(1)
    dl_list.add_first(2)
    dl_list.add_first(3)
    assert dl_list.size() == 3
