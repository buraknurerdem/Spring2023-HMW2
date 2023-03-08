import HW2_tasks

def test_4_1():
    assert HW2_tasks.task_4({1,2,3}, 3) == True

def test_4_2():
    assert HW2_tasks.task_4({1,2,3}, 4) == False

def test_4_3():
    assert HW2_tasks.task_4({1}, 1) == True