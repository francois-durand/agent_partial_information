from agent_partial_information.algo_on_x import AlgoOnX


class AlgoSeveralOutputsExample(AlgoOnX):
    """Compute several outputs based on the current `x`.

    For this example, we compute the square and the sube of current `x`.

    Examples
    --------
    Basic usage:

        >>> algo = AlgoSeveralOutputsExample()
        >>> algo(x=12, t=0)  # doctest: +ELLIPSIS
        Potentially long computation...
        <...>
        >>> algo.x_square_
        144
        >>> algo.x_cube_
        1728

    Note that even if you use the one-liner syntax, and even if you pass the arguments each time, the computation
    is only performed once:

        >>> algo = AlgoSeveralOutputsExample()
        >>> algo(x=12, t=0).x_square_
        Potentially long computation...
        144
        >>> algo(x=12, t=0).x_cube_
        1728
    """

    def __init__(self):
        super().__init__()
        self.x_square_ = None
        # Number: Square of current `x`.
        self.x_cube_ = None
        # Number: Cube of current `x`.

    def _receive_new_value(self, x, t):
        print("Potentially long computation...")
        self.x_square_ = x**2
        self.x_cube_ = x**3
