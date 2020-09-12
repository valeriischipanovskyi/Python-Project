def even_only(numbers):
   for num in numbers:
      if num% 2 == 0:
         yield num

def sum_even_only_v2(numbers):
   """Суммирует все четные числа"""

   result = 0
   for num in even_only(numbers):
       result += num
   return result

print(sum_even_only_v2([5,7,8,9,10,2,2]))