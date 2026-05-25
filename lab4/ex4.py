import numpy as np

def main():
    s1 = np.array([1, 2])
    s2 = np.array([2, 4])

    A = np.vstack([s1, s2]).T

    rank = np.linalg.matrix_rank(A)
    det = np.linalg.det(A)

    print("A =\n", A)
    print("rank =", rank)
    print("det =", det)

    if rank < A.shape[1]:
        print("Columns are NOT independent")
    else:
        print("Columns are independent")

if __name__ == "__main__":
    main()