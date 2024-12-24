defmodule Day10 do
  def find_nine(grid, {x, y}, current_val) do
    directions = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

    Enum.map(directions, fn {dirx, diry} ->
      next_x = x + dirx
      next_y = y + diry
      next_value = Map.get(grid, {next_x, next_y})

      cond do
        next_value == 57 && next_value == current_val + 1 ->
          {next_x, next_y}

        next_value == current_val + 1 ->
          find_nine(grid, {x + dirx, y + diry}, next_value)

        true ->
          nil
      end
    end)
    |> Enum.filter(fn a -> a end)
  end
end

# map of all characters by coordinate {col, row} (x, y)
grid =
  File.read!("file.txt")
  |> String.split("\n", trim: true)
  |> Enum.map(&String.to_charlist/1)
  |> Enum.with_index()
  |> Enum.flat_map(fn {line, row} ->
    Enum.with_index(line) |> Enum.flat_map(fn {char, col} -> [{{col, row}, char}] end)
  end)
  |> Map.new()

all_zeros = Map.filter(grid, fn {_key, val} -> val == 48 end)

## Part 1
result =
  Enum.map(all_zeros, fn {key, val} -> Day10.find_nine(grid, key, val) end)
  |> Enum.map(&List.flatten/1)
  |> Enum.map(&MapSet.new/1)
  |> Enum.map(&MapSet.size/1)
  |> Enum.sum()

IO.inspect(result)

## Part 2
result =
  Enum.map(all_zeros, fn {key, val} -> Day10.find_nine(grid, key, val) end)
  |> Enum.map(&List.flatten/1)
  |> Enum.map(&Enum.count/1)
  |> Enum.sum()

IO.inspect(result)
