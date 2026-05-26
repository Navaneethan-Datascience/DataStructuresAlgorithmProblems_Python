def generate_sequence(length):
    
    if length <= 0:
       return []      #return empty list
    if length == 1:
       return [1]     #returns th3 first list value
    if length == 2:
       return [1,1]   #returns the list with first two value
    
    seq	= [1,1] 
    
    for n in range(3,length + 1):
        next_term = seq[n-3] + seq[n-2] + n    #formula: a_n = a_(n-2) + a_(n-1) + n
        seq.append(next_term)
    
    return seq


sequence = generate_sequence(5)
print(sequence)