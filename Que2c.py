def flatten_list(l): 
         result = [] 
         for element in l: 
                 if type(element) == list: 
                      for i in element: 
                          result.append(i) 
                 else: 
                      result.append(element) 
         return result 
  
 lst = [[1,6,98,2,34], [45, 66, 49], [27, 52, 80]] 
 print("Before :",lst) 
 print("After:",flatten_list(lst)) 
 
