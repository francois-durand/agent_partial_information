class AlgoOnX:
    """An algo that updates its results when a new value of `x` occurs.

    The outputs of the algo are stored in attributes whose names end with an underscore, like `my_result_`.
    Note that these attributes will not have any meaningful value before the `AlgoOnX` object is called.

    Examples
    --------
        Cf. :class:`AlgoAbsX`.
    """

    def __init__(self):
        self.last_t_recorded = -1

    def __call__(self, x, t):
        """Update the results, unless `t` is the same as in the previous call.

        Parameters
        ----------
        x: Number
            The value of `x` at time `t`.
        t: int
            Time slot.
        """
        if t != self.last_t_recorded:
            self.last_t_recorded = t
            self._receive_new_value(x, t)
        return self

    def _receive_new_value(self, x, t):
        """Update the results. Here we can assume that `t` is not the same as in the previous call.

        Parameters
        ----------
        x: Number
            The value of `x` at time `t`.
        t: int
            Time slot.
        """
        raise NotImplementedError
