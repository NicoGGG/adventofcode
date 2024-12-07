defmodule XmasMatch do
  @doc """
  Only takes a 3x3 grid of strings and return true if it's a X-MAS according to the puzzle instruction
  """
  @spec is_cross_mas([String.t()]) :: boolean()
  def is_cross_mas(grid) do
    diagonals = get_diagonals(grid)
    mas = ~r/MAS/
    sam = ~r/SAM/

    combinations =
      for i <- [mas, sam] do
        [diagonals, i]
      end

    count =
      Enum.map(combinations, fn [i, r] -> count_xmas(i, r) end)
      |> Enum.sum()

    if count == 2 do
      true
    else
      false
    end
  end

  @doc """
  Counts all matches of the regex in an array of string
  Used to count all XMAS and SAMX in the puzzle input grid
  """
  @spec count_xmas([String.t()], Regex.t()) :: integer
  def count_xmas(lines, regex) do
    Enum.flat_map(lines, fn line -> Regex.scan(regex, line) end)
    |> Enum.count()
  end

  @doc """
  Returns all possible diagonals in a AxA grid
  """
  @spec get_diagonals([String.t()]) :: [String.t()]
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

  @doc """
  Returns all possible 3x3 grids in a AxA grid
  The first array needs to be flatten afterward for simpler usage
  """
  @spec get_3_3_grids([String.t()]) :: [[[String.t()]]]
  def get_3_3_grids(grid) do
    rows = Enum.map(grid, &String.graphemes/1)
    size = length(rows)

    for y <- 0..(size - 3) do
      Enum.map(0..(size - 3), fn x ->
        for current_y <- y..(y + 2) do
          Enum.map(x..(x + 2), fn current_x ->
            Enum.at(Enum.at(rows, current_y), current_x)
          end)
          |> Enum.join()
        end
      end)
    end
  end
end

# Script start

lines =
  File.read!("file.txt")
  |> String.split("\n", trim: true)

## Part 1
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

result_part1 =
  Enum.map(combinations, fn {i, r} -> XmasMatch.count_xmas(i, r) end)
  |> Enum.sum()

IO.inspect(result_part1)

## Part 2
# For part 2, I should probably split the total grid into 3x3 grids and then check if the diagonals have 2 MAS/SAM total
# Count 1 if true and sum up all 3x3 grids results

grids_3_3 =
  XmasMatch.get_3_3_grids(lines)
  |> Enum.flat_map(fn inner_list -> inner_list end)

result_part2 =
  Enum.map(grids_3_3, fn grid -> XmasMatch.is_cross_mas(grid) end)
  |> Enum.filter(fn x -> x end)
  |> Enum.count()

IO.inspect(result_part2)

# NOTE: This is all very slow and bruteforcish but as a first time elixir user I am not going to optimize it further for now
# A probably better way to solve part 2 would be to iterate thru all chars and check if the surrounding diagonals form a X-MAS when finding a "A" character
# Same idea probably with part 1 and checking all surrounding combinations of XMAS when finding a "X" character
