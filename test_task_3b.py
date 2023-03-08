import HW2_tasks

def test_3b_1():
    assert HW2_tasks.task_3b([[1,2,3,9],[11,13,17,21],[999,1000]], 1000) == True

def test_3b_2():
    assert HW2_tasks.task_3b([[1,2,2,3]], 2) == True

def test_3b_3():
    assert HW2_tasks.task_3b([[1,2,3,9],[11,13,17,21],[999,1000]], 4) == False

def test_3b_4():
    assert HW2_tasks.task_3b([[],[1,2,3],[5]], 0) == False

def test_3b_5():
    assert HW2_tasks.task_3b([[],[]], 5) == False