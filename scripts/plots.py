import matplotlib.pyplot as plt
import numpy as np


def plot_rolls_distribution(rolls, density=True):
    fig, axs = plt.subplots(figsize=(10, 5))
    bins = np.linspace(0.5, 6.5, 7)
    axs.hist(rolls, bins=bins, rwidth=0.8, density=density)
    axs.set_title(f"Distribution for {len(rolls)} rolls")
    axs.set_xlabel("Value on the die")
    if density:
        axs.set_ylabel("Probability density")
        axs.set_ylim([0, 1])
    else:
        axs.set_ylabel("Counts")

    plt.show()
    return
