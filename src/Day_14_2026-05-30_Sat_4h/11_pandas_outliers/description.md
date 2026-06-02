# Pandas — 异常值检测与处理 (Outliers)

- **Difficulty**: Medium
- **Time budget**: ~25 min

## Objective
掌握用 IQR 和 Z-score 两种方法检测异常值，并学会不同的处理策略。

## 背景数据
一份用户消费记录，包含 `user_id`, `age`, `purchase_amount`, `session_duration`。

## Tasks

### Task 1 — IQR 方法
- 计算 `purchase_amount` 的 Q1、Q3、IQR
- 定义上下界：`[Q1 - 1.5*IQR, Q3 + 1.5*IQR]`
- 返回所有异常值行
- 封装成通用函数 `detect_outliers_iqr(df, col)`

### Task 2 — Z-score 方法
- 对 `purchase_amount` 计算 Z-score（手动实现：`(x - mean) / std`）
- 也用 `scipy.stats.zscore` 实现一遍
- 找出 `|z| > 3` 的行
- 封装成 `detect_outliers_zscore(df, col, threshold=3)`

### Task 3 — 处理策略
实现以下三种处理方式，各有适用场景：
1. **删除**：直接 drop 异常行
2. **截断 (Winsorize/Clip)**：超出上下界的值替换为边界值
3. **替换为 NaN**：用 `np.nan` 替换，后续再填充

### Task 4 — 多列批量检测
- 对所有数值列批量运行 IQR 检测
- 返回一个 dict：`{col: outlier_indices}`

## Self-check
- IQR 和 Z-score 分别适用于什么分布的数据？
- `df.clip(lower, upper)` 和手动 replace 有什么区别？
- 为什么先检测异常值，再做缺失值填充？
