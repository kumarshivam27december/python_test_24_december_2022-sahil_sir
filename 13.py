def fizzBuzz(N):
     
    # Stores count of multiples
    # of 3 and 5 respectively
    count3 = 0
    count5 = 0
 
    # Iterate from 1 to N
    for i in range(1, N + 1):
 
        # Increment count3 by 1
        count3 += 1
 
        # Increment count5 by 1
        count5 += 1
 
        # Initialize a boolean variable
        # to check if none of the
        # condition matches
        flag = False
 
        # Check if the value of count3
        # is equal to 3
        if (count3 == 3):
            print ("Fizz", end = "")
 
            # Reset count3 to 0, and
            # set flag as True
            count3 = 0
            flag = True
 
        # Check if the value of count5
        # is equal  to 5
        if (count5 == 5):
            print ("Buzz", end = "")
 
            # Reset count5 to 0, and
            # set flag as True
            count5 = 0
            flag = True
 
        # If none of the condition matches
        if (not flag):
            print (i, end = "")
 
        print(end = " ")
 
# Driver Code
if __name__ == '__main__':
    N = 15
    fizzBuzz(N)
 