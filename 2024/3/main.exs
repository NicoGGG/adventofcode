r = ~r/mul\(([[:alnum:]]+,[[:alnum:]]+)\)/

memory = File.read!("file.txt")

result_part_1 =
  Regex.scan(r, memory)
  |> Enum.map(&List.last/1)
  |> Enum.map(fn inner_string -> String.split(inner_string, ",") end)
  |> Enum.map(fn two_digits -> Enum.map(two_digits, &String.to_integer/1) end)
  |> Enum.map(fn two_digits -> Enum.reduce(two_digits, 1, fn a, acc -> a * acc end) end)
  |> Enum.sum()

IO.inspect(result_part_1)

