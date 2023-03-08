# Homework 2
### Due Date: 14.03.2023 23:59

* **Case 1:** You are given a list of lists of integers which are not particularly sorted in any way.
    * **Task 1:** Find out if a certain integer exists in the list or not.
* **Case 2:** You are given a list of list of integers. Additionally, you know that in the nested lists, the integer values are sorted ascending. Again, you want to find out if a certain integer exists in the list or not.
    * **Task 2a:** Implement using iterative search.
    * **Task 2b:** Implement using binary search in the nested lists.
* **Case 3:** You are given a list of list of integers. This time, not only the integers in the nested lists are sorted, but also, you know that the lists are ordered among themselves. One example of such input is as follows. 

        [[1,3,4],[7,9],[12,15,29,201]]

    * **Task 3a:** Implement binary search among the nested lists and inside the nested lists.
    * **Task 3b:** Flatten the list. Implement binary search.

* **Case 4**: As a last task, you are given a set of integers. 
    * **Task 4:** Find out if a certain integer exists in the set or not.


You are expected to test the performances of the code you wrote for each task. Note that in each task, your functions should return a boolean value.

Perform the test for `n` = [10, 100, 1000, 10000]

For each `n` value, generate 10 random instances and take the average runtime among 10 instances. For each instance, you need to generate the necessary input. The outward list (or set) should have size `n` as well as the nested structures. integers should be selected randomly in the interval of *[0*, *1000 * n]*. The target to search for should also be a random integer in the interval. Make sure you handle the conditions on sortedness as explained above before giving the generated data as inputs.

As an output, prepare a table in markdown notation. The columns of the table should be the different sizes of `n`, the rows should indicate the task. In the entries of the table report the average run time per 10 runs in seconds. You might create the table using strings or you might utilize the `pandas` dataframe library. Just make sure the output you provide is in markdown notation.

You should write the search functions in HW2_tasks.py. If you change function names, parameter positions, the tests may not work. Then input generation, performance runs, generating the table in markdown format should be done in HW2_perform.py file. Lastly, write a very brief report about the performances of search methods in a markdown file. Add your generated table of runtimes to the report.