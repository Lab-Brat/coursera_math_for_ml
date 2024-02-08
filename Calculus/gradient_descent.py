import numpy as np
from typing import Tuple
from sklearn.linear_model import LinearRegression


class LinReg:
    def __init__(self, dataset, show=False, method=None) -> None:
        self.data = dataset.pd_data
        self.show = show
        self.method = method

        if self.data.shape[1] != 2:
            print("Only support 2D data, exiting...")
            exit()

    def linear_regression_numpy(self, X, Y):
        m, b = np.polyfit(X, Y, 1)
        return m, b

    def linear_regression_sklearn(self, X, Y):
        X = np.array(X)
        Y = np.array(Y)
        X = X.reshape(self.data.shape[0], 1)
        Y = Y.reshape(self.data.shape[0], 1)
        lr_sci = LinearRegression()
        lr_sci.fit(X, Y)
        m = lr_sci.coef_
        b = lr_sci.intercept_
        return m[0][0], b[0]  # noqa

    def _normalize(self, X, Y):
        X = (X - np.mean(X)) / np.std(X)
        Y = (Y - np.mean(Y)) / np.std(Y)
        return X, Y

    def _denormalize(self, X, Y):
        pass

    def _sum_of_squares_cost_function(self, m, b, X, Y):
        return 1 / (2 * len(Y)) * np.sum((m * X + b - Y) ** 2)

    def _sum_of_squares_partial_divs(self, m, b, X, Y):
        dFdm = 1 / len(X) * np.dot(m * X + b - Y, X)
        dFdb = 1 / len(X) * np.sum(m * X + b - Y)
        return dFdm, dFdb

    def gradient_descent(
        self, m, b, X, Y, learning_rate=0.001, num_iterations=1000, show_cost=False
    ):
        for _ in range(num_iterations):
            dFdm, dFdb = self._sum_of_squares_partial_divs(m, b, X, Y)
            m = m - learning_rate * dFdm
            b = b - learning_rate * dFdb

            if show_cost:
                print(f"cost: {self._sum_of_squares_cost_function(m, b, X, Y)}")
        return m, b

    def linear_regression_from_scratch(self, X, Y):
        X, Y = self._normalize(X, Y)
        m, b = 0, 0
        learning_rate = 1.2
        iterations = 30
        m, b = self.gradient_descent(
            m, b, X, Y, learning_rate, iterations, show_cost=True
        )
        return m, b

    def calculate(self) -> None | Tuple:
        x = self.data[self.data.columns[0]]
        y = self.data[self.data.columns[1]]

        match self.method:
            case "sci":
                result = self.linear_regression_sklearn(x, y)
            case "np":
                result = self.linear_regression_numpy(x, y)
            case "scr":
                result = self.linear_regression_from_scratch(x, y)
            case _:
                print("Allowed methods: sci, np, scr")
                exit()

        if self.show:
            m, b = result
            print("Linear regression (Numpy) results:")
            print(f"slope = {m}, intercept = {b}")

        return result
