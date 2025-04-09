#For creating an array using array module in python.


#Syntax: arr_name = array.array(typecode ,[elements])   Typecode is the type of array elements.(i = int ,f = float)
#(d = float for double ,b = int for byte ,B = unsigned char)


import array
arr = array.array('i',[23, 45 , 7, 89, 67,8 ,0])

'''for i in arr:
    print(i)'''


#Accesing elments by indexing

'''print( "The Array elements are :",arr[0])
print( "The Array elements are :",arr[5])'''

#Appending element in array
# append method adds the element at the end of the array.

'''arr.append(60)
print("After appending array:",arr)'''

#adding element to specific index using insert method .
#Syntax : array_name.insert(index ,element)

arr.insert(2 , 25)
print("Array after adding :", arr)