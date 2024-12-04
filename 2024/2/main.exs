defmodule ReportChecker do
  def check_report(report) when is_list(report) do
    asc = Enum.sort(report, :asc)
    desc = Enum.sort(report, :desc)

    valid_report =
      Enum.reduce_while(report, 0, fn x, acc ->
        cond do
          acc == 0 ->
            {:cont, x}

          abs(acc - x) in 1..3 ->
            {:cont, x}

          true ->
            {:halt, 0}
        end
      end)

    cond do
      asc !== report && desc !== report ->
        false

      valid_report === 0 ->
        false

      true ->
        true
    end
  end
end

reports =
  File.stream!("file.txt", [:trim_bom, encoding: :utf8])
  |> Enum.map(&String.trim/1)
  |> Enum.map(&String.split/1)
  |> Enum.map(fn report ->
    Enum.map(report, &String.to_integer/1)
  end)

result_part_1 =
  reports
  |> Enum.filter(fn report ->
    ReportChecker.check_report(report)
  end)
  |> Enum.count()

IO.inspect("part1: " <> Integer.to_string(result_part_1))

# Using list comprehension, I can build all combinations of array with a element poped, including the original array
combinations =
  reports
  |> Enum.map(fn report ->
    for {_level, index} <- Enum.with_index(report), reduce: [] do
      acc ->
        updated_report = List.delete_at(report, index)
        [updated_report | acc]
    end
  end)

result_part_2 =
  combinations
  |> Enum.map(fn reports_combination ->
    Enum.filter(reports_combination, fn report -> ReportChecker.check_report(report) end)
  end)
  |> Enum.filter(fn reports_combination -> Enum.count(reports_combination) !== 0 end)
  |> Enum.count()

IO.inspect("part2: " <> Integer.to_string(result_part_2))
