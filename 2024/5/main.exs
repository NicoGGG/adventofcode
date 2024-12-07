defmodule Day05 do
  @spec is_valid_update(%{String.t() => [String.t()]}, [String.t()]) :: boolean()
  def is_valid_update(rules, update) do
    Enum.reduce_while(update, [], fn page, acc ->
      forbidden = Map.get(rules, page)

      cond do
        forbidden === nil ->
          {:cont, acc ++ [page]}

        Enum.any?(forbidden, fn x -> Enum.find(acc, fn y -> x == y end) !== nil end) ->
          {:halt, false}

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

result =
  Enum.map(updates, fn update -> Day05.is_valid_update(rules, update) end)
  |> Enum.filter(fn r -> r end)
  |> Enum.map(fn inner_list -> Enum.at(inner_list, Integer.floor_div(length(inner_list), 2)) end)
  |> Enum.map(&String.to_integer/1)
  |> Enum.sum()

IO.inspect(result, label: "part1")
