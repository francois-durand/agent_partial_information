from agent_partial_information.algos_x_hat.algo_x_hat import AlgoXHat


class AlgoXHatPeriodic(AlgoXHat):

    def __init__(self, period: int):
        super().__init__()
        self.period = period

    def _receive_new_value(self, x, t):
        if t % self.period == 0:
            self._receive_new_value_aux(x, t)

    def _receive_new_value_aux(self, x, t):
        """Here, t can be assumed to be a multiple of the period."""
        raise NotImplementedError
