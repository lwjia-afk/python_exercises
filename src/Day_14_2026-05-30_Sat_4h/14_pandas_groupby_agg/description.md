# Pandas — GroupBy 与聚合 (GroupBy & Aggregation)

- **Difficulty**: Medium
- **Time budget**: ~30 min

## Objective
掌握 groupby 的核心用法：`agg`, `transform`, `filter`, `apply`，这是面试最高频考点之一。

## Tasks

### Task 1 — 基础聚合
- 按 `department` 分组，计算每组的 salary 均值、最大值、人数
- `agg` 传入字典 vs 传入列表的区别
- `named aggregation`：`agg(avg_salary=('salary','mean'), count=('name','count'))`

### Task 2 — 多列分组 + 多种聚合
- 按 `department` 和 `level` 双维度分组
- 同时对 salary 求均值，对 bonus 求总和，对 name 计数
- 用 `reset_index()` 把多级索引打平

### Task 3 — transform（保持原索引）
- 计算每个员工的薪资**占本部门总薪资的比例**
- 计算每个员工薪资与**本部门平均薪资的差值**
- 关键：`transform` 返回与原 DataFrame 等长的 Series，方便新增列

### Task 4 — filter（按组条件过滤行）
- 保留平均薪资 > 75000 的部门的所有员工行
- 保留员工人数 >= 3 的部门
- 注意：`filter` 保留的是整组，不是单行

### Task 5 — apply（最灵活）
- 对每个部门的 DataFrame 进行自定义操作：返回薪资最高和最低员工的信息
- 用 `apply` 计算每组的薪资分位数（25%, 50%, 75%）
- 了解 `apply` 比 `transform`/`agg` 慢的原因

## Self-check
- `agg` vs `transform` vs `apply` 的核心区别是什么？
- `groupby` 后直接访问列 `df.groupby('dept')['salary']` 是什么类型？
- 如何对分组结果排序（每组内排序 vs 按组间统计量排序）？
