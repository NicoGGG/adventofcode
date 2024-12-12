defmodule Day07 do
  def print([result | numbers]) do
    IO.inspect(result, label: "result")
    IO.inspect(numbers, label: "numbers")
  end

  def valid?([result | numbers]) do
    cond do
      Enum.product(numbers) === result ->
        true

      length(numbers) <= 1 ->
        false

      true ->
        [one, two | rest] = numbers
        start_sum = Enum.sum([one, two])
        start_prod = Enum.product([one, two])
        valid?([result | [start_sum | rest]]) || valid?([result | [start_prod | rest]])
    end
  end

  def valid_p2?([result | numbers]) do
    cond do
      Enum.product(numbers) === result ->
        true

      length(numbers) <= 1 ->
        false

      true ->
        [one, two | rest] = numbers
        start_sum = Enum.sum([one, two])
        start_prod = Enum.product([one, two])

        start_concat =
          Enum.map([one, two], fn num -> Integer.to_string(num) end)
          |> Enum.join()
          |> String.to_integer()

        valid_p2?([result | [start_sum | rest]]) || valid_p2?([result | [start_prod | rest]]) ||
          valid_p2?([result | [start_concat | rest]])
    end
  end
end

result =
  File.read!("file.txt")
  |> String.split("\n", trim: true)
  |> Enum.map(&String.split(&1, ~r/[: ]/, trim: true))
  |> Enum.map(fn line -> Enum.map(line, &String.to_integer/1) end)
  |> Enum.filter(&Day07.valid?/1)
  |> Enum.reduce(0, fn [first | _], acc -> acc + first end)

IO.inspect(result)

result =
  File.read!("file.txt")
  |> String.split("\n", trim: true)
  |> Enum.map(&String.split(&1, ~r/[: ]/, trim: true))
  |> Enum.map(fn line -> Enum.map(line, &String.to_integer/1) end)
  |> Enum.filter(&Day07.valid_p2?/1)
  |> Enum.reduce(0, fn [first | _], acc -> acc + first end)

IO.inspect(result)

# NOTE: Part 2 is a bit slow but as an Elixir beginner I find this just too elegant to try and dig further
# Too bad I can't use Enum.product in a guard or it would have been even better
# This language is so cool
