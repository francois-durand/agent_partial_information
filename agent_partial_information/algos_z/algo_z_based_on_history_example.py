import numpy as np
from agent_partial_information.algos_z.algo_z import AlgoZ
from agent_partial_information.algos_on_x.algo_on_x_history_x_hat import AlgoOnXHistoryXHat
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise


class AlgoZBasedOnHistoryExample(AlgoZ):
    """An example of algorithm for `z_`, based on the history of values of some `x_hat_`

    For this example, return the product of the last two values of `x_hat_`. For `t = 0`, return the square of
    the initial value of `x` for consistency.

    Examples
    --------
        >>> np.random.seed(42)
        >>> measurer_x = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> recorder_of_measures_x = AlgoOnXHistoryXHat(algo_x_hat=measurer_x)
        >>> algo_z = AlgoZBasedOnHistoryExample(recorder_of_measures_x)
        >>> algo_z(x=12, t=0).z_
        156.16786462207125
        >>> algo_z(x=18, t=1).z_
        223.21300530490007
    """

    def __init__(self, algo_on_x_history_x_hat: AlgoOnXHistoryXHat):
        super().__init__()
        self.algo_on_x_history_x_hat = algo_on_x_history_x_hat

    def _receive_new_value(self, x, t):
        history = self.algo_on_x_history_x_hat(x, t).history_
        if t == 0:
            self.z_ = history[0] ** 2
        else:
            self.z_ = history[t - 1] * history[t]
