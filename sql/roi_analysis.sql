SELECT
    Department,
    AVG(ROI) AS AverageROI
FROM financial_data
GROUP BY Department
ORDER BY AverageROI DESC;