fruits_list = ['apple', 'banana', 'cherry']
print(fruits_list[0])  # Output: apple
print(fruits_list[1])  # Output: banana
print(fruits_list[-1])  # Output: cherry
print(fruits_list[-2])  # Output: banana
fruits_list[1] = 'blueberry'
print(fruits_list)  # Output: ['apple', 'blueberry', 'cherry']
fruits_list.append('orange')
print(fruits_list)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
fruits_list.insert(1, 'kiwi')
print(fruits_list)  # Output: ['apple', 'kiwi', 'blueberry', 'cherry', 'orange']
fruits_list.remove('kiwi')
print(fruits_list)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
last_fruit = fruits_list.pop()
print(last_fruit)  # Output: orange
print(fruits_list.count('cherry'))  # Output: 1
print(fruits_list.index('apple'))  # Output: 0
fruits_list.clear()
print(fruits_list)  # Output: []

numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3]
print(numbers[:3])   # Output: [0, 1, 2]
print(numbers[4:])   # Output: [4, 5, 6]
print(len(numbers))  # Output: 7
numbers.sort()
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6]
numbers.reverse()
print(numbers)  # Output: [6, 5, 4, 3, 2, 1, 0]