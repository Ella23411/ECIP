import numpy as np

def main():
    errors = np.array([-1, 2, -2])

    squared_error = np.sum(errors**2)
    absolute_error = np.sum(np.abs(errors))

    print("errors =", errors)
    print("squared error =", squared_error)
    print("absolute error =", absolute_error)

if __name__ == "__main__":
    main()