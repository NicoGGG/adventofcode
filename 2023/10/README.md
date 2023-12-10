# [Day 10: Pipe Maze](https://adventofcode.com/2023/day/10)

Got stuck on part 2.

According to a reddit comment:

> Part 2: a cell is inside the loop if, when I look all cells in one direction (let's say "north"), there are an odd number of perpendicular pipes.
> I loop on every cell and count when it's inside with this property.

The statement is not totally understandable, but after some digging around, I found the Odd-Even Rule:

Take an arbitrary direction, and count the number of crossings in the perpendicular direction. The trick is that crossing of JLF7 pipes are not counted as a crossing if the exit is in the same direction as it entered. For example. if the direction is North, and the pipe is J, then the crossing is not counted if the exit pipe is 7, because it entered from the west and exited to the west.

The way to do that was to keep a counter of west (-J7) and east (-FL), and take the min of the two. If that minimum is odd, then the cell is inside the loop.
