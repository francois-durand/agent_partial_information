import numpy as np
from agent_partial_information.algos_y.algo_y import AlgoY
from agent_partial_information.algos_misc.algo_history_x_hat import AlgoHistoryXHat
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise


class AlgoYBasedOnHistoryExample(AlgoY):
    """An example of algorithm for `y_`, based on the history of values of some `x_hat_`.

    For this example, return the sum of the last two values of `x_hat_`. For `t = 0`, return twice the initial value
    of `x` for consistency.

    Examples
    --------
        >>> np.random.seed(42)
        >>> measurer_x = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> recorder_of_measures_x = AlgoHistoryXHat(measurer_x)
        >>> algo_y = AlgoYBasedOnHistoryExample(recorder_of_measures_x)
        >>> algo_y(x=12, t=0).y_
        24.993428306022466
        >>> algo_y(x=18, t=1).y_
        30.35844985184005
    """

    def __init__(self, algo_history_x_hat: AlgoHistoryXHat):
        super().__init__()
        self.algo_history_x_hat = algo_history_x_hat

    def _receive_new_value(self, x, t):
        history = self.algo_history_x_hat(x, t).history_
        if t == 0:
            self.y_ = 2 * history[0]
        else:
            self.y_ = history[t - 1] + history[t]
