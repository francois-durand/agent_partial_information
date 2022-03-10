import numpy as np
from agent_partial_information.algos_misc.algo_history_x_hat import AlgoHistoryXHat
from agent_partial_information.algos_x_hat.algo_x_hat import AlgoXHat
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise


class AlgoXHatLinearRegression(AlgoXHat):
    """Perform a linear regression over history values of `x_hat_`.

    Examples
    --------
    Suppose that we are able to measure a noisy version of `x`:

        >>> measurer_x = AlgoXHatAddGaussianNoise(noise_intensity=1.)

    We can record the history of these noisy values:

        >>> recorder_of_measures_x = AlgoHistoryXHat(measurer_x)

    We can then compose with a linear regression to estimate `x`:

        >>> estimator_x = AlgoXHatLinearRegression(recorder_of_measures_x)

    Here we go:

        >>> np.random.seed(42)
        >>> for t in range(101):
        ...     _ = estimator_x(x=t, t=t)
        >>> estimator_x.x_hat_
        99.91258983110032

    Note that this value is better than the last measure, which is:

        >>> measurer_x.x_hat_
        98.58462925794959
    """

    def __init__(self, algo_on_x_history_x_hat: AlgoHistoryXHat):
        super().__init__()
        self.algo_on_x_history_x_hat = algo_on_x_history_x_hat

    def _receive_new_value(self, x, t):
        self.algo_on_x_history_x_hat(x, t)
        if t == 0:  # Because with only one value, linear regression is not defined.
            self.x_hat_ = self.algo_on_x_history_x_hat.history_[0]
            return
        history = self.algo_on_x_history_x_hat.history_
        fit = np.polyfit(list(history.keys()), list(history.values()), 1)
        poly = np.poly1d(fit)
        self.x_hat_ = poly(t)
