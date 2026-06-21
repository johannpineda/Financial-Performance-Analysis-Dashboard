SELECT
    Department,
    SUM(Revenue) AS Revenue,
    SUM(Expenses) AS Expenses,
    SUM(Profit) AS Profit
FROM financial_data
GROUP BY Department;