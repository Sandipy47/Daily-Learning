# Factorail number in the Python
# with the recursion 

def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))


# Generator Wiht the factorial
def factorial(n):
    fact = 1
    
    for ele in range(1, n+1):
        fact *= ele
        yield fact

for value in factorial(5):
    print(value)



Count the frequence 

def frequence_count(nums):
    freq = {}
    for ele in nums:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1   
    return freq
            
print(frequence_count([1,23,4,4,4,5,6,6,6,7,7,8,8,8,9,9,9]))   




Find the first character is not repeating in the string 

def first_non_repeating_char(word):
    freq = {}
    temp = ''
    for ch in word:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1 
    print(freq)
    
    # for i,j in freq.items():
    #     for k in word:
    #         if k == i and j == 1:
    #             return k  
       
    for char in word:
        if freq[char] == 1:
            return char                   
    print(temp)
n = "sansndip"
print(first_non_repeating_char(n))



# string grouping

def string_grouping(words):
    store = {}
    for word in words:
        key = word[0]       #When the for loop first thing the word oth index assign in key
        if key in store:
            store[key].append(word)    
        else:
            store[key] = [word]
    return store

lst = ["apple", "ant", "ball", "badminton", "cat", "car"]
print(string_grouping(lst))

               
               
   
   
               
                          


