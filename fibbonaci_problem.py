# class DPSolver:
#     def __init__():
        
#         pass
"""
this code solves the fibbonaci problem in dynamic programming manner
"""
if __name__ == "__main__":
    
    def fibbonaci_dp(n):
        
        if n <= 1 and n >= 0: 
            return 1
        memo = [0] * (n+1)
        memo[0] = 1
        memo[1] = 1
        
        for i in range(2,n+1):
            memo[i] = memo[i-1] +memo[i-2]
        
        return memo[n]
    
    def test_fibbonaci_dp():
        assert fibbonaci_dp(0) == 1 , "test case 0 failed"
        assert fibbonaci_dp(1) == 1 , "test case 1 failed"
        assert fibbonaci_dp(2) == 2 , "test case 2 failed"
        assert fibbonaci_dp(15) == 987, "test case 15 failed"
        
        print("all tests are passed")
        
    test_fibbonaci_dp()
        
        
    
    
    