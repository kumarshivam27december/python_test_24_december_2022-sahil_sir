def BalancedPartition(str1, n):
     
    # If the size of the string is 0,
    # then answer is zero
    if (n == 0):
        return 0
 
    # Variable that represents the
    # number of 'R's and 'L's
    r = 0
    l = 0
 
    # To store maximum number of
    # possible partitions
    ans = 0
 
    for i in range(n):
         
        # Increment the variable r if the
        # character in the string is 'R'
        if (str1[i] == 'R'):
            r += 1
 
        # Increment the variable l if the
        # character in the string is 'L'
        elif (str1[i] == 'L'):
            l += 1
 
        # If r and l are equal,
        # then increment ans
        if (r == l):
            ans += 1
 
    # Return the required answer
    return ans
if __name__ == '__main__':
     
    str1 = input()
    n = len(str1)
 
    # Function call
    print(BalancedPartition(str1, n))