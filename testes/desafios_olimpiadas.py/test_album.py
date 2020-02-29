from album import fig_rest

def test_1():
    assert fig_rest(10, 2, 5, [4,7], [7, 1, 2, 8, 3]) == 1

def test_2():
    assert fig_rest(10, 2, 6, [4,7], [7, 1, 8, 4, 9, 3]) == 0

def test_3():
    assert fig_rest(8, 4, 10, [2,4,6,8], [3,1,1,5,3,1,7,7,1,1]) == 4