-- 测试 CICD 流水线 - SQL 查询任务
-- 验证数据完整性

SELECT COUNT(*) AS total_records FROM transformed_data;

SELECT * FROM transformed_data LIMIT 10;
