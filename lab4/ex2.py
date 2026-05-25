import numpy as np

def main():
    t = np.array([1, 2, 3])
    y = np.array([40, 42, 45])

    A = np.vstack([t, np.ones(len(t))]).T

    params = np.linalg.lstsq(A, y, rcond=None)[0]
    a, b = params

    print("A =\n", A)
    print("y =", y)
    print("a =", a)
    print("b =", b)

if __name__ == "__main__":
    main()
