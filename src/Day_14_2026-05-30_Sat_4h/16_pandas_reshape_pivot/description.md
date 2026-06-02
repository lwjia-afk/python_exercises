# Pandas — 数据重塑 (Reshape: Pivot & Melt)

- **Difficulty**: Medium–Hard
- **Time budget**: ~30 min

## Objective
掌握宽表↔长表的转换，`pivot_table`, `melt`, `stack/unstack`，这是 DS 面试必考项。

## 核心概念
- **宽表（Wide）**：每个变量是一列，每行是一个观测
- **长表（Long/Tidy）**：每行是一个变量的观测值，更适合 groupby 和可视化

## Tasks

### Task 1 — pivot_table
给定销售长表（date, product, region, amount）：
- 行=product，列=region，值=amount 总和
- `aggfunc` 参数：sum vs mean vs count
- `margins=True`：添加汇总行列（"All"）
- `fill_value=0`：填充 NaN

### Task 2 — melt（宽→长）
给定学生成绩宽表（student_id, math, english, science）：
- 用 `melt` 转成长表：(student_id, subject, score)
- `id_vars` 和 `value_vars` 参数
- `var_name` 和 `value_name` 重命名列

### Task 3 — stack / unstack
- `stack`：将列名"压入"行索引（宽→长）
- `unstack`：将行索引"展开"为列（长→宽）
- 多级索引的 stack/unstack（指定 level）
- 与 pivot/melt 的区别：stack/unstack 操作的是**索引**

### Task 4 — 综合练习
给定长表，完成以下转换链：
1. 长表 → pivot_table（宽表）
2. 宽表 → melt（长表）
3. 验证往返转换后数据是否一致（`sort_values` 后对比）

## Self-check
- `pivot` 和 `pivot_table` 的区别？（pivot 不支持聚合，有重复 key 会报错）
- `melt` 后为什么通常需要 `sort_values`？
- `stack(dropna=False)` 和 `stack(dropna=True)` 的区别？
