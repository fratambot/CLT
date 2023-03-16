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
        if round(sum(weights), 6) != 1:
            raise ValueError(
                f"The sum of weights (rounded to the 6th decimal place) \
                must be 1. It was: {round(sum(weights), 6)}"
            )
        self.weights = weights
        self.cumulative_probs = self._compute_cumulative(weights)

    def _compute_cumulative(self, weights):
        cumulative_probs = list(accumulate(weights))
        return cumulative_probs

    def roll(self, n_rolls=1, n_dice=1):
        """Roll n_dice for n_rolls times.
        If n_dice=1, returns the outcomes. For more than 1 die,
        it returns the sum of the dice outcomes.

        Parameters
        ----------
        n_rolls : int
            how many time the die or dice are rolled (the default is 1)
        n_dice : int
            the number of dice to roll (the default is 1)

        Returns
        -------
        IF n_dice == 1:
        results : list
            the outcomes of the rolls. The list contains integers between 1 and 6 and
            len(results) == n_rolls
        IF n_dice > 1:
            the sum of the outcomes of the n_dice. The list contains integers
            (larger as the number of dice increase) and len(results) == n_rolls

        Raises
        ------
        ValueError
            If n_dice < 1
        """
        results = []
        if n_dice < 1:
            raise ValueError("The minimum number of dice is 1")
        if n_dice == 1:
            for _ in range(n_rolls):
                results.append(
                    bisect.bisect(self.cumulative_probs, random.random()) + 1
                )
        else:
            for _ in range(n_rolls):
                dice_sum = 0
                for _ in range(n_dice):
                    dice_sum += (
                        bisect.bisect(self.cumulative_probs, random.random()) + 1
                    )
                results.append(dice_sum)

        return results
