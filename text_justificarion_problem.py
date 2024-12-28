"""
    this code implements a solution for text justification for a text file which .txt
    
"""
if __name__ == "__main__":
    
    def justify_text(text, line_width):
        '''
        knuth plass line breaking algirithm
            we want to minimize the badness(numerixal measure of gaps or uneven spacing)
            
            badness = ( (avilable space -required space)/line width)^3
            
            the most important paramter till now is the line width
            
        '''
        words_list = text.split()
        words_length = [len(word) for word in words_list]
        
        n = len(words_list)
        
        breakpionts = [-1]*(n+1) #if we stopped at this word what is the index of the first word in the line
        
        dp = [float('inf')]*(n+1) # as the solution is the minmum badness so the intialization value is maximum
        
        dp[0] = 0 #base solution when there are no words
        
        for i in range(1, n+1):
            line_length = 0
            for j in range(i,0, -1): # احنا هنا بنرجع لورا 
                line_length += words_length[j-1]+(1 if (j<i) else 0) 
                
                if line_length > line_width :
                    break
                
                badness = (line_width - line_length)**3
                
                if dp[i-1] + badness < dp[i]:
                    dp[i] =  dp[i-1] + badness
                    breakpionts[i] = j-1
                    
        print(dp)
        lines = build_lines(words_list, breakpionts)
        return lines, breakpionts
    
    def build_lines(words_list, breakpoints):
        lines = []
        i = len(words_list)
        
        while i>0:
            start = breakpoints[i]
            lines.insert(0, " ".join(words_list[start:i])) 
            i = start 
            
        return lines
    
    
    text = "This is an example of text justification"
    line_width = 16

    justified_lines,breaks = justify_text(text, line_width)
    for line in justified_lines:
        print(line)
      
                    
        