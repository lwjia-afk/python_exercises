# Pandas — 合并与连接 (Merge & Join)

- **Difficulty**: Medium
- **Time budget**: ~25 min

## Objective
掌握 `merge`, `join`, `concat` 的各种用法，以及如何处理合并中的冲突和重复。

## Tasks

### Task 1 — merge 四种连接类型
给定 employees 表和 departments 表：
- `inner join`：只保留两表都有的 dept_id
- `left join`：保留所有员工（右表无匹配填 NaN）
- `right join`：保留所有部门（左表无匹配填 NaN）
- `outer join`：保留所有记录

可视化理解：画出每种 join 保留哪些行。

### Task 2 — 多键 merge + 冲突列处理
- 用 `on=['dept_id', 'year']` 多键合并
- 当两表有同名列（非 key）时，pandas 自动加 `_x`, `_y` 后缀
- 用 `suffixes=('_emp', '_dept')` 自定义后缀
- 合并后删除不需要的列

### Task 3 — concat（纵向拼接）
- `pd.concat([df1, df2])` 纵向拼接，处理索引重置
- `ignore_index=True` vs 保留原索引
- `keys=['Q1', 'Q2']` 创建多级索引
- 横向 concat（`axis=1`）vs merge 的区别

### Task 4 — 合并验证（validate 参数）
- `validate='one_to_one'`：确保 key 在两表中都唯一
- `validate='many_to_one'`：左表可以有重复 key
- 当验证失败时如何 debug

### Task 5 — 实战：多表关联
给定 orders, products, customers 三表，用 merge 链式关联，
得到每笔订单的 customer_name, product_name, total_amount。

## Self-check
- `merge` 和 `join` 的区别？（join 基于 index，merge 基于列）
- left join 后如何找出右表中没有匹配的左表行？（提示：`indicator=True`）
- `pd.concat` 的 `sort=True` 参数有什么用？
