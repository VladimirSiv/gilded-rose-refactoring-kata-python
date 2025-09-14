# Gilded Rose Refactoring Kata in Python

This repository contains an example solution to the
[Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main)
exercise.

There are many ways and possible approaches to deal with conditional complexity, which is the
main focus of this refactoring exercise.

In this example solution, I've implemented
[Strategy Pattern](https://refactoring.guru/design-patterns/strategy) which is quite useful and
commonly used design pattern for refactoring code, specifically code with conditional complexity.

The `Conjured` item logic is handled with a decorator class that adapts the strategy of
any item, whether it's the strategy of a specific item (like `Aged Brie`) or a random item with
the default strategy.

The solution also respects clean code and best practices by implementing:

- A clear folder structure
- Linters, static analyzers, annotations, docstrings, etc.
- Normalized input strings
- Validation
- Utility functions
- Exception hierarchy
- Error handling
- Mock and parametrized testing
- 100% test coverage
- Dependency manager
- Logging

Any feedback and recommendations for improvement are highly appreciated.
