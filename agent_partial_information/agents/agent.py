from agent_partial_information.algo_on_x import AlgoOnX


class Agent(AlgoOnX):
    """An agent that computes `y_` and `z_`."""

    def __init__(self):
        super().__init__()
        self.y_ = None
        self.z_ = None

    def _receive_new_value(self, x, t):
        """Updates `y_` and `z_` if necessary."""
        raise NotImplementedError
