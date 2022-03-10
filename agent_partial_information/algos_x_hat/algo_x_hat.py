from agent_partial_information.algos_on_x.algo_on_x import AlgoOnX


class AlgoXHat(AlgoOnX):
    """An algo that computes `x_hat_`, something that "looks like" `x`.

    In particular, `x_hat_` must have the same type as `x`. In real applications of this
    "proof of concept package", where `x` will be a matrix, `x_hat_` should also have the same shape
    as `x` for example.
    """

    def __init__(self):
        super().__init__()
        self.x_hat_ = None

    def _receive_new_value(self, x, t):
        """Update `x_hat_` if necessary."""
        raise NotImplementedError
