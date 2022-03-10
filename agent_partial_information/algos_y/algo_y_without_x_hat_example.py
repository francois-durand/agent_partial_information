from agent_partial_information.algos_y.algo_y import AlgoY
from agent_partial_information.algos_misc.algo_sign_x import AlgoSignX


class AlgoYWithoutXHatExample(AlgoY):
    """An example of algorithm that does not rely on some `x_hat_` (estimation of `x`).

    ... But it is based directly on a different kind of measure, here the sign of `x` for example.

    Examples
    --------
        >>> measurer_x = AlgoSignX()
        >>> algo_y = AlgoYWithoutXHatExample(measurer_x)
        >>> algo_y(x=12, t=0).y_
        'Some value based on the fact that x > 0'
    """

    def __init__(self, algo_sign_x: AlgoSignX = None):
        super().__init__()
        if algo_sign_x is None:
            algo_sign_x = AlgoSignX()
        self.algo_sign_x = algo_sign_x

    def _receive_new_value(self, x, t):
        self.algo_sign_x(x, t)
        if self.algo_sign_x.sign_x_ == 1:
            self.y_ = "Some value based on the fact that x > 0"
        else:
            self.y_ = "Some value based on the fact that x <= 0"
