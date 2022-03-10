from agent_partial_information.algos_on_x.algo_on_x import AlgoOnX


class AlgoZ(AlgoOnX):

    def __init__(self):
        super().__init__()
        self.z_ = None

    def _receive_new_value(self, x, t):
        """Updates `z_` if necessary."""
        raise NotImplementedError
