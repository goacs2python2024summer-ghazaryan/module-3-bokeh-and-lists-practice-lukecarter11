import random
def marble_game(plays):
  marbles = ['blue', 'blue', 'blue', 'red', 'red', 'black']
  total = 0
  results = []
  for i in range(plays):
    draw1 = random.choice(marbles)
    marbles.remove(draw1) 
    draw2 = random.choice(marbles)
    marbles.append(draw1)  # Put the first marble back
    if draw1 == draw2:
      total += 1  
    else:
      total -= 1  
    results.append(total)
    
  return results
  

#example
print(marble_game(5))

