##Get all substrings of a string
s = input()  
print("The original string is : " + str(s)) 
res = [s[i: j] for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)]   
print("All substrings of string are : " + str(res)) 