N = int(input())

#00:00:00 ~ (N~23):59:59
overalSec = 0
count = 0
hour, min, sec = 0,0,0

while hour <= N:
    hour = overalSec // 3600
    min  = (overalSec % 3600) // 60
    sec  = overalSec % 60
    overalSec += 1 
    if '3' in str(hour)+str(min)+str(sec):
        count += 1
        
print(count)
        
    
    