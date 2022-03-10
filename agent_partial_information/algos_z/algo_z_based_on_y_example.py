from agent_partial_information.algos_x_hat.algo_x_hat_identity import AlgoXHatIdentity
from agent_partial_information.algos_y.algo_y import AlgoY
from agent_partial_information.algos_y.algo_y_based_on_x_hat_example import AlgoYBasedOnXHatExample
from agent_partial_information.algos_z.algo_z import AlgoZ


class AlgoZBasedOnYExample(AlgoZ):
    """Example of algo for `z_` based on the value of `y_`.

    Parameters
    ----------
    algo_y: AlgoY
        The algo for computing `y_`.

    Examples
    --------
        >>> algo_y = AlgoYBasedOnXHatExample(algo_x_hat=AlgoXHatIdentity())
        >>> algo_z = AlgoZBasedOnYExample(algo_y)
        >>> algo_z(x=12, t=0).z_
        Long computation...
        'Some value of `z` based on y=24'

    We can check the value for `y`:

        >>> algo_y.y_
        24
    """

    def __init__(self, algo_y: AlgoY):
        super().__init__()
        self.algo_y = algo_y

    def _receive_new_value(self, x, t):
        y = self.algo_y(x, t).y_
        self.z_ = f"Some value of `z` based on {y=}"
