# Pandas — Apply / Map / Transform

- **Difficulty**: Medium
- **Time budget**: ~20 min

## Objective
掌握 `apply`, `map`, `applymap`/`map`(元素级) 的使用场景和性能取舍。

## 核心区分
| 方法 | 作用对象 | 返回 | 典型用途 |
|------|----------|------|----------|
| `Series.map` | 每个元素 | Series | 值映射/替换 |
| `Series.apply` | 每个元素（或复杂函数） | Series | 需要 if/else 逻辑 |
| `DataFrame.apply` | 每行/每列 | Series/DataFrame | 跨列计算 |
| `DataFrame.map` | 每个元素 | DataFrame | 格式化/批量替换 |

## Tasks

### Task 1 — Series.map（值映射）
- 将 `department` 列中的英文名映射为中文
- 用**字典**映射：`{'Engineering': '工程部', ...}`
- 用**函数**映射：等价实现
- 未匹配的值 map 后会变成什么？

### Task 2 — Series.apply（自定义逻辑）
- 根据 salary 判断薪资等级：`<60k='低', 60k-90k='中', >90k='高'`
- 等价方式：`pd.cut`（了解哪种更快）

### Task 3 — DataFrame.apply（跨列）
- 按行（axis=1）：计算每个员工的 "total compensation"（salary + bonus）
- 按列（axis=0）：计算每列的 min/max/range（自定义聚合函数）
- 何时用 `apply`，何时直接用向量化操作？

### Task 4 — DataFrame.map（元素级格式化）
- 将所有数值列格式化为带千位分隔符的字符串：`95000 → '95,000'`
- 将字符串列全部转大写

### Task 5 — 性能对比（思考题）
以下三种方式对 salary 列加 1000，哪种最快？
```python
df["salary"].apply(lambda x: x + 1000)   # apply
df["salary"].map(lambda x: x + 1000)     # map
df["salary"] + 1000                       # 向量化
```
写出结论（不需要 benchmark 代码）。

## Self-check
- `apply(func, axis=1)` 慢的原因是什么？什么时候不得不用？
- pandas 2.0 中 `applymap` 被重命名为什么？
- `map` 传字典和传函数的区别（NaN 处理方式不同）？
