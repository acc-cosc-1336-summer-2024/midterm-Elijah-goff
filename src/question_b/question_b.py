#write functions here, don't add input('') statements here

original_string = "Hello, World"
reversed_string = ''
index = len(original_string) - 1

while index >= 0:
  reversed_string += original_string[index]
  index -= 1

  print("Original String:", original_string)
  print("Reversed String", reversed_string)

