# Pandas — 数据清洗 (Data Cleaning)

- **Difficulty**: Easy–Medium
- **Time budget**: ~25 min

## Objective
处理真实数据中最常见的脏数据问题：重复行、错误数据类型、格式不统一。

## Tasks

### Task 1 — 重复行
- 检测重复行（`duplicated`），找出所有重复行
- 理解 `keep='first'`, `keep='last'`, `keep=False` 的区别
- 基于**部分列**（`subset`）去重
- 删除重复行后重置索引

### Task 2 — 数据类型转换
给定包含脏数据的 DataFrame：
- `age` 列是字符串 `"25"`, `"30"`, `"unknown"` → 转成 int，`"unknown"` 变 NaN
- `price` 列含有 `"$100.5"`, `"$200"` → 去掉 `$` 后转 float
- `is_active` 列含有 `"True"`, `"False"`, `"yes"`, `"no"` → 统一映射为 bool
- `date` 列含有 `"2024-01-15"`, `"15/01/2024"` 混合格式 → 转 datetime

### Task 3 — 字符串规范化
- `category` 列含有 `"  Electronics "`, `"electronics"`, `"ELECTRONICS"` → 统一为 `"Electronics"`
- 找出并删除 `email` 列中格式非法的行（不含 `@` 的）
- `phone` 列含有 `"138-1234-5678"`, `"13812345678"`, `"(138)12345678"` → 统一格式为 `"138-1234-5678"`

### Task 4 — 列名清洗
- 列名含有空格、大写、特殊字符 → 统一为 snake_case 小写
- 例：`"First Name"` → `"first_name"`, `"Age (years)"` → `"age_years"`

## Self-check
- `pd.to_numeric(errors='coerce')` 和 `errors='raise'`, `errors='ignore'` 有什么区别？
- 为什么 `astype(int)` 在有 NaN 时会报错？如何解决？（提示：`Int64` nullable integer）
- `inplace=True` 有哪些潜在风险？现在 pandas 推荐用什么替代？
