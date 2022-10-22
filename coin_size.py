import numpy as np
import time

class MonteCarloCoin:
    """
    Simulation to estimate the radius of a circle by firing darts.

    Arguments
    ------------

    radius_circle: float. Radius of the Circle to be estimated. Only used to
    calculate number of darts that fall inside circle.
    side_square: float. Length of the side of the square
    n_shots: int. Number of darts fired.

    Returns
    -----------

    simulated_radius: array-like or float. Returns an array is n_shots is an array.
    Returns a float is n_shots is an int.
    """
    def __init__(self, radius_circle, side_square, n_shots, verbose = False):
        self.radius_circle = radius_circle
        self.side_square = side_square
        self.n_shots = n_shots
        self.verbose = verbose
        if type(self.n_shots) == int:
            self.n_shots = [self.n_shots]

    def area_of_circle(self, area_square, coin_hits, total_hits):
        area_circle = (coin_hits / int(total_hits)) * area_square 
        return area_circle

    def random_shot(self):
        x = (np.random.random(1)[0] * self.side_square) - (self.side_square / 2)
        y = (np.random.random(1)[0] * self.side_square) - (self.side_square / 2)
        return x, y

    def run(self):
        simulated_radius = np.zeros(len(self.n_shots))
        start_simulate = time.time()
        for idx, j in enumerate(self.n_shots):
            start = time.time()
            n_coin_shots = 0
            for i in range(int(j)):
                a, b = self.random_shot()
                if ((a ** 2) + (b ** 2)) <= (self.radius_circle ** 2):
                    n_coin_shots += 1
            end = time.time()

            area_circle = self.area_of_circle(self.side_square ** 2, n_coin_shots, j)
            calculated_radius = np.sqrt(area_circle / np.pi)
            if self.verbose:
                print(f"N_Shots: {j} | Time: {end - start:.2f} seconds | Calculated Radius: {calculated_radius:.2f}")
            simulated_radius[idx] = calculated_radius
        
        end_simulate = time.time()
        if self.verbose:
            print(f"Total time for simulation: {end_simulate - start_simulate:.2f} seconds")

        return simulated_radius


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()

    radius_circle = 1.75
    side_square = 5.
    n_shots = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6]
    coin = MonteCarloCoin(radius_circle, side_square, n_shots, verbose = True)

    radii = coin.run()

    plt.plot(n_shots, radii)
    plt.scatter(n_shots, radii, color = "red")
    plt.xscale("log")
    plt.xlabel("No of shots")
    plt.ylabel("radius")
    plt.title("Number of shots vs radius")
    plt.savefig("plot.png")