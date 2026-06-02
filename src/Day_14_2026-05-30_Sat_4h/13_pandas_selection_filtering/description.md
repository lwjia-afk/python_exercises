# Pandas — 选择与过滤 (Selection & Filtering)

- **Difficulty**: Easy
- **Time budget**: ~20 min

## Objective
深度掌握 `loc` / `iloc` / 布尔索引 / `query`，以及 `where` / `mask` 的用法。

## Tasks

### Task 1 — loc vs iloc
- `loc`：基于**标签**选行列（可以是字符串索引）
- `iloc`：基于**整数位置**选行列
- 练习：选第 2~4 行、选 `name` 和 `salary` 列、同时选行列

### Task 2 — 布尔索引
- 单条件：`salary > 80000`
- 多条件：`salary > 80000 AND department == 'Engineering'`（`&` 运算符）
- OR 条件：`department == 'Engineering' OR department == 'Marketing'`
- `isin()` 的使用：等价于上面的 OR 条件，更简洁
- `~` 取反：不属于某个集合

### Task 3 — query 方法
- 用 `query` 重写 Task 2 的所有条件，对比语法差异
- `query` 中引用外部变量用 `@variable`
- `query` 的性能在大数据集上的优势（了解即可）

### Task 4 — where / mask
- `where(condition)`：条件为 False 的位置替换为 NaN（或指定值）
- `mask(condition)`：条件为 True 的位置替换为 NaN（where 的反义）
- 练习：将 salary 中低于 60000 的值替换为 60000（薪资底线）

### Task 5 — 复杂索引场景
- `between()`：选出 age 在 [25, 35] 之间的行
- `str.startswith()` / `str.contains()`：按字符串条件过滤
- `notna()` / `isna()`：过滤缺失值

## Self-check
- `df[df['a'] > 1]` 和 `df.query('a > 1')` 的语义完全等价吗？
- 为什么链式赋值 `df[df['x']>0]['y'] = 1` 不可靠？如何正确赋值？
- `loc` 的切片是**包含**右端点的，`iloc` 呢？
