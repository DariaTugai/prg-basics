def avg_speed(distance,hours,minutes):
    avg=distance/(hours + minutes/60)
    return avg

print(avg_speed(50,2,30))