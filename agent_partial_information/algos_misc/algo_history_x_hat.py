import numpy as np
from agent_partial_information.algo_on_x import AlgoOnX
from agent_partial_information.algos_x_hat.algo_x_hat import AlgoXHat
from agent_partial_information.algos_x_hat.algo_x_hat_identity import AlgoXHatIdentity
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise


class AlgoHistoryXHat(AlgoOnX):
    """Records a history of values of `x_hat_`.

    Parameters
    ----------
    algo_x_hat: AlgoXHat
        An algo that computes `x_hat_` (a value of the same type as `x`).

    Examples
    --------
    The simplest use case is to record the *exact* values of `x`:

        >>> algo = AlgoHistoryXHat(algo_x_hat=AlgoXHatIdentity())
        >>> algo(x=12, t=0)  # doctest: +ELLIPSIS
        <...>
        >>> algo(x=51, t=1)  # doctest: +ELLIPSIS
        <...>
        >>> algo.history_
        {0: 12, 1: 51}

    But for example, we can also record noisy values of `x`:

        >>> np.random.seed(42)
        >>> algo = AlgoHistoryXHat(algo_x_hat=AlgoXHatAddGaussianNoise(noise_intensity=1.))
        >>> algo(x=12, t=0)  # doctest: +ELLIPSIS
        <...>
        >>> algo(x=51, t=1)  # doctest: +ELLIPSIS
        <...>
        >>> algo.history_
        {0: 12.496714153011233, 1: 50.86173569882882}
    """

    def __init__(self, algo_x_hat: AlgoXHat):
        super().__init__()
        self.algo_x_hat = algo_x_hat
        self.history_ = dict()
        # dict: Keys are time slots, values are the corresponding values of `x_hat_`.

    def _receive_new_value(self, x, t):
        self.history_[t] = self.algo_x_hat(x, t).x_hat_
