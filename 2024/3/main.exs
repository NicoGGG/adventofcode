r = ~r/mul\((?<digits>[[:alnum:]]+,[[:alnum:]]+)\)/

memory = File.read!("sample.txt")

result_part_1 =
  Regex.scan(r, memory, capture: :all_names)
  |> Enum.map(&List.last/1)
  |> Enum.map(fn inner_string -> String.split(inner_string, ",") end)
  |> Enum.map(fn two_digits -> Enum.map(two_digits, &String.to_integer/1) end)
  |> Enum.map(fn two_digits -> Enum.reduce(two_digits, 1, fn a, acc -> a * acc end) end)
  |> Enum.sum()

IO.inspect(result_part_1)

# For part two, I should probably use return: :index option on do and don't matching to create windows of active mul
# Then I should use it again with the mul matching, and filter those that are not in a window
# Then transform the remaining to string by slicing the original string on the correct indexes, and redo the Enums from part 1
# Also, maybe I could match both mul and do/don't at the same time using named_capture ?

memory_part_2 = File.read!("file.txt")

dos = ~r/do\(\)/

dont = ~r/don\'t\(\)/

do_functions =
  ([[{0, 4}]] ++ Regex.scan(dos, memory_part_2, return: :index))
  |> Enum.map(fn inner_list -> Enum.map(inner_list, &Tuple.to_list/1) end)
  |> Enum.map(fn [inner_list] -> Enum.sum(inner_list) end)

dont_functions =
  Regex.scan(dont, memory_part_2, return: :index)
  |> Enum.map(fn inner_list -> Enum.map(inner_list, &Tuple.to_list/1) end)
  |> Enum.map(fn [inner_list] -> Enum.sum(inner_list) end)

IO.inspect(do_functions)
IO.inspect(dont_functions)
