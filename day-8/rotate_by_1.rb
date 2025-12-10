def rotate_arr(arr)
  return arr if arr.empty?

  last = arr.pop
  arr.unshift(last)

  return arr
end


puts rotate_arr [1, 2, 3, 4, 5]