def returnMinMax( arr)
  puts arr.length
  max = arr[0]
  min = arr[0]
  for num in arr
    if num > max
      max = num
    end
    if num < min
      min = num
    end
  end

  [min, max]
end

puts returnMinMax([10, 9, 4, 1, 3])
puts returnMinMax([12, 45, 2, 9, 100, -5, 56])