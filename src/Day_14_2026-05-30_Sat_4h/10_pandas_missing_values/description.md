# Pandas — 缺失值处理 (Missing Values)

- **Difficulty**: Easy–Medium
- **Time budget**: ~25 min

## Objective
掌握检测、删除、填充缺失值的全套方法，这是数据清洗最高频的操作。

## 背景数据
一份销售记录，包含 `order_id`, `product`, `quantity`, `price`, `discount`, `region`，
其中多列含有 NaN。

## Tasks

### Task 1 — 检测缺失值
- 用一行代码得到每列缺失值的**数量**和**百分比**
- 找出**任意列有缺失**的所有行（`any`）
- 找出**所有列都缺失**的行（`all`）

### Task 2 — 删除缺失值
- 删除缺失值超过 **50%** 的列
- 删除**任意关键列**（`product`, `quantity`）有缺失的行
- `dropna` 的 `thresh` 参数有什么用？写一个例子。

### Task 3 — 填充缺失值
- `discount` 列：用 **0** 填充（业务含义：无折扣）
- `price` 列：用该列**中位数**填充
- `quantity` 列：用**前向填充**（`ffill`），再用**后向填充**（`bfill`）处理首行
- `region` 列：用**众数**填充

### Task 4 — 插值
- 创建一个时间序列 DataFrame（日期为索引，某传感器读数含缺失）
- 分别用 `method='linear'` 和 `method='time'` 插值，对比结果差异

## Self-check
- `fillna(method='ffill')` 和 `ffill()` 有什么区别？（版本差异）
- 为什么不应该用均值填充分类变量？
- `interpolate` 与 `fillna` 的根本区别是什么？
