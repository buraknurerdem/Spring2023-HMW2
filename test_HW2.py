import HW2_tasks

## task_1
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

## task_2a
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

## task_2b
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

## task_3a
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

## task_3b
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

## task_4
def test_4_1():
    assert HW2_tasks.task_4({1,2,3}, 3) == True

def test_4_2():
    assert HW2_tasks.task_4({1,2,3}, 4) == False

def test_4_3():
    assert HW2_tasks.task_4({1}, 1) == True
