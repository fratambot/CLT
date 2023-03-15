import bisect
import numpy as np
import random

from itertools import accumulate


class Die:
    def __init__(self, weights=None):
        if weights is None:
            weights = np.full(6, 1.0 / 6.0)
        if len(weights) != 6:
            raise ValueError(
                "You must give exactly 6 weights since we are \
                considering only dice with 6 sides"
            )
        if round(sum(weights), 10) != 1:
            raise ValueError(
                f"The sum of weights (rounded to the 10th decimal place) \
                must be 1. It was: {round(sum(weights), 10)}"
            )
        self.weights = weights
        self.cumulative_weights = self.compute_cumulative(weights)

    def compute_cumulative(self, weights):
        cumulative_weights = list(accumulate(weights))
        return cumulative_weights

    def roll(self, times=1):
        results = []
        for i in range(times):
            results.append(bisect.bisect(self.cumulative_weights, random.random()) + 1)
        return results
