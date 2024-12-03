elements =
  File.stream!("file.txt")
  |> Enum.map(&String.trim/1)
  |> Enum.map(&String.split/1)
  |> Enum.map(fn inner_list -> Enum.map(inner_list, &String.to_integer/1) end)

result_part_1 =
  elements
  |> Enum.filter(fn inner_list ->
    Enum.sort(inner_list, :asc) == inner_list || Enum.sort(inner_list, :desc) == inner_list
  end)
  |> Enum.map(fn inner_list ->
    Enum.reduce_while(inner_list, 0, fn x, acc ->
      cond do
        acc == 0 ->
          {:cont, x}

        abs(acc - x) > 0 && abs(acc - x) < 4 ->
          {:cont, x}

        abs(acc - x) == 0 || abs(acc - x) >= 4 ->
          {:halt, 0}
      end
    end)
  end)
  |> Enum.filter(fn el -> el !== 0 end)
  |> Enum.count()

IO.inspect(combinations)

IO.inspect(result_part_1)
