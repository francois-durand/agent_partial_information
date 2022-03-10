from agent_partial_information.algo_on_x import AlgoOnX


class AlgoZ(AlgoOnX):
    """An algo that computes `z_`.

    In a real package, the documentation here states exactly what type of object is `z_`, what are the possible
    exceptions, etc.
    """

    def __init__(self):
        super().__init__()
        self.z_ = None

    def _receive_new_value(self, x, t):
        """Updates `z_` if necessary."""
        raise NotImplementedError
