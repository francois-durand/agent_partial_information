import numpy as np
from agent_partial_information.algos_on_x.algo_on_x import AlgoOnX


class AlgoOnXSign(AlgoOnX):
    """Compute the sign of current `x`.

    Examples
    --------
        >>> algo = AlgoOnXSign()
        >>> algo(x=-12, t=0).sign_x_
        -1
    """

    def __init__(self):
        super().__init__()
        self.sign_x_ = None
        # int: Sign of current `x`.

    def _receive_new_value(self, x, t):
        self.sign_x_ = np.sign(x)
