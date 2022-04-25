import numpy as np

'''
Fix-point interation method that find a root by using the derivative
Exit when maximum iterations have been performed
Print number of iterations and error.
'''


def fixed_point(function, x_start: float, error_bound: float, max_iter: int):
    assert max_iter>0, "Invalid maximum iterations"
    n_iterations, error, x_old, x_new = 0, np.inf, x_start, None

    while n_iterations <= max_iter:
        x_new = function(x_old)
        n_iterations, error = n_iterations + 1, abs(x_new - x_old)

        # exit when error<error_bound
        if error < error_bound:
            print(f"Number of iterations: {n_iterations:d}  Error: {error:.2g}")
            return x_new
        # update x_old
        x_old = x_new

    print("The method failed after " + str(max_iter) + "iterations")
    print(f"Number of iterations: {n_iterations:d}  Error: {error:.2g}")
    return x_new


# Example function
def dF(x):
    return np.log(2 * x + 1)


if __name__ == "__main__":
    print(fixed_point(dF, 1.5, 1e-12,100))
