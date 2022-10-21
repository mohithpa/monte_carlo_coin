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
#def circle_checker(number1, number2,radius):
#    global N
#    global Ncoin
#    if (number1**2) + (number2**2) <= radius**2:
#        Ncoin = Ncoin + 1
#        N = N + 1
#    else:
#        N=N+1
shots = [10,100,1000,10000,100000, 10**6, 10**7]
simulated_radius = []
for j in shots:
    for i in range(j):
        a,b = random_shot(square_side)
        if (a**2) + (b**2) <= radius_of_circle**2:
            Ncoin = Ncoin + 1
            N = N + 1
        else: 
            N = N + 1
        #circle_checker(a,b,radius_of_circle)

    areaaa = area_of_circle(square_side**2,Ncoin, N)
    simulated_element = (areaaa/np.pi)**0.5
    simulated_radius.append(simulated_element)

print(simulated_radius)
plt.plot(shots,simulated_radius)
plt.xscale("log")
plt.xlabel("No of shots")
plt.ylabel("radius")
plt.title("Number of shots vs radius")
plt.savefig("coin_size.png")