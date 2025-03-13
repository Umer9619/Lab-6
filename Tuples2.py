# A tuple of strings
fruits_tuple = ('Kiwi', 'Pineapple', 'blueberry')

print(fruits_tuple[0])  
print(fruits_tuple[1])  

print(fruits_tuple[-1])  
print(fruits_tuple[-2]) 

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
co_tuple = tuple1 + tuple2
print(co_tuple)

tuple3 = ('hello',)
repeat_tuple = tuple3 * 3
print(repeat_tuple)

numbers = (0, 1, 2, 3, 4, 5, 6)
print(numbers[1:4])
print(numbers[:3])  

fruits_tuple = ('Kiwi', 'Pineapple', 'Blueberry', 'Kiwi')
print(fruits_tuple.count('Kiwi'))

s=fruits_tuple[0]
print(s.count('i'))

print(fruits_tuple.count('i'))


