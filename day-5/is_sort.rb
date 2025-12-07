def is_sort(arr)
  length = arr.length
  puts length

  if length <= 1
    return true
  end

  (0...arr.length - 1).each do |i|
    # Compare current element with the NEXT element
    if arr[i] > arr[i + 1]
      return false
    end
  end

  return true
end


puts is_sort([1, 4])
puts is_sort([2, 7, 9, 10])