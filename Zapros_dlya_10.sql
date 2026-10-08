DELETE FROM rosstat_salary_ru
WHERE region_name IN ('Рязанская область', 'Свердловская область', 'Чеченская республика', 'Ростовская область')
SELECT * FROM rosstat_salary_ru
ORDER BY salary ASC
SELECT ROUND(AVG(salary),2) AS Srednee FROM rosstat_salary_ru 
SELECT DISTINCT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) OVER() AS Median FROM rosstat_salary_ru