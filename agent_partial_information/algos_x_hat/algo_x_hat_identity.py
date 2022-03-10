from agent_partial_information.algos_x_hat.algo_x_hat import AlgoXHat


class AlgoXHatIdentity(AlgoXHat):
    """A trivial algorithm that just stores `x` as `x_hat_`."""

    def _receive_new_value(self, x, t):
        self.x_hat_ = x
