#Push All Zero's to the end in the array

import numpy as np

def push_zero_to_end (arr):
    temp = 0
    for ele in range(len(arr)):
        if arr[ele] !=0:
            arr[ele], arr[temp] = arr[temp], arr[ele]
            temp = temp + 1
    return arr
        
array = np.array([3,5,67,0,87,00,0,87,7,790,0,0,7655,0,0,760,80,0,0,0,69])

print(push_zero_to_end(array))



#-------------------------------------

arr = np.array([3,5,67,0,87,00,0,87,7,790,0,0,7655,0,0,760,80,0,0,0,69])

keep_zero = arr[arr == 0]
arr_number = arr[arr != 0]

new_array = np.concatenate((arr_number, keep_zero))
print(new_array)







