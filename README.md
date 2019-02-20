# Matching-Algorithm

Python script capable of matching best-case-senario pairs for best overall and individual matches.

OneSource() - Pairs within the passed 2D array

  Ex. Work partners on a school project:
    
    Bill: Dan, Dom, Josh  ->  [0,1,3,2] (0 represents self)
    Dan: Bill, Josh, Dom  ->  [1,0,2,3] 
    Josh: Dom, Bill, Dan  ->  [2,3,0,1]
    Dom: Bill, Dan, Josh  ->  [1,2,3,0]
    
  Output is: 
     Josh is paried with Dom
     Bill is paired with Dan 
     
     System Equlibrium : 83% 
            (The worst case senario is that all 4 get their last option. This would be a total of 12 sacrifices (3*4). This solution however only requires 2 sacrifices (2 people chosing their second best option) which is 10/12 or 83% of perfect equlibrium.)
            
