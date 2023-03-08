import HW2_tasks

def test_2a_1():
    assert HW2_tasks.task_2a([[1,2,3,9]], 2) == True

def test_2a_2():
    assert HW2_tasks.task_2a([[1,2,2,3]], 2) == True

def test_2a_3():
    assert HW2_tasks.task_2a([[1,2,3,11]], 4) == False

def test_2a_4():
    assert HW2_tasks.task_2a([[9],[1,2,3],[5]], 5) == True

def test_2a_5():
    assert HW2_tasks.task_2a([[],[]], 5) == False