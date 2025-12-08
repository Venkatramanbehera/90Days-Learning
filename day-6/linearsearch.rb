def search arr, target 

  arr.each_with_index do |num, index|
    return index if num == target
  end 

  return nil
end

puts search([1, 7, 90, 6], 2)
puts search([1, 7, 90, 6], 6)