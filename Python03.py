# Find the anagrams


def is_anagram(sentence01, sentence02):
    if len(sentence01) != len(sentence02):     #fist calculate the length of the both words and if the len is not eqaul or same then is not an anagram.
        
        return False
    
    freq = {}
    #first we count the occrance of each count.    
    for ch in sentence01:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    #in the the second one will subtract the with 1 and the last one is zero then it's an anagram        
    for ch in sentence02:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
        
    return True

print(is_anagram("listen", "slient"))\
    
    
#----------------------------------------------------------------------------
# Prime number

def is_prime(n):
    is_prime = False
    
    if n < 2:
        return False
    
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            is_prime = False
        else:
            is_prime = True
            
    return is_prime       

print(is_prime(2))     

            