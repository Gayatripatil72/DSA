#For creating an array using array module in python.


#Syntax: arr_name = array.array(typecode ,[elements])   Typecode is the type of array elements.(i = int ,f = float)
#(d = float for double ,b = int for byte ,B = unsigned char)


import array
arr = array.array('i',[23, 45 , 7, 89, 67,8 ,0])

for i in arr:
    print(i)

#Accesing elments by indexing

'''print( "The Array elements are :",arr[0])
print( "The Array elements are :",arr[5])'''

#Appending element in array
# append method adds the element at the end of the array.

'''arr.append(60)
print("After appending array:",arr)'''

#adding element to specific index using insert method .
#Syntax : array_name.insert(index ,element)

'''arr.insert(2 , 25)
print("Array after adding :", arr)'''

#removing an element
#Syntax : array_name.remove(element)

'''arr.remove(25)
print(arr)
'''
#by poping we can delete specific index number or last number
#syntax:array_name.pop()  -> for last element
#array_name.pop(1) -> for perticular element

'''arr.pop()
arr.pop(4)
print(arr)'''

#by using reverse we can reverse the array

'''arr.reverse()
print(arr)'''

#converting array to list
'''l1 = arr.tolist()
print(l1)'''

#we can add array over the existing array using extend function

'''arr1 = array.array('i',[70 , 80])
arr.extend(arr1)
print(arr)'''

print("Buffer info:", arr.buffer_info())

