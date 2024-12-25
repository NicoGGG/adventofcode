defmodule Day11 do
  def blink([{0, freq} | tail], acc), do: blink(tail, Map.update(acc, 1, freq, &(&1 + freq)))

  def blink([], acc), do: acc

  def blink([{key, freq} | tail], acc) do
    digits = Integer.digits(key)
    len = Enum.count(digits)

    cond do
      rem(len, 2) == 0 ->
        [left, right] = split(digits, len)
        acc = Map.update(acc, left, freq, &(&1 + freq))
        acc = Map.update(acc, right, freq, &(&1 + freq))
        blink(tail, acc)

      true ->
        r = key * 2024
        acc = Map.update(acc, r, freq, &(&1 + freq))
        blink(tail, acc)
    end
  end

  def blink_stones(stones, 0), do: stones |> Map.values() |> Enum.sum()

  def blink_stones(stones, blinks) do
    stones
    |> Map.to_list()
    |> blink(%{})
    |> blink_stones(blinks - 1)
  end

  def split(digits, len) do
    half = div(len, 2)

    Enum.split(digits, half)
    |> Tuple.to_list()
    |> Enum.map(&Integer.undigits/1)
  end
end

args = System.argv()

case args do
  [filename, blinks] ->
    stones =
      File.read!(filename)
      |> String.split()
      |> Enum.map(&String.to_integer/1)
      |> Enum.frequencies()

    result = Day11.blink_stones(stones, String.to_integer(blinks))

    IO.inspect(result)

  _ ->
    IO.puts("Usage: elixir main.exs <filename> <blinks>")
end

## Part 2
## My approach was too naive to work for part 2. When blinking 75 times, the number of stones in the array quickly becomes gigantic and iterating over it is too long
## After looking at some solutions, it appears there are two main optimisations
## - Instead of an array of int, I can use a map of frequencies %{ 1234: 3} means there are 3 1234 in the array.
##   Since there are obviously a lot of duplicates, this reduces the size of the iterator by a lot
## - I can use "memoization" (I just learned what it is) to cache previous results.
##   I think the idea is to store a separate map like %{previous_value: next_value}, so where I blink a stone, I check if the cache map has a key of it
##   If it does, there is no need to compute anything like modulo and split, just return the saved value

## After implementing cache, it didn't change anything and part 2 was still taking way too long
## Looks like the real optimization is the frequency thing. This will require a complete overhaul tho...
## In addition to iterating over less elements, I can solve multiple stone at once
## If I have %{1: 100}, I only need to do it once and change the key to %{2024: prev_value + 100}

## I have a working solution without cache. I could optimize further with it but the real solution was using a map of frequencies
## This is expected since there must be a lot of duplicate values seeing the size of the array, but every time a number has 8xdigits, it is split down to 1 digit
## So we never actually have insanely large integer
