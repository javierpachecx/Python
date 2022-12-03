# Search for an item in an ordered list

def binary_search(list, element):
  # We set the lower and upper bounds for the search.
  lower_limit = 0
  upper_limit = len(list) - 1

  # as long as the element has not been found and there are still elements to search for
  while lower_limit <= upper_limit:
    # Calculate the index of the middle element of the list.
    middle_index = (lower_limit + upper_limit) // 2

    # If the middle element is the searched element, we return it.
    if list[middle_index] == element:
      return middle_index

    # If the middle element is less than the searched element, we update the lower limit
    if list[middle_index] < element:
      lower_limit = middle_index + 1

    # If the middle element is greater than the searched element, we update the upper boundary
    else:
      upper_limit = middle_index - 1

  # If the element was not found, we return -1
  return -1

# Let's test the program with an example
list = [1, 3, 5, 5, 7, 9]
element = 7
index = binary_search(list, element)
if index != -1:
  print("The element", element, "is in position", index, "of the list")
else:
  print("The element", element, "is not found in the list")