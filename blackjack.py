''' 
the goal in blackjack is to maximize your cards without exceeding 21
if you are given a set of cards and a maximum score:
    what is the maximum value you can achieve without exceeding the maximum score?
    whether it possible to achive a target score?
    
the number of the subproblem is the number of the situation that need decision could be taken, then number of decisions are function of number of cards 
then number of of subproblems is the number of situations (if you knew the right decision at each situation you will do the correct)

the stuation or state space is defined by 4 dimentions:
    - indecies of the cards (size of the deck)
    - player turn
    - value of the player score
    - value of the dealer score
    
So number of the problem is: 
    22 * 22 * (n+1) * 2

so we need a solution for each state what to do?
each state is defined by prev decisions and current situation

State S(player_score, dealer_score, player_turn)

we can use buttom up solution for it
starting from the base state
'''

def maximize_blackjack_winning(deck):
    n = len(deck)
    dp = {}
    
    def compute_value(player_score, dealer_score, deck_idx, player_turn):
        
        if player_score>21:
            return -1
        if dealer_score>21:
            return 1
        if deck_idx> n:
            return 0 
        
        state = (player_score, dealer_score, deck_idx, player_turn)
        
        if state in dp:
            #memoization here we remember the states we computed before
            return dp[state]
        
        if player_turn:
            hit_value = compute_value(player_score+deck[deck_idx], dealer_score, deck_idx+1, player_turn= True)
            stand_value = compute_value(player_score, dealer_score, deck_idx, player_turn= False)
            
            dp[(state)] = max(hit_value, stand_value)
            
        else:
            if dealer_score>=17:
                dp[state] = 1 if player_score>dealer_score else -1 if player_score<dealer_score else 1
            else: 
                dp[state] = compute_value(player_score, dealer_score+ deck[deck_idx], deck_idx+1,False)
        
        return dp[state]
    
    initial_player_score = deck[0] +deck[1]
    initial_dealer_score = deck[2]
    initial_deck_idx = 3
    initial_player_turn = True
    result = compute_value(initial_player_score, initial_dealer_score, initial_deck_idx, initial_player_turn)
    
    player_score, dealer_score, deck_idx, player_turn = (
        initial_player_score,
        initial_dealer_score,
        initial_deck_idx,
        initial_player_turn
    )
    
    #backtrack the strategy
    stratgy = []
    while deck_idx<n:
        if player_turn:
             
            hit_value = float('-inf')
            stand_value = float('-inf')
            
            if player_score + deck[deck_idx]<=21:
                
                hit_value = compute_value(player_score+ deck[deck_idx], dealer_score, deck_idx+1, True)
            else:
                hit_value =-1
                
            stand_value = compute_value(player_score, dealer_score, deck_idx, False)
        
            if hit_value > stand_value:
                stratgy.append('hit')
                player_score += hit_value 
                deck_idx+=1
                
            else:
                stratgy.append('stand')
                player_turn = False
        else: break

    return stratgy, result

if __name__ == "__main__":
    # Example Usage:
    deck =[10, 5, 6, 3, 2, 8, 7, 9, 4, 10, 1, 11]
    strategy, winnings = maximize_blackjack_winning(deck)
    print("Optimal Strategy:", strategy)
    print("Maximum Expected Winnings:", winnings)
        
    

