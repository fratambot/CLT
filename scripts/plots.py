import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm


def plot_rolls_distribution(rolls, density=True):
    label, counts = np.unique(rolls, return_counts=True)
    fig, axs = plt.subplots(figsize=(8, 4))
    mu, std = norm.fit(np.asarray(rolls))
    print("mu = ", mu)
    print("std = ", std)
    color = "teal"
    axs.set_title(f"Distribution for {len(rolls)} rolls")
    axs.set_xlabel("Value on the die")
    if density:
        axs.set_ylabel("Probability density")
        axs.bar(
            label,
            counts / np.sum(counts),
            alpha=0.4,
            color=color,
            edgecolor=color,
            linewidth=2,
        )
        ymin, ymax = 0, 1
        axs.set_ylim([ymin, ymax])
        plt.vlines(mu, ymin, ymax, color="magenta", label="mu")
        plt.vlines(
            mu - std, ymin, ymax, color="red", linestyles="dashed", label="sigma"
        )
        plt.vlines(mu + std, ymin, ymax, color="red", linestyles="dashed")
    else:
        axs.set_ylabel("Counts")
        axs.bar(label, counts, alpha=0.4, color=color, edgecolor=color, linewidth=2)
        plt.vlines(mu, 0, np.max(counts), color="magenta", label="mu")
        plt.vlines(
            mu - std, 0, np.max(counts), color="red", linestyles="dashed", label="sigma"
        )
        plt.vlines(mu + std, 0, np.max(counts), color="red", linestyles="dashed")

    plt.legend()
    plt.show()
    return mu, std


def plot_dice_sum_distribution(results, density=True):
    label, counts = np.unique(results, return_counts=True)
    fig, axs = plt.subplots(figsize=(8, 4))
    mu, std = norm.fit(np.asarray(results))
    gaussian = norm.pdf(label, mu, std)
    print("mu = ", mu)
    print("std = ", std)
    color = "teal"
    axs.set_title(f"Distribution for {len(results)} rolls")
    axs.set_xlabel("Sum of dice's values")
    if density:
        axs.set_ylabel("Probability density")
        axs.bar(
            label,
            counts / np.sum(counts),
            alpha=0.4,
            color=color,
            edgecolor=color,
            linewidth=2,
        )
        ymin, ymax = 0, 1
        axs.set_ylim([ymin, ymax])
        axs.plot(label, gaussian, color="darkgreen", label="normal distr.")
        plt.vlines(mu, ymin, ymax, color="magenta", label="mu")
        plt.vlines(
            mu - std, ymin, ymax, color="red", linestyles="dashed", label="sigma"
        )
        plt.vlines(mu + std, ymin, ymax, color="red", linestyles="dashed")
    else:
        axs.set_ylabel("Counts")
        axs.bar(label, counts, alpha=0.4, color=color, edgecolor=color, linewidth=2)
        axs.plot(
            label, gaussian * len(results), color="darkgreen", label="normal distr."
        )
        plt.vlines(mu, 0, np.max(counts), color="magenta", label="mu")
        plt.vlines(
            mu - std, 0, np.max(counts), color="red", linestyles="dashed", label="sigma"
        )
        plt.vlines(mu + std, 0, np.max(counts), color="red", linestyles="dashed")

    plt.legend()
    plt.show()

    return
