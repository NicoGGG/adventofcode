defmodule Day11 do
  def blink(input, 0), do: input

  def blink(input, blinks) do
    IO.inspect(blinks)
    input =
      List.flatten(input)
      |> Enum.map(fn stone ->
        digits = Integer.to_string(stone)
        len = String.length(digits)

        cond do
          stone == 0 -> 1
          rem(len, 2) == 0 -> split(digits)
          true -> stone * 2024
        end
      end)

    blink(input, blinks - 1)
  end

  def split(digits) do
    length = String.length(digits)
    half = Integer.floor_div(length, 2)

    [String.slice(digits, 0, half), String.slice(digits, half, half)]
    |> Enum.map(&String.to_integer/1)
  end
end

input =
  File.read!("file.txt")
  |> String.split()
  |> Enum.map(&String.to_integer/1)

result = Day11.blink(input, 25) |> List.flatten() |> Enum.count()

IO.inspect(result)
