# Pandas — 日期时间处理 (DateTime)

- **Difficulty**: Medium
- **Time budget**: ~25 min

## Objective
掌握 pandas 中 datetime 的解析、提取、运算、重采样，时间序列在 DS 工作中极其常见。

## Tasks

### Task 1 — 解析日期
- `pd.to_datetime` 解析多种格式
- `format` 参数加速解析（`"%Y-%m-%d"`）
- `errors='coerce'` 处理无法解析的值
- 将字符串列转为 datetime 后，原 dtype 会变成什么？

### Task 2 — 提取日期属性（dt accessor）
给定一列 datetime，提取：
- `year`, `month`, `day`, `weekday`（0=Monday）
- `hour`, `minute`（如果有时间）
- `quarter`（季度）
- `is_month_end`（是否月末）

### Task 3 — 日期运算
- 两个日期列相减得到 Timedelta
- 从 Timedelta 提取**天数**（`.dt.days`）
- 用 `pd.DateOffset` 给日期加 30 天、加 1 个月
- 用 `pd.Timestamp` 创建单个时间点

### Task 4 — 重采样（resample）
给定每日销售时间序列：
- 按周（`W`）求和
- 按月（`ME`）求均值
- 按季度（`QE`）求最大值
- `resample` 和 `groupby(pd.Grouper(freq='M'))` 的等价写法

### Task 5 — 时间窗口
- `rolling(7).mean()`：7 日移动平均
- `expanding().sum()`：累计求和
- `shift(1)`：滞后一期（昨日数据）
- 用移动平均平滑噪声

## Self-check
- `datetime64[ns]` 和 Python 的 `datetime.datetime` 有什么关系？
- 为什么时区处理要特别小心？`tz_localize` vs `tz_convert` 的区别？
- `resample` 需要 DatetimeIndex，如果 datetime 列不是 index 怎么办？
