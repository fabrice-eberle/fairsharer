def fair_sharer(values, num_iterations, share=0.1):
    
  n = 1
  print(values)
  
  while n<= num_iterations:
      
    index = values.index(max(values))
    share_value = int(values[index] * share)
    
    # Exception if highest item is last item, rightmost neighbor is the first value
    if index+1 == len(values):
        values[0] = values[0] + share_value
        values[index-1] = values[index-1] + share_value
    
    else:
        values[index-1] = values[index-1] + share_value
        values[index+1] = values[index+1] + share_value
    
    values[index]=values[index]-2*share_value    
    n+=1
    print(values)
"""Runs num_iterations.
In each iteration the highest value in values gives a fraction (share)
to both the left and right neighbor. The leftmost field is considered
the neightbor of the rightmost field.
Examples:
fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
Args
values:
1D array of values (list or numpy array)
num_iteration:
Integer to set the number of iterations
"""
# code
  #return values_new
  
fair_sharer([900, 0, 800, 1000], 3)
