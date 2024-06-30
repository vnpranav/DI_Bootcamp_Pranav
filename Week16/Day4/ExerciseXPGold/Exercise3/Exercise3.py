def power(base, exponent):
   if exponent == 1:
      return base
   else:
      return base * power(base,exponent -1)
   
print(power(2,4))