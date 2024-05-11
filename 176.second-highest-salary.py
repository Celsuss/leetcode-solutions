"""
Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
The result format is in the following example.

Example 1:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """Calculate second highest salary."""
    if len(employee) <= 1:
        return pd.DataFrame([None], columns=['SecondHighestSalary'])
    res_data = None

    while res_data is None and employee.shape[0] > 1:
        max_value = employee['salary'].max()
        max_value_idx = employee['salary'].idxmax()
        employee = employee.drop(max_value_idx)

        res_data = employee['salary'].max()
        if res_data == max_value:
            res_data = None

    res = pd.DataFrame([res_data], columns=['SecondHighestSalary'])
    return res


def main():
    """Perform tests."""
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype(
        {'id': 'int64', 'salary': 'int64'})
    expected_data = [200]
    res_expected = pd.DataFrame(expected_data, columns=['SecondHighestSalary'])
    res = second_highest_salary(employee)
    assert res.equals(res_expected)

    data = [[1, 100]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype(
        {'id': 'int64', 'salary': 'int64'})
    expected_data = [None]
    res_expected = pd.DataFrame(expected_data, columns=['SecondHighestSalary'])
    res = second_highest_salary(employee)
    assert res.equals(res_expected)

    data = [[1, 100], [2, 100]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype(
        {'id': 'int64', 'salary': 'int64'})
    expected_data = [None]
    res_expected = pd.DataFrame(expected_data, columns=['SecondHighestSalary'])
    res = second_highest_salary(employee)
    assert res.equals(res_expected)

    data = [[1, 100], [2, 100], [3, 50]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype(
        {'id': 'int64', 'salary': 'int64'})
    expected_data = [50]
    res_expected = pd.DataFrame(expected_data, columns=['SecondHighestSalary'])
    res = second_highest_salary(employee)
    assert res.equals(res_expected)

    print('Success')


if __name__ == '__main__':
    main()
