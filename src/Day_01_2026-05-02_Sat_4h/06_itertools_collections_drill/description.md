# itertools & collections drill

- **Time budget**: ~45 min

## Objective
Get familiar with the standard-library tools that show up constantly.

## Task
In `practice.py`, demonstrate ONE example of each:

---

### 1. `collections.Counter` — Top 3 most common letters

给定一个句子，找出出现频率最高的前 3 个字母。

**Example:**

```
Input:  "hello world, it is a beautiful day"
Output: [('l', 4), ('i', 2), ('o', 2)]
         ^字母   ^出现次数
```

**Follow-up (interview):** 统计一个列表中最常见的元素 → `Counter(list).most_common(k)`

---

### 2. `collections.defaultdict(list)` — Group words by length

给定一组单词，按单词长度分组，返回一个字典。

**Example:**

```
Input:  ["cat", "dog", "elephant", "ox", "bee", "ant"]
Output: {
    2: ["ox"],
    3: ["cat", "dog", "bee", "ant"],
    8: ["elephant"]
}
```

**Follow-up (interview):** 字母异位词分组（Group Anagrams）→ `defaultdict(list)`，key 用 `sorted(word)`

---

### 3. `collections.deque` — Sliding-window queue

用 `appendleft` 和 `popleft` 模拟一个固定大小的滑动窗口队列（容量为 3）。

**Example:**

```
操作序列: appendleft(1), appendleft(2), appendleft(3), appendleft(4)

After appendleft(1): deque([1])
After appendleft(2): deque([2, 1])
After appendleft(3): deque([3, 2, 1])
After appendleft(4): deque([4, 3, 2])  ← 右端的 1 被弹出（maxlen=3）

popleft() → 返回 4，剩余: deque([3, 2])
```

**Follow-up (interview):** BFS 队列、滑动窗口最大值 → 用 `deque` 替代 `list` 以获得 O(1) 的两端操作

---

### 4. `itertools.combinations(nums, 2)` — All pairs

给定一个列表，生成所有长度为 2 的组合（不重复、不考虑顺序）。

**Example:**

```
Input:  nums = [1, 2, 3, 4]
Output: (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)

共 C(4,2) = 6 对
```

**Follow-up (interview):** 两数之和的所有候选对 → `combinations(nums, 2)`；三数之和 → `combinations(nums, 3)`

---

### 5. `itertools.permutations([1,2,3])` — All orderings

给定一个列表，生成所有排列（顺序不同视为不同结果）。

**Example:**

```
Input:  [1, 2, 3]
Output: (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)

共 3! = 6 种排列
```

**Follow-up (interview):** 全排列问题（LeetCode 46）→ 面试中通常要求手写回溯，但 `permutations` 可用于验证答案

---

### 6. `itertools.groupby` — Group words by length (without defaultdict)

先将单词按长度排序，再用 `groupby` 分组（注意：`groupby` 只对连续相同 key 的元素分组，所以必须先排序）。

**Example:**

```
Input:  ["cat", "elephant", "ox", "dog", "bee", "ant"]

先排序: ["ox", "cat", "dog", "bee", "ant", "elephant"]
         len=2   len=3  len=3  len=3  len=3   len=8

groupby 结果:
  key=2 → ["ox"]
  key=3 → ["cat", "dog", "bee", "ant"]
  key=8 → ["elephant"]
```

**Follow-up (interview):** 与 `defaultdict` 的区别 → `groupby` 是惰性迭代器，不构建完整字典，适合流式数据

---

### 7. `itertools.chain([1,2],[3,4])` — Flatten iterables

将多个可迭代对象拼接成一个连续的迭代器（浅层展平）。

**Example:**

```
Input:  [1, 2], [3, 4], [5, 6]
Output: 1, 2, 3, 4, 5, 6

等价于: list(chain([1,2], [3,4], [5,6])) → [1, 2, 3, 4, 5, 6]

chain.from_iterable([[1,2],[3,4],[5,6]]) → 同上，输入为嵌套列表
```

**Follow-up (interview):** 展平一层嵌套列表 → `list(chain.from_iterable(nested))`；比列表推导式更高效（无需构建中间列表）

---

## Self-check

**Q: `combinations` 和 `permutations` 的区别？**

| | combinations | permutations |
|---|---|---|
| 是否考虑顺序 | 否 | 是 |
| (1,2) 和 (2,1) | 同一个 | 两个不同结果 |
| 数量公式 | C(n,r) = n!/(r!(n-r)!) | P(n,r) = n!/(n-r)! |
| 典型场景 | 选牌、选组合 | 全排列、密码生成 |

**记忆口诀：** combination = 组合（选人不管站位），permutation = 排列（选人且看站位）
