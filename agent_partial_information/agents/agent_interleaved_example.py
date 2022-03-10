import numpy as np
from agent_partial_information.agents.agent import Agent
from agent_partial_information.algos_x_hat.algo_x_hat import AlgoXHat
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise


class AgentInterleavedExample(Agent):
    """Example of agent where the computations of `y_` and `z_` are interleaved (= share common steps).

    For this example, `y_ = x_hat_**2 - 1`, and `y_ = x_hat_**2 + 1`.

    Parameters
    ----------
    algo_x_hat: AlgoXHat
        An algo that computes `x_hat_` (a value of the same type as `x`).

    Examples
    --------
        >>> np.random.seed(42)
        >>> measurer_x = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> agent = AgentInterleavedExample(measurer_x)
        >>> agent(x=12, t=0)  # doctest: +ELLIPSIS
        Potentially long computation...
        <...>
        >>> agent.y_
        155.16786462207125
        >>> agent.z_
        157.16786462207125
    """

    def __init__(self, algo_x_hat):
        super().__init__()
        self.algo_x_hat = algo_x_hat

    def _receive_new_value(self, x, t):
        x_hat_ = self.algo_x_hat(x, t).x_hat_
        print("Potentially long computation...")
        x_hat_square = x_hat_ ** 2
        self.y_ = x_hat_square - 1
        self.z_ = x_hat_square + 1
