def average(arr)
  arr_length = arr.length

  if arr_length == 0
    return "Array can not empty"
  end

  total_sum = 0

  for num in arr
    total_sum = total_sum + num
  end

  return total_sum/arr_length
end


puts average([2, 5, 8])
puts average([])