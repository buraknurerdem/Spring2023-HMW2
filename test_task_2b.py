import HW2_tasks

def test_2b_1():
    assert HW2_tasks.task_2b([[1,2,3,9]], 2) == True

def test_2b_2():
    assert HW2_tasks.task_2b([[1,2,2,3]], 2) == True

def test_2b_3():
    assert HW2_tasks.task_2b([[1,2,3,11]], 4) == False

def test_2b_4():
    assert HW2_tasks.task_2b([[9],[1,2,3],[5]], 5) == True

def test_2b_5():
    assert HW2_tasks.task_2b([[],[]], 5) == False