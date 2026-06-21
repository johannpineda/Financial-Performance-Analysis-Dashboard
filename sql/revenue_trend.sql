SELECT
    Month,
    SUM(Revenue) AS TotalRevenue
FROM financial_data
GROUP BY Month
ORDER BY Month;