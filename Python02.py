# Count the occurance of the given number and after that find the max occurance count like highest count

import numpy as np

arr = np.array([457,457,457,547,67,8,8,8,5667,54,543,63,345])
obj = {}
temp = 0

for  ele in arr:       #first here it will check the element is exists in the obj or not.
    if  ele in obj:    
        temp = obj[ele]      # if the element is exists in the obj then the index of obj will assign to the temp and the temp will get +1
        temp = temp + 1
        obj[ele] = temp     # And here the obj of i the index value got the temp value where the value increment happen.
        
    else:
        obj[ele] = 1     # if the not exists then this keep the key in the dict with the value of 1.

print(obj)   


# if we have to find the highest occurance then 

max_count = 0
max_value = None

for key in obj:      #we already have the occurance count in the form of dict we saved.
    
    if obj[key] > max_count:    #initally the max_count is 0 then the key of obj is 457 and the value is 3 it comes 3 times.
        max_count = obj[key]    # Here if the max_count is less then the obj[key]= 3 is greater the max count then the key what is 457 is store in the max value.
        max_value = key         # loop iterate the len(obj)
   
print(f"High Value: {max_value}")     #Here just printing the vallues.      
print(f"High Count: {max_count}")     # We can also do in function but for my understanding i follow this way






#-----------------------------------------------------------------------------
# Palindrom



def find_the_palindrom(palindrom):
    rev = ''
    for ch in palindrom.lower():    #This a very simple way we can perform the palindrom without built in method.
        rev = ch + rev
    print(rev, user_input)    
    if rev == user_input.lower():
        print(f"{rev} This is an palindrom") 
    else:
        print(f"{rev} This not a palindrome")       
          
          
user_input = input("Enter a VALID things: ")
print(find_the_palindrom(user_input))






#------------------------------------------------------------------
# Reverse the word in place


def reverse_word_in_place(sentence):
    word = ' '
    result = ''
    
    for ch in sentence:
        if ch != ' ':        #Here is the character fount the it reverse the word and store in word variable and in the else part store the word value in the result and + space.
            word = ch + word
        else:
            result += word + " "  # Here it is save the word
            word = ''        #Here again the word is empty 
    result += word     # And Here is put the last reverse word in the result
    return result    #simply we are returning the result

n = "Hey i am daily learning and clear my concept again HAAHAHAHAHAH"
print(reverse_word_in_place(n))          
            
            