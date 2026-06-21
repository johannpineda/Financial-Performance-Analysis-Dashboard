SELECT
    Department,
    SUM(Profit) AS TotalProfit
FROM financial_data
GROUP BY Department
ORDER BY TotalProfit DESC;