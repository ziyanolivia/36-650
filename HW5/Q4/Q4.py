def pyramid(p):
   if (not isinstance(p, int)):
        print("Invalid Input")
   elif (p < 0):
        print("Invalid Input") 
   else:
       num = 1
       for m in range(1, p+1):
           for n in range(1, m+1):
               print(num, end=" ")
               num = num + 1
           print("\n")
# test the output
pyramid(3)
pyramid(6)

# Edge cases
pyramid(-2)
pyramid(1.1)
