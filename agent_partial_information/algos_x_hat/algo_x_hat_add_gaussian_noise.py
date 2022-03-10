import numpy as np
from agent_partial_information.algos_x_hat.algo_x_hat import AlgoXHat


class AlgoXHatAddGaussianNoise(AlgoXHat):
    """Add a Gaussian noise to `x`.

    Parameters
    ----------
    noise_intensity: float
        The intensity (scaling) of the Gaussian noise.

    Examples
    --------
        >>> np.random.seed(42)
        >>> algo = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> algo(x=12, t=0).x_hat_
        12.496714153011233

    If, for some reasons, we give again the value for t == 0, nothing bad happens, you will simply get the same
    value:

        >>> algo(x=12, t=0).x_hat_
        12.496714153011233

    Now, let us give the value of `x` for the next time slot:

        >>> algo(x=51, t=1).x_hat_
        50.86173569882882
    """

    def __init__(self, noise_intensity: float):
        super().__init__()
        self.noise_intensity = noise_intensity

    def _receive_new_value(self, x, t):
        self.x_hat_ = x + self.noise_intensity * np.random.randn()
