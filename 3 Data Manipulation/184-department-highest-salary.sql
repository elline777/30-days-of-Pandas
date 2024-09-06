SELECT
    Employee.name AS Employee,
    Employee.salary AS Salary,
    Department.name AS Department
FROM Employee
JOIN Department
ON Employee.departmentId = Department.id
WHERE
    (Employee.departmentId, Salary) IN (
        SELECT
            departmentId,
            MAX(salary)
        FROM Employee
        GROUP BY departmentId
    );