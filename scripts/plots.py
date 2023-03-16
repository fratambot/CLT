import itertools
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
        ymin, ymax = 0, 0.5
        axs.set_ylim([ymin, ymax])
        axs.vlines(mu, ymin, ymax, color="magenta", label="mu")
        axs.vlines(
            mu - std, ymin, ymax, color="red", linestyles="dashed", label="sigma"
        )
        axs.vlines(mu + std, ymin, ymax, color="red", linestyles="dashed")
    else:
        axs.set_ylabel("Counts")
        axs.bar(label, counts, alpha=0.4, color=color, edgecolor=color, linewidth=2)
        axs.vlines(mu, 0, np.max(counts), color="magenta", label="mu")
        axs.vlines(
            mu - std, 0, np.max(counts), color="red", linestyles="dashed", label="sigma"
        )
        axs.vlines(mu + std, 0, np.max(counts), color="red", linestyles="dashed")

    plt.legend()
    plt.show()
    return


def plot_dice_sum_distribution(results, n_dice=" ", density=True):
    label, counts = np.unique(results, return_counts=True)
    fig, axs = plt.subplots(figsize=(8, 4))
    mu, std = norm.fit(np.asarray(results))
    gaussian = norm.pdf(label, mu, std)
    print("mu = ", mu)
    print("std = ", std)
    color = "teal"
    axs.set_title(f"Distribution for {len(results)} rolls")
    axs.set_xlabel(f"Sum of {n_dice} dice's values")
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
        ymin, ymax = 0, 0.5
        axs.set_ylim([ymin, ymax])
        axs.plot(label, gaussian, color="darkgreen", label="normal distr.")
        axs.vlines(mu, ymin, ymax, color="magenta", label="mu")
        axs.vlines(
            mu - std, ymin, ymax, color="red", linestyles="dashed", label="sigma"
        )
        axs.vlines(mu + std, ymin, ymax, color="red", linestyles="dashed")
    else:
        axs.set_ylabel("Counts")
        axs.bar(label, counts, alpha=0.4, color=color, edgecolor=color, linewidth=2)
        axs.plot(
            label, gaussian * len(results), color="darkgreen", label="normal distr."
        )
        axs.vlines(mu, 0, np.max(counts), color="magenta", label="mu")
        axs.vlines(
            mu - std, 0, np.max(counts), color="red", linestyles="dashed", label="sigma"
        )
        axs.vlines(mu + std, 0, np.max(counts), color="red", linestyles="dashed")

    plt.legend()
    plt.show()

    return


def plot_multiple_dice_distributions(results_list, n_dice_list, density=True):
    n_plots = len(results_list)
    figlength = 4 * n_plots
    all_results = list(itertools.chain.from_iterable(results_list))
    max_x = max(all_results)
    fig, axs = plt.subplots(n_plots, figsize=(8, figlength))
    for i, results in enumerate(results_list):
        label, counts = np.unique(results, return_counts=True)
        mu, std = norm.fit(np.asarray(results))
        gaussian = norm.pdf(label, mu, std)
        print("n_dice = ", n_dice_list[i])
        print("mu = ", mu)
        print("std = ", std)
        print("----")
        color = "teal"
        axs[i].set_title(f"Distribution for {len(results)} rolls")
        axs[i].set_xlabel(f"Sum of {n_dice_list[i]} dice's values")
        if density:
            axs[i].set_ylabel("Probability density")
            axs[i].bar(
                label,
                counts / np.sum(counts),
                alpha=0.4,
                color=color,
                edgecolor=color,
                linewidth=2,
            )
            ymin, ymax = 0, 0.5

            axs[i].plot(label, gaussian, color="darkgreen", label="normal distr.")
            axs[i].vlines(mu, ymin, ymax, color="magenta", label="mu")
            axs[i].vlines(
                mu - std, ymin, ymax, color="red", linestyles="dashed", label="sigma"
            )
            axs[i].vlines(mu + std, ymin, ymax, color="red", linestyles="dashed")
            axs[i].set_xlim((0, max_x))
            axs[i].set_ylim([ymin, ymax])
        else:
            axs[i].set_ylabel("Counts")
            axs[i].bar(
                label, counts, alpha=0.4, color=color, edgecolor=color, linewidth=2
            )
            axs[i].plot(
                label, gaussian * len(results), color="darkgreen", label="normal distr."
            )
            axs[i].vlines(mu, 0, np.max(counts), color="magenta", label="mu")
            axs[i].vlines(
                mu - std,
                0,
                np.max(counts),
                color="red",
                linestyles="dashed",
                label="sigma",
            )
            axs[i].vlines(mu + std, 0, np.max(counts), color="red", linestyles="dashed")
            axs[i].set_xlim((0, max_x))

        axs[i].legend()

    fig.tight_layout()
    plt.show()
    return


def plot_standard_distributions(results_list, n_dice_list):
    n_plots = len(results_list)
    figlength = 4 * n_plots
    fig, axs = plt.subplots(n_plots, figsize=(8, figlength))
    for i, results in enumerate(results_list):
        # label, counts = np.unique(results, return_counts=True)
        mu, std = norm.fit(np.asarray(results))
        z = (results - mu) / std
        new_mu, new_std = norm.fit(np.asarray(z))
        print("n_dice = ", n_dice_list[i])
        print("mu (0) = ", new_mu)
        print("std (1) = ", new_std)
        print("----")
        xmin, xmax = -4, 4
        ymin, ymax = 0, 0.6
        x = np.linspace(xmin, xmax, len(results))
        gaussian = norm.pdf(x, 0, 1)
        color = "teal"
        axs[i].set_title(f"Standardized Distribution for {len(results)} rolls")
        axs[i].set_ylabel("Probability density")
        axs[i].hist(
            z,
            range=(xmin, xmax),
            density=True,
            alpha=0.4,
            color=color,
            edgecolor=color,
            linewidth=2,
        )
        axs[i].plot(x, gaussian, color="darkgreen", label="normal distr. (mu=0, sig=1)")
        axs[i].legend()
        axs[i].set_xlim([xmin, xmax])
        axs[i].set_ylim([ymin, ymax])

    fig.tight_layout()
    plt.show()
    return
