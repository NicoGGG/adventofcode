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

  defp rotate90({a, b}), do: {-b, a}

  def move_next_step(grid, {current_x, current_y}, size, traveled_locations, {dir_x, dir_y}) do
    next_coord = {current_x + dir_x, current_y + dir_y}

    cond do
      blocked?(grid, next_coord) ->
        {new_dir_x, new_dir_y} = rotate90({dir_x, dir_y})

        move_next_step(
          grid,
          {current_x, current_y},
          size,
          traveled_locations,
          {new_dir_x, new_dir_y}
        )

      out_of_bound?(next_coord, size) ->
        MapSet.put(traveled_locations, {current_x, current_y})

      true ->
        move_next_step(
          grid,
          next_coord,
          size,
          MapSet.put(traveled_locations, {current_x, current_y}),
          {dir_x, dir_y}
        )
    end
  end

  defp out_of_bound?({x, y}, size) do
    if x < 0 || y < 0 || x >= size || y >= size do
      true
    else
      false
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

guard_path =
  Day06.move_next_step(input, guard_location, size, MapSet.new(), {0, -1})

result =
  Enum.count(guard_path)

IO.inspect(result, label: "part1")

# NOTE: About part 1, there could be an optimization (or at least simplification) by changing the input from a grid (list of list), into a map
# The key could be the coord as a tuple (if possible in elixir ?) and the value the character.
# This would avoid doing Enum.at(Enum.at(grid, y), x), which is not very pretty
# There is a good chance that this is actually almost required to solve part 2 so we'll see

# NOTE: Part 2 - For each position in the returned set, I can build a new grid with this position replaced by a # (except the first one)
# Then make the guard patrol the new grid and checking if he is in a loop (two cursor method ?)
