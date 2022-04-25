import numpy as np

'''
Bisection method that find a root within the errorBound
Print number of iterations and error.
'''


def bisection(function, lower_endpoint: float, upper_endpoint: float, error_bound: float):
    assert np.sign(function(lower_endpoint)) * np.sign(function(upper_endpoint)) <= 0 < error_bound \
           and upper_endpoint >= lower_endpoint, "Input not valid'"

    n_iterations, error, root = 0, np.inf, None

    # check whether root is at the endpoints
    if np.sign(function(lower_endpoint)) * np.sign(function(upper_endpoint)) == 0:
        root = lower_endpoint if np.sign(function(lower_endpoint)) == 0 else upper_endpoint
        error = 0

    else:
        # perform bisection method
        while error > error_bound:
            root, error, n_iterations  = lower_endpoint + (upper_endpoint - lower_endpoint) / 2,\
                                         (upper_endpoint - lower_endpoint) / 2,\
                                         n_iterations+1

            if np.sign(function(root)) == 0:
                # exit if f(root)=0
                error = 0
                break
            elif np.sign(function(lower_endpoint)) * np.sign(function(root)) < 0:
                upper_endpoint = root
            elif np.sign(function(root)) * np.sign(function(upper_endpoint)) < 0:
                lower_endpoint = root
            else:
                root = None
                print("bisection fail")
                break

    print(f"Number of iterations: {n_iterations:d}  Error: {error:.2g}")
    return root


# Example function
def func(x):
    return np.exp(x) - 2 * x - 1


if __name__ == "__main__":
    print(bisection(func, 1, 2, 1e-12))
