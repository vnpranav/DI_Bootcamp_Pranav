def reverse_string(input : str):
   if not input:
      return ""
   else:
      return reverse_string(input[1:]) + input[0]
   
print(reverse_string('hello'))