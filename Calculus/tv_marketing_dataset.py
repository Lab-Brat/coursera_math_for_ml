import pandas as pd
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


if __name__ == "__main__":
    data_file = "./data/tvmarketing.csv"
    dataset = DataSet(data_file, show=True)
    method = "scr"
    LinReg(dataset, show=True, method=method).calculate()
