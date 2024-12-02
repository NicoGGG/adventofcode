two_columns =
  File.stream!("file.txt")
  |> Enum.map(&String.trim/1)
  |> Enum.map(&String.split/1)
  |> Enum.map(fn inner_list -> Enum.map(inner_list, &String.to_integer/1) end)
  |> Enum.map(&List.to_tuple/1)
  |> Enum.unzip()

result_part_1 =
  Tuple.to_list(two_columns)
  |> Enum.map(fn inner_list -> Enum.sort(inner_list) end)
  |> Enum.zip()
  |> Enum.map(&Tuple.to_list/1)
  |> Enum.map(fn inner_list -> Enum.reduce(inner_list, fn x, acc -> abs(acc - x) end) end)
  |> Enum.reduce(fn x, acc -> acc + x end)

IO.inspect(result_part_1)

list_1 = elem(two_columns, 0)
list_2 = elem(two_columns, 1)

result_part_2 =
  Enum.map(list_1, fn element ->
    element * Enum.count(Enum.filter(list_2, fn x -> x == element end))
  end)
  |> Enum.sum()

IO.inspect(result_part_2)
