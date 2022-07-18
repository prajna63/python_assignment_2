list1 = [1,2,3,4,5] 
 list2 = [4,5,6,7,8] 
  
 def mult_lists(a,b) : 
   sum = 0 
   for i in range(len(list1)) : 
      sum += list1[i] * list2[i] 
   return sum 
  
 print("Two lists are :") 
 print(list1,list2) 
 print("sum of product of corresponding elements :") 
 print(mult_lists(list1,list2)) 
  
 
