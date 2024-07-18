import regex

def check_full_name(full_name):
   pattern = r'^[A-Z][a-z] + [A-Z][a-z]+$'

   if regex.match(pattern, full_name):
      return True
   else:
      return False