from agent_partial_information.algos_x_hat.algo_x_hat_periodic import AlgoXHatPeriodic


class EstimatorXPeriodicExact(AlgoXHatPeriodic):
    """
    Examples
    --------
        >>> algo_on_x = EstimatorXPeriodicExact(period=2)
        >>> algo_on_x(x=12, t=0).x_hat_
        12
        >>> algo_on_x(x=51, t=1).x_hat_
        12
        >>> algo_on_x(x=18, t=2).x_hat_
        18
    """

    def _receive_new_value_aux(self, x, t):
        self.x_hat_ = x
