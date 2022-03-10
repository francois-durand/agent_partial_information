from agent_partial_information.algos_y.algo_y import AlgoY


class AlgoYConstant(AlgoY):
    """An example of constant algorithm.

    Examples
    --------
        >>> algo_y = AlgoYConstant(y=42)
        >>> algo_y(x=12, t=0).y_
        42
    """

    def __init__(self, y):
        super().__init__()
        self.y_ = y

    def _receive_new_value(self, x, t):
        pass
