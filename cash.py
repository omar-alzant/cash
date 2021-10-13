from cs50 import get_float, get_int

while True:
    nbr = get_float("Change owed: ")
    if nbr >= 0:
        break
        
cent = int((nbr*100)+0.5)
total = 0

for coin in [25, 10, 5, 1]:
    total += cent // coin  #total = total + cent /int(coin)
    cent %= coin           #cent = cent % coin  
    
print(total)