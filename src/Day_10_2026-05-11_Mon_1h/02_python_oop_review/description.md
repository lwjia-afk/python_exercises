# Python OOP concepts review

- **Time budget**: ~20 min

## Objective
Map your .NET OOP knowledge to Python idioms. Topics likely to come up:
- `__init__`, `self`
- inheritance, `super().__init__(...)`
- `@property`, `@staticmethod`, `@classmethod`
- `__repr__` vs `__str__`
- duck typing vs nominal types
- dataclasses (`@dataclass`)

## Task
In `practice.py`:

1. Define `Animal` with `name`, `sound()`. Subclass `Dog`, `Cat` overriding `sound`.
2. Add a `@property` `description` returning `f"{self.name} says {self.sound()}"`.
3. Add a `@classmethod` `from_dict(cls, d)` building an Animal from `{"name": ...}`.
4. Convert `Animal` to a `@dataclass` and note what code disappeared.
5. Show duck typing: a function `make_noise(thing)` that calls `thing.sound()` regardless of type.

## Expected output
All five examples run.

## Self-check
- How is `@property` different from a public field in C#?
- Python has no `interface` keyword — what's the closest equivalent? (Hint: `abc.ABC`, `Protocol`.)
