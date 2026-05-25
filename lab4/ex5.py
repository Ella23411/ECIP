import numpy as np
import matplotlib.pyplot as plt

def main():
    t = np.array([0, 1, 2, 3, 4, 5])
    energy = np.array([10, 12, 15, 19, 22, 25])

    A = np.vstack([t, np.ones(len(t))]).T
    params = np.linalg.lstsq(A, energy, rcond=None)[0]
    a, b = params

    consumption_rate = a

    fitted = A @ np.array([a, b])

    print("slope (consumption rate) =", consumption_rate)
    print("intercept =", b)

    plt.scatter(t, energy)
    plt.plot(t, fitted)
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.title("Energy vs Time with Linear Fit")
    plt.show()

if __name__ == "__main__":
    main()