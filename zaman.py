a = float(input("zaman ra bar hasab zam vared konid: "))

hours = a // 3600
minutes = (a% 3600) // 60
seconds = (a % 3600) % 60

print("Time:", hours, "hours,", minutes, "minutes,", seconds, "seconds")