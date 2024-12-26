defmodule Day13 do
  def parse(input) do
    xmove = ~r/X\+(\d+)/
    ymove = ~r/Y\+(\d+)/
    xtarget = ~r/X=(\d+)/
    ytarget = ~r/Y=(\d+)/

    input
    |> String.split("\n\n", trim: true)
    |> Enum.map(&String.split(&1, "\n", trim: true))
    |> Enum.map(fn [a, b, p] ->
      [_, ax] = Regex.run(xmove, a)
      [_, ay] = Regex.run(ymove, a)
      [_, bx] = Regex.run(xmove, b)
      [_, by] = Regex.run(ymove, b)
      [_, px] = Regex.run(xtarget, p)
      [_, py] = Regex.run(ytarget, p)

      [
        [String.to_integer(ax), String.to_integer(ay)],
        [String.to_integer(bx), String.to_integer(by)],
        [String.to_integer(px), String.to_integer(py)]
      ]
    end)
  end

  def play([[ax, ay], [_, _], [px, py]], as, 0)
      when as * ax > px or as * ay > py,
      do: 0

  def play([[ax, ay], [bx, by], [px, py]], as, bs)
      when as * ax + bs * bx == px and as * ay + bs * by == py,
      do: as * 3 + bs

  def play([[ax, ay], [bx, by], [px, py]], as, bs)
      when as * ax + bs * bx <= px and as * ay + bs * by <= py,
      do: play([[ax, ay], [bx, by], [px, py]], as, bs + 1)

  def play([[ax, ay], [bx, by], [px, py]], as, bs)
      when as * ax + bs * bx > px or as * ay + bs * by > py,
      do: play([[ax, ay], [bx, by], [px, py]], as + 1, 0)
end

input =
  File.read!("file.txt")

games = Day13.parse(input)

result = games |> Enum.map(&Day13.play(&1, 0, 1))

IO.inspect(result |> Enum.sum())

## For part 2, I have not looked at solutions for now, but I would assume I need to do some kind of bisecting instead of one by one iteration
## Even tho I could have done it in part 1, I saw an opportunity to do something with Elixir guards and wanted to try it
## I will try to find somes ideas before looking up some solutions
