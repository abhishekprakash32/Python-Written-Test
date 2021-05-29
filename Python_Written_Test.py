'''
Question1
Use python lists and make an list of numbers.
Write a function which returns sum of the list of numbers
'''

def sum_list():
  total = 0
  for i in list_numbers:
    total = total + i
  return total

list_numbers = [5,10,15,20,25]
print (f"Sum of the list of numbers = {sum_list()}")


'''
Question2
Write a function in python in python, which will return maximum i.e function should return dictionary
'''
Dict1={
  '1' : 'Varun',
  '2' : 'Ravi',
  '3' : 'Karun',
  '4' : 'Vicky',
  '5' : 'Shubham'
}
Dict2={
  '1' : 70,
  '2' : 98,
  '3' : 50,
  '4' : 79,
  '5' : 65
}

x = max(Dict2.items(),key=lambda x : x[1])
y = Dict1[x[0]]
print('************Return detail of user whose maximum exam score:-************')
print('User ID = ',x[0])
print('Name = '+y)
print(f'Exam score = {x[1]}')

'''
Question 3
Write a python function to the number of maximum consecutive  one’s present in the array. 
'''
def maxlength(arr, n):
	count = 0
	result = 0
	for i in range(n):
		if (arr[i] == 0):
			count = 0
		else:
			count+= 1
			result = max(result, count)
	return result

arr = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
n = len(arr)
print(maxlength(arr, n))


