def sumOfElement(arr)
  count = 0
  for num in arr
    count = count + num
  end
  count
end

puts sumOfElement([1, 2, 10, 20])