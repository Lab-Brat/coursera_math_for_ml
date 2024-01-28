from typing import Tuple
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression


class DataSet:
    def __init__(self, data_file, show=False) -> None:
        self.pd_data = pd.read_csv(data_file)
        self.show = show

        if show:
            self.show_dataset(self.pd_data)

    def show_dataset(self, pd_data):
        print("Preview:")
        print(pd_data.head())
        #pd_data.plot(x="TV", y="Sales", kind="scatter", c="black", backend="matplotlib")
        print()
        print(f"Dimensions: {pd_data.shape[1]} columns of length {pd_data.shape[0]}")
        print()
        print(f"Column names:")
        for column in pd_data.columns:
            print(column)
        print()


class LinReg:
    def __init__(self, dataset: DataSet, show=False, method=None) -> None:
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
        return m[0][0], b[0] #noqa

    def linear_regression_from_scratch(self, X, Y):
        return (0, 0)

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


if __name__ == '__main__':
    data_file = './data/tvmarketing.csv'
    dataset = DataSet(data_file, show=True)
    method = "sci"
    LinReg(dataset, show=True, method=method).calculate()

