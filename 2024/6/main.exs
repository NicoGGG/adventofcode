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

  defp rotate90({x, y}), do: {-y, x}

  # def move_next_step(nil, {current_x, current_y}, size, traveled_locations, {dir_x, dir_y}),
  #   do: MapSet.put(traveled_locations, {current_x, current_y})

  def move_next_step(grid, {current_x, current_y}, traveled_locations, {dir_x, dir_y}) do
    next_coord = {current_x + dir_x, current_y + dir_y}

    cond do
      Map.get(grid, next_coord) === ?# ->
        new_dir = rotate90({dir_x, dir_y})

        move_next_step(
          grid,
          {current_x, current_y},
          traveled_locations,
          new_dir
        )

      Map.get(grid, {current_x, current_y}) === nil ->
        traveled_locations

      true ->
        move_next_step(
          grid,
          next_coord,
          MapSet.put(traveled_locations, {current_x, current_y}),
          {dir_x, dir_y}
        )
    end
  end
end

input =
  File.read!("file.txt")
  |> String.split("\n", trim: true)
  |> Enum.map(&String.to_charlist/1)
  |> Enum.with_index()
  |> Enum.flat_map(fn {line, row} ->
    Enum.with_index(line) |> Enum.flat_map(fn {char, col} -> [{{col, row}, char}] end)
  end)
  |> Map.new()

{guard_location, _} = Enum.find(input, fn {_, char} -> char === ?^ end)

guard_path =
  Day06.move_next_step(input, guard_location, MapSet.new(), {0, -1})

result =
  Enum.count(guard_path)

IO.inspect(result, label: "part1")

# NOTE: About part 1, there could be an optimization (or at least simplification) by changing the input from a grid (list of list), into a map
# The key could be the coord as a tuple (if possible in elixir ?) and the value the character.
# This would avoid doing Enum.at(Enum.at(grid, y), x), which is not very pretty
# There is a good chance that this is actually almost required to solve part 2 so we'll see

# NOTE: Part 2 - For each position in the returned set, I can build a new grid with this position replaced by a # (except the first one)
# Then make the guard patrol the new grid and checking if he is in a loop (two cursor method ?)
