def odd_even(arr)
  odd_count = 0
  even_count = 0
  for num in arr
    if num % 2 == 0
      even_count = even_count + 1
    else
      odd_count = odd_count + 1
    end
  end
  return odd_count, even_count
end


puts odd_even([1, 2, 3, 4 , 5])