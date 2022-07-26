# 1017 - Gasto de Combustível

time_travel = int(input())
speed_time = int(input())


def consumption(time, speed):
    km = 12
    return (time * speed) / km
    

print(f"{consumption(time_travel, speed_time):.3f}")



