# [Wait For It](https://adventofcode.com/2023/day/6)

Current solution is O(n) in time.
There is certainly a faster way by traversing the time list simultaneously from both ends, and return the difference between start index and end index (where start and end index are the first time that a winning prep time is found).

This is because the winning combinations are always a range. We either don't push long enough, or we push too long, but there is no reason that 13 millisecond would be winning, 14 would _not_, and 15 would be winning again.

After implementing it, partial traversal is about 30% faster than full traversal for my input, but it's still O(n) in time.
