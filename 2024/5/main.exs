defmodule Day05 do
  @spec is_valid_update(%{String.t() => [String.t()]}, [String.t()]) :: boolean()
  def is_valid_update(rules, update) do
    Enum.reduce_while(update, [], fn page, acc ->
      forbidden = Map.get(rules, page)

      cond do
        forbidden === nil ->
          {:cont, acc ++ [page]}

        Enum.any?(forbidden, fn x -> Enum.find(acc, fn y -> x == y end) end) ->
          {:halt, false}

        true ->
          {:cont, acc ++ [page]}
      end
    end)
  end

  @spec fix_invalid_update(%{String.t() => [String.t()]}, [String.t()]) :: [String.t()]
  def fix_invalid_update(rules, update) do
    Enum.reduce_while(update, [], fn page, acc ->
      forbidden = Map.get(rules, page)

      cond do
        forbidden === nil ->
          {:cont, acc ++ [page]}

        Enum.any?(forbidden, fn x -> Enum.find(acc, fn y -> x == y end) end) ->
          # All this is to find the actual forbidden value that came before current page
          # then swap them before recalling the function recursivly until the update is valid
          left_right =
            Enum.reduce_while(forbidden, {0, 0}, fn left, indexes ->
              left_index = Enum.find_index(acc, fn l -> l == left end)

              if left_index === nil do
                {:cont, indexes}
              else
                right_index = Enum.find_index(update, fn r -> r == page end)
                {:halt, {left_index, right_index}}
              end
            end)

          {left_index, right_index} = left_right

          {left, [el1 | rest1]} = Enum.split(update, left_index)
          {middle, [el2 | right]} = Enum.split(rest1, right_index - left_index - 1)

          swap_update = left ++ [el2] ++ middle ++ [el1] ++ right

          {:halt, Day05.fix_invalid_update(rules, swap_update)}

        true ->
          {:cont, acc ++ [page]}
      end
    end)
  end
end

lines =
  File.read!("file.txt")
  |> String.split("\n")

{rules, updates} = Enum.split_while(lines, fn s -> s !== "" end)

rules =
  Enum.map(rules, fn rule -> String.split(rule, "|") end)
  |> Enum.reduce(%{}, fn [x, y], acc ->
    Map.update(
      acc,
      x,
      [y],
      fn existing_value -> existing_value ++ [y] end
    )
  end)

updates =
  Enum.filter(updates, fn x -> x !== "" end)
  |> Enum.map(fn s -> String.split(s, ",") end)

valid_updates =
  Enum.map(updates, fn update -> Day05.is_valid_update(rules, update) end)
  |> Enum.filter(fn r -> r end)

result =
  Enum.map(valid_updates, fn inner_list ->
    Enum.at(inner_list, Integer.floor_div(length(inner_list), 2))
  end)
  |> Enum.map(&String.to_integer/1)
  |> Enum.sum()

IO.inspect(result, label: "part1")

# For part 2, get only the invalid updates
# For fixing them, I can always bruteforce by trying all combinations
# I could also try to do some swapping when I find a forbidden page in the accumulator
# Swap could actually be easier with recursion

invalid_updates =
  Enum.filter(updates, fn update ->
    Enum.find(valid_updates, fn valid_update -> update === valid_update end) === nil
  end)

result =
  Enum.map(invalid_updates, fn update -> Day05.fix_invalid_update(rules, update) end)
  |> Enum.map(fn inner_list ->
    Enum.at(inner_list, Integer.floor_div(length(inner_list), 2))
  end)
  |> Enum.map(&String.to_integer/1)
  |> Enum.sum()

IO.inspect(result, label: "part2")
