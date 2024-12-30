'''
choose the effective finger that minimize the diffculty 
we have sequence of notes and five fingers(right hand)

Number of subproblems depend on the state space:
    we have two state variables the index of key and the index of finger
    at each state we solve F different problems so the number of the subproblems is F*N 
    total nnumber of the subproblems N*F^2 
'''

def play_note_effectivly(note):
    
    '''
    note (list): sequence of keys will be pressed 
    
    returns: 
        list of best moves sequences for this problem

    '''
    
    fingers = [1, 2, 3, 4, 5]
    f  =len(fingers)
    n = len(note)
    dp = [[float('inf')]*n for _ in range(f)]
    trace = [[-1]*n for _ in range(f)]
    
    for f in range(fingers):
        dp[f][0] = calc_diffculty(f + 1, note[0], 0, 0)  # Assume an initial dummy state
        
    for n in range(1, len(note)):
        # For each note in the sequence (starting from the second note)
        for p in range(f):
            # If the current finger for this note is p
            for q in range(f):
                # Transitioning from finger q (previous note) to finger p
                difficulty = dp[q][n-1] + calc_diffculty(q + 1, note[n-1], p + 1, note[n])

                if difficulty < dp[p][n]:
                    dp[p][n] = difficulty
                    trace[p][n] = q #wht is the next move q from the finger p
                    
    min_cost = float('inf')
    
    #starting from the last finger I endded at
    last_finger = -1
    for p in range(f):
        if dp[p][n-1]< min_cost:
            min_cost =dp[p][n-1]
            last_finger = p
            
    #reconstructing the path
    path =[]
    current_finger = last_finger
    for i in range(n-1, -1, -1): #starting from the end and end where you start and go backward
        path.append(current_finger+1) # 1 based indexing 
        current_finger = trace[current_finger][i] #at note I what is the finger is being used 
        
        
            
                    
    def calc_diffculty(f,p,g,q):
        """
        pressing p notre with f finger then pressing q with finger g
        """
        diffculty  = abs(f-g) * abs(p-q)
        return diffculty
        
        
    return path[::-1] # reversed to make the order true