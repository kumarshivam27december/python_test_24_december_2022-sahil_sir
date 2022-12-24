def fizzBuzz(N):
     
    
    count3 = 0
    count5 = 0
 
    
    for i in range(1, N + 1):
 
       
        count3 += 1
 
        
        count5 += 1
 
        
        flag = False
 
        
        if (count3 == 3):
            print ("Fizz", end = "")
 
            
            count3 = 0
            flag = True
 
       
        if (count5 == 5):
            print ("Buzz", end = "")
 
            
            count5 = 0
            flag = True
 
       
        if (not flag):
            print (i, end = "")
 
        print(end = " ")
 

if __name__ == '__main__':
    N = 15
    fizzBuzz(N)
 
