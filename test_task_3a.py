import HW2_tasks

def test_3a_1():
    assert HW2_tasks.task_3a([[1,2,3,9],[11,13,17,21],[999,1000]], 1000) == True

def test_3a_2():
    assert HW2_tasks.task_3a([[1,2,2,3]], 2) == True

def test_3a_3():
    assert HW2_tasks.task_3a([[1,2,3,9],[11,13,17,21],[999,1000]], 4) == False

def test_3a_4():
    assert HW2_tasks.task_3a([[],[1,2,3],[5]], 0) == False

def test_3a_5():
    assert HW2_tasks.task_3a([[],[]], 5) == False