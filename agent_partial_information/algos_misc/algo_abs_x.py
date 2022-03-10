from agent_partial_information.algo_on_x import AlgoOnX


class AlgoAbsX(AlgoOnX):
    """Compute the absolute value of current `x`.

    Examples
    --------
        >>> algo = AlgoAbsX()
        >>> algo(x=-12, t=0)  # doctest: +ELLIPSIS
        <...>
        >>> algo.abs_x_
        12

    Note that you are *not* supposed to give a different value of `x` for the same time slot `t`. If you do,
    bad behavior will occur:

        >>> algo(x=42, t=0)  # doctest: +ELLIPSIS
        <...>
        >>> algo.abs_x_
        12

    Here is why: for performance reasons, when you give the same `t` again, the object only checks that `t` is
    the same as in the previous call and avoids computing again its results, but it does not check whether the
    new `x` value (42) is equal to the previous `x` value (12).

    Let us finish with an example of the next time slot (also note the one-liner instruction):

        >>> algo(x=51, t=1).abs_x_
        51
    """

    def __init__(self):
        super().__init__()
        self.abs_x_ = None
        # Number: Absolute value of current `x`.

    def _receive_new_value(self, x, t):
        self.abs_x_ = abs(x)
