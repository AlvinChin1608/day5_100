"""
Write a program that calculates the average student hight from a list of heights. 
eg. student_heights = [180, 124, 165]

The average height can be calculated by adding all the heights together and dividing by the total number of heights

average height rounded to the nearest whole number = 123

Important: You should not use the sum() or len() functions in your answer. You should try to replicate their functionality what you have learnt about for loops

"""
#Method 1 : input a python list of student heights
student_heights = input("Please insert the heights of the students separated by spaces: ").split()
sum_heights = 0 
average = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_heights = sum_heights + student_heights[n]
average = round(sum_heights/len(student_heights))
print(f"total height: {sum_heights}")
print(len(f"Number of students: {student_heights}"))
print(f"average height {average}")

# Method 2 - without the Len() and Sum() challenge

student_heights = input("Please insert the heights of the students separated by spaces: ").split()
sum_height = 0
student_count = 0
for height in student_heights:
  height = int(height) 
  # print(height)
  sum_height += height
  student_count = student_count + 1
  average = round(sum_height/student_count)
print(sum_height)
print(student_count)
print(average)

#Method 3 - Re-doing but seperate it 

student_heights = input("Please insert the heights of the students separated by spaces: ").split()
# n iterates over the indices of the student_heights list.
#we did not use this for loop, the n is an index that is used to access a specific element in the student_height list. 
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print("Total height: " + str(total_height))

number_of_student = 0
for student in student_heights:
  number_of_student += 1
print("Number of students: " + str(number_of_student))

average_height = total_height / number_of_student
print("Average height: " + str(average_height))