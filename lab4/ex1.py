import numpy as np

def main():
    y = np.array([21, 22, 23, 24])
    x = np.mean(y)
    residuals = y - x
    mse = np.mean(residuals**2)

    print("Sensor readings:", y)
    print("Estimated (calibrated) temperature x =", x)
    print("Residuals:", residuals)
    print("Mean squared error:", mse)

if __name__ == "__main__":
    main()