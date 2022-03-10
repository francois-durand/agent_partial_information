from agent_partial_information.algos_x_hat.algo_x_hat_periodic import AlgoXHatPeriodic
from agent_partial_information.algos_x_hat.algo_x_hat_periodic_exact import EstimatorXPeriodicExact


class EstimatorXBasedOnPeriodicExample(AlgoXHatPeriodic):
    """Exponential moving average.

    Examples
    --------
        >>> algo_x_hat = EstimatorXBasedOnPeriodicExample(
        ...     update_ratio=.5,
        ...     sub_algo_x_hat_periodic=EstimatorXPeriodicExact(period=2)
        ... )
        >>> algo_x_hat(x=12, t=0)  # doctest: +ELLIPSIS
        <...>
        >>> algo_x_hat.x_hat_
        12
        >>> algo_x_hat(x=2022, t=1).x_hat_
        12
        >>> algo_x_hat(x=18, t=2).x_hat_
        15.0
        >>> algo_x_hat(x=2023, t=3).x_hat_
        15.0
        >>> algo_x_hat(x=18, t=4).x_hat_
        16.5
    """

    def __init__(self, update_ratio, sub_algo_x_hat_periodic: AlgoXHatPeriodic):
        super().__init__(period=sub_algo_x_hat_periodic.period)
        self.update_ratio = update_ratio
        self.sub_algo_x_hat_periodic = sub_algo_x_hat_periodic

    def _receive_new_value_aux(self, x, t):
        self.sub_algo_x_hat_periodic(x, t)
        if t == 0:
            self.x_hat_ = self.sub_algo_x_hat_periodic.x_hat_
        else:
            self.x_hat_ = self.update_ratio * self.sub_algo_x_hat_periodic.x_hat_ + (1 - self.update_ratio) * self.x_hat_
