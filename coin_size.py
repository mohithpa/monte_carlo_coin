import numpy as np
import matplotlib.pyplot as plt

def area_of_circle(asquare, coin_hits, total_hits):
    acircle = (coin_hits/total_hits)*asquare 
    return acircle

square_side = 5
def random_shot(side):
    halfside = side/2
    x=(np.random.random(1)[0]*5) - halfside
    y=(np.random.random(1)[0]*5) - halfside
    return x, y

Ncoin = 0
N = 0

radius_of_circle = 1.75
def circle_checker(number1, number2,radius):
    global N
    global Ncoin
    if (number1**2) + (number2**2) <= radius**2:
        Ncoin = Ncoin + 1
        N = N + 1
    else:
        N=N+1

for i in range(100):
    a,b = random_shot(square_side)
    circle_checker(a,b,radius_of_circle)

areaaa = area_of_circle(square_side**2,Ncoin, N)
print(areaaa)