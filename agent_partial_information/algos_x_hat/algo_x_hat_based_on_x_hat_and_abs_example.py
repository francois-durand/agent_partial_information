import numpy as np

from agent_partial_information.algos_x_hat.algo_x_hat import AlgoXHat
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise
from agent_partial_information.algos_misc.algo_abs_x import AlgoAbsX


class AlgoXHatBasedOnXHatAndAbsExample(AlgoXHat):
    """An example of algorithm that is based on two other algorithms.

    Here we try to recover the value of `x`, based on another `x_hat_` (which will give the
    correct sign if we are lucky) and the exact absolute value of `x`.

    Parameters
    ----------
    sub_algo_x_hat: AlgoXHat
        An algo that computes a `x_hat_` (a value of the same type as `x`).
    algo_on_x_abs: AlgoAbsX
        Default: AlgoOnXAbs().

    Examples
    --------
    Assume that you are able to measure the absolute value of `x`, and a noisy version of `x` (with sign):

        >>> np.random.seed(42)
        >>> measurer_x_abs = AlgoAbsX()
        >>> measurer_x_noisy = AlgoXHatAddGaussianNoise(noise_intensity=1.)

    Then you may want to recover the value of `x` by this composition:

        >>> estimate_x = AlgoXHatBasedOnXHatAndAbsExample(
        ...     sub_algo_x_hat=measurer_x_noisy,
        ...     algo_on_x_abs=measurer_x_abs
        ... )

    Now, let us see what happens when we feed the algorithm:

        >>> estimate_x(x=-12, t=0)  # doctest: +ELLIPSIS
        <...>

    We have the measures:

        >>> measurer_x_abs.abs_x_
        12
        >>> measurer_x_noisy.x_hat_
        -11.503285846988767

    And the estimation of `x` is:

        >>> estimate_x.x_hat_
        -12.0
    """

    def __init__(self, sub_algo_x_hat: AlgoXHat, algo_on_x_abs: AlgoAbsX = None):
        super().__init__()
        self.sub_algo_x_hat = sub_algo_x_hat
        if algo_on_x_abs is None:
            algo_on_x_abs = AlgoAbsX()
        self.algo_on_x_abs = algo_on_x_abs

    def _receive_new_value(self, x, t):
        self.sub_algo_x_hat(x, t)
        self.algo_on_x_abs(x, t)
        sign_x_hat_ = np.sign(self.sub_algo_x_hat.x_hat_)
        self.x_hat_ = sign_x_hat_ * self.algo_on_x_abs.abs_x_
