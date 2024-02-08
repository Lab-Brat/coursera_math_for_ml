import pandas as pd
import numpy as np
from gradient_descent import LinReg


class DataSet:
    def __init__(self, data_file, show=False) -> None:
        self.pd_data = pd.read_csv(data_file)
        self.show = show

        if show:
            self.show_dataset(self.pd_data)

    def show_dataset(self, pd_data):
        print("Preview:")
        print(pd_data.head())
        # pd_data.plot(x="TV", y="Sales", kind="scatter", c="black", backend="matplotlib")
        print()
        print(f"Dimensions: {pd_data.shape[1]} columns of length {pd_data.shape[0]}")
        print()
        print(f"Column names:")
        for column in pd_data.columns:
            print(column)
        print()


def predict(m, b, X):
    for x in X:
        y = m * x + b
        print(f"for x={x}, prediction={y}")


def predict_scr(m, b, X, dataset):
    for x in X:
        data = dataset.pd_data
        x_orig = data[data.columns[0]]
        y_orig = data[data.columns[1]]
        x_norm = (x - np.mean(x_orig)) / np.std(x_orig)
        y_norm = m * x_norm + b
        y = y_norm * np.std(y_orig) + np.mean(y_orig)
        print(f"for x={x}, prediction={y}")


if __name__ == "__main__":
    data_file = "./data/tvmarketing.csv"
    dataset = DataSet(data_file, show=True)
    m_sk, b_sk = LinReg(dataset, show=True, method="sci").calculate()
    m_np, b_np = LinReg(dataset, show=True, method="np").calculate()
    m_sc, b_sc = LinReg(dataset, show=True, method="scr").calculate()
    # print(mb_scikit, mb_numpy, mb_frmscr)

    X = [50, 120, 280]
    predict(m_sk, b_sk, X)
    predict(m_np, b_np, X)
    predict_scr(m_sc, b_sc, X, dataset)
