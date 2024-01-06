import numpy as np
import matplotlib.pyplot as plt


def plot_vectors(list_v, list_label, list_color):
    _, ax = plt.subplots(figsize=(10, 10))
    ax.tick_params(axis="x", labelsize=14)
    ax.tick_params(axis="y", labelsize=14)
    ax.set_xticks(np.arange(-10, 10))
    ax.set_yticks(np.arange(-10, 10))

    x_size = 8
    y_size = 8
    axis_dimension = (-x_size, x_size, -y_size, y_size)
    plt.axis(axis_dimension)
    for i, v in enumerate(list_v):
        sgn = 0.4 * np.array([[1] if i == 0 else [i] for i in np.sign(v)])
        plt.quiver(
            v[0], v[1], color=list_color[i], angles="xy", scale_units="xy", scale=1
        )
        ax.text(
            v[0] - 0.2 + sgn[0],
            v[1] - 0.2 + sgn[1],
            list_label[i],
            fontsize=14,
            color=list_color[i],
        )

    plt.grid()
    plt.gca().set_aspect("equal")
    plt.show()
