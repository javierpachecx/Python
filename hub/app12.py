# Determines whether a word is a palindrome or not

# We define a function to determine if a word is a palindrome
def is_palindrome(word):
  # We convert the word to lower case
  word = word.lower()

  # We remove the whitespace from the word
  word = word.replace(" ", "")

  # Create a variable to store the result
  result = True

  # Compare the characters in the word from left to right with the characters from right to left
  for i in range(len(word) // 2):
    if word[i] != word[len(word) - i - 1]:
      result = False
      break

  # We return the result
  return result

# We test the function with an example
word = "Anita washes the bathtub"
if is_palindrome(word):
  print("The word", word, "is a palindrome")
else:
  print("The word", word, "is not a palindrome")