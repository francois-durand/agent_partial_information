import numpy as np
from agent_partial_information.algos_y.algo_y import AlgoY
from agent_partial_information.algos_x_hat.algo_x_hat import AlgoXHat
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise


class AlgoYBasedOnXHatExample(AlgoY):
    """An example of algorithm for `y_` based on some `x_hat_`.

    For this example, `y_` is simply twice `x_hat_`.

    Examples
    --------
        >>> np.random.seed(42)
        >>> measurer_x = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> algo_y = AlgoYBasedOnXHatExample(measurer_x)
        >>> algo_y(x=12, t=0).y_
        Long computation...
        24.993428306022466

    If we give the value of `x` again for the same time slot, the value is not computed again:

        >>> algo_y(x=12, t=0).y_
        24.993428306022466
    """

    def __init__(self, algo_x_hat: AlgoXHat):
        super().__init__()
        self.algo_x_hat = algo_x_hat

    def _receive_new_value(self, x, t):
        print('Long computation...')
        self.y_ = 2 * self.algo_x_hat(x, t).x_hat_
