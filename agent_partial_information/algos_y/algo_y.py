from agent_partial_information.algos_on_x.algo_on_x import AlgoOnX


class AlgoY(AlgoOnX):
    """An algo that computes `y_`."""

    def __init__(self):
        super().__init__()
        self.y_ = None

    def _receive_new_value(self, x, t):
        """Updates `y_` if necessary."""
        raise NotImplementedError
