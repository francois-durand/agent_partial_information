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

    def __init__(self, algo_on_x_sign: AlgoSignX = None):
        super().__init__()
        if algo_on_x_sign is None:
            algo_on_x_sign = AlgoSignX()
        self.algo_on_x_sign = algo_on_x_sign

    def _receive_new_value(self, x, t):
        self.algo_on_x_sign(x, t)
        if self.algo_on_x_sign.sign_x_ == 1:
            self.y_ = "Some value based on the fact that x > 0"
        else:
            self.y_ = "Some value based on the fact that x <= 0"
