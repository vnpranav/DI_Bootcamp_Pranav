def merge_sort(arr: list):
   if len(arr) > 1:
      left = arr[:len(arr) // 2]
      right = arr[len(arr) // 2:]

      merge_sort(left)
      merge_sort(right)

      i = 0
      j = 0
      k = 0
      while i < len(left) and j < len(right):
         if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
            k = k + 1
         else:
            arr[k] = right[j]
            j += 1
            k += 1
      
      while i < len(left):
         arr[k] = left[i]
         i += 1
         k += 1

      while j < len(right):
         arr[k] = right[j]
         j += 1
         k += 1

      return arr
   else:
      return arr
   
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))