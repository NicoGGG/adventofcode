defmodule Day06 do
  @doc """
  Return the {x, y} of the guard, x being the column, and y the row
  """
  def find_guard(grid) do
    Enum.reduce_while(grid, {0, 0}, fn line, coord ->
      guard_x = Enum.find_index(line, fn point -> point === ?^ end)

      if guard_x === nil do
        {x, y} = coord
        {:cont, {x, y + 1}}
      else
        {_, y} = coord
        {:halt, {guard_x, y}}
      end
    end)
  end

  def move_guard_north(_grid, {x, 0}, _size, traveled_locations),
    do: MapSet.put(traveled_locations, {x, 0})

  def move_guard_north(grid, {x, y}, size, traveled_locations) do
    if blocked?(grid, {x, y - 1}) do
      move_guard_east(grid, {x, y}, size, traveled_locations)
    else
      move_guard_north(grid, {x, y - 1}, size, MapSet.put(traveled_locations, {x, y}))
    end
  end

  defp move_guard_east(_grid, {x, y}, size, traveled_locations) when x >= size,
    do: MapSet.put(traveled_locations, {x, y})

  defp move_guard_east(grid, {x, y}, size, traveled_locations) do
    if blocked?(grid, {x + 1, y}) do
      move_guard_south(grid, {x, y}, size, traveled_locations)
    else
      move_guard_east(grid, {x + 1, y}, size, MapSet.put(traveled_locations, {x, y}))
    end
  end

  defp move_guard_south(_grid, {x, y}, size, traveled_locations) when y >= size,
    do: MapSet.put(traveled_locations, {x, y})

  defp move_guard_south(grid, {x, y}, size, traveled_locations) do
    if blocked?(grid, {x, y + 1}) do
      move_guard_west(grid, {x, y}, size, traveled_locations)
    else
      move_guard_south(grid, {x, y + 1}, size, MapSet.put(traveled_locations, {x, y}))
    end
  end

  defp move_guard_west(_grid, {0, y}, _size, traveled_locations),
    do: MapSet.put(traveled_locations, {0, y})

  defp move_guard_west(grid, {x, y}, size, traveled_locations) do
    if blocked?(grid, {x - 1, y}) do
      move_guard_north(grid, {x, y}, size, traveled_locations)
    else
      move_guard_west(grid, {x - 1, y}, size, MapSet.put(traveled_locations, {x, y}))
    end
  end

  defp blocked?(grid, {x, y}) do
    case Enum.at(grid, y) do
      nil -> false
      row -> Enum.at(row, x) === ?#
    end
  end
end

input =
  File.read!("file.txt")
  |> String.split("\n", trim: true)
  |> Enum.map(&String.to_charlist/1)

guard_location = Day06.find_guard(input)

size = length(input)

result =
  Day06.move_guard_north(input, guard_location, size, MapSet.new())
  |> Enum.count()

IO.inspect(result, label: "part1")

# NOTE: About part 1, there could be an optimization (or at least simplification) by changing the input from a grid (list of list), into a map
# The key could be the coord as a tuple (if possible in elixir ?) and the value the character.
# This would avoid doing Enum.at(Enum.at(grid, y), x), which is not very pretty
# There is a good chance that this is actually almost required to solve part 2 so we'll see
