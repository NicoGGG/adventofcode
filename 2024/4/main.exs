defmodule XmasMatch do
  def count_xmas(lines, regex) do
    Enum.flat_map(lines, fn line -> Regex.scan(regex, line) end)
    |> Enum.count()
  end

  def get_diagonals(grid) do
    rows = Enum.map(grid, &String.graphemes/1)
    size = length(rows)

    top_left_to_bottom_right =
      for offset <- (-size + 1)..(size - 1) do
        Enum.map(0..(size - 1), fn row_index ->
          col_index = row_index + offset
          if col_index in 0..(size - 1), do: Enum.at(rows, row_index) |> Enum.at(col_index)
        end)
        |> Enum.reject(&is_nil/1)
      end

    top_right_to_bottom_left =
      for offset <- (-size + 1)..(size - 1) do
        Enum.map(0..(size - 1), fn row_index ->
          col_index = size - 1 - row_index + offset
          if col_index in 0..(size - 1), do: Enum.at(rows, row_index) |> Enum.at(col_index)
        end)
        |> Enum.reject(&is_nil/1)
      end

    Enum.map(top_left_to_bottom_right ++ top_right_to_bottom_left, fn line -> Enum.join(line) end)

    # NOTE: this is pretty convoluted but I couldn't find a nice idiomatic way to make the diagonals from the lines
  end
end

lines =
  File.read!("file.txt")
  |> String.split("\n", trim: true)

columns =
  lines
  |> Enum.map(&String.to_charlist/1)
  |> Enum.zip()
  |> Enum.map(fn inner_charlist -> List.to_string(Tuple.to_list(inner_charlist)) end)

diagonals = XmasMatch.get_diagonals(lines)

xmas = ~r/XMAS/
samx = ~r/SAMX/

inputs = [lines, columns, diagonals]
regexes = [xmas, samx]

combinations = for i <- inputs, r <- regexes, do: {i, r}

result =
  Enum.map(combinations, fn {i, r} -> XmasMatch.count_xmas(i, r) end)
  |> Enum.sum()

IO.inspect(result)
