import HW2_tasks

def test_1_1():
    assert HW2_tasks.task_1([[9,1,2,3]], 2) == True

def test_1_2():
    assert HW2_tasks.task_1([[9,2,2,3]], 2) == True

def test_1_3():
    assert HW2_tasks.task_1([[9,1,2,3]], 4) == False

def test_1_4():
    assert HW2_tasks.task_1([[9],[1,2,3],[5]], 5) == True

def test_1_5():
    assert HW2_tasks.task_1([[],[]], 5) == False