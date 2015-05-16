import numpy as np

right = np.asarray(xrange(100,1000))
palindromes = []
for i in right:
    checking_array = i*right
    for k in checking_array:
        s = str(k)
        r = s[0]+s[1]+s[2]
        l = s[-1]+s[-2]+s[-3]
        if r==l:
            palindromes.append(k)
palindromes = np.asarray(palindromes)
max_palindrome = np.max(palindromes)
print max_palindrome
