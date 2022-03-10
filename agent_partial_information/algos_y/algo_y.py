from agent_partial_information.algo_on_x import AlgoOnX


class AlgoY(AlgoOnX):
    """An algo that computes `y_`.

    In a real package, the documentation here states exactly what type of object is `y_`, what are the possible
    exceptions, etc.
    """

    def __init__(self):
        super().__init__()
        self.y_ = None

    def _receive_new_value(self, x, t):
        """Updates `y_` if necessary."""
        raise NotImplementedError
