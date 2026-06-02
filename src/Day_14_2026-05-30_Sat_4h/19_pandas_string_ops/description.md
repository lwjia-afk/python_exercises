# Pandas — 字符串操作 (String Operations)

- **Difficulty**: Easy–Medium
- **Time budget**: ~20 min

## Objective
掌握 pandas `str` accessor 的常用方法，处理文本数据是 DS 日常工作的核心技能。

## Tasks

### Task 1 — 基础 str 方法
给定产品名称列，练习：
- `str.upper()` / `str.lower()` / `str.title()`
- `str.strip()` / `str.lstrip()` / `str.rstrip()`
- `str.len()`：每个字符串的长度
- `str.replace('old', 'new')`：支持正则

### Task 2 — 切割与提取
- `str.split('_')` → 列表，再用 `str[0]` 取第一个元素
- `str.split('_', expand=True)` → 直接分成多列
- `str.extract(r'(\d+)')` → 用正则提取数字部分
- `str.extractall()` vs `str.extract()` 的区别

### Task 3 — 判断与过滤
- `str.contains('pattern')` → 布尔 Series，默认支持正则
- `str.startswith()` / `str.endswith()`
- `str.match(r'^[A-Z]')` → 正则全匹配（从头开始）
- `str.isnumeric()` / `str.isalpha()`

### Task 4 — 实战：解析日志行
给定一组日志字符串，格式为：
`"[2024-01-15 10:23:45] ERROR user_id=123 message=login_failed"`
提取：`timestamp`, `level`, `user_id`, `message`

### Task 5 — str 方法处理 NaN
- str accessor 自动跳过 NaN（返回 NaN）
- `str.contains('pattern', na=False)` 的重要性

## Self-check
- `str.replace` 默认用正则还是字面量？（pandas 2.x 有变化）
- `str.extract` 必须有**捕获组** `()`，否则报错
- 为什么对大量文本列用 `str` accessor 比 `apply(lambda)` 快？
