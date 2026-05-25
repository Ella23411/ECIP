import numpy as np

def main():
    t = np.array([1, 2, 3])
    y = np.array([40, 42, 45])

    A = np.vstack([t, np.ones(len(t))]).T

    params = np.linalg.lstsq(A, y, rcond=None)[0]
    a, b = params

    x = np.array([a, b])

    Ax = A @ x
    r = y - Ax
    squared_error = np.sum(r**2)

    print("A =\n", A)
    print("y =", y)
    print("a =", a)
    print("b =", b)
    print("Ax =", Ax)
    print("r =", r)
    print("squared error =", squared_error)

if __name__ == "__main__":
    main()
