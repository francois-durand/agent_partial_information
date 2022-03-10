from agent_partial_information.algos_x_hat.algo_x_hat_periodic_exact import EstimatorXPeriodicExact


class EstimatorXExact(EstimatorXPeriodicExact):
    """Just a common shortcut..."""

    def __init__(self):
        super().__init__(period=1)
