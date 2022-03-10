import numpy as np
from agent_partial_information.agents.agent import Agent
from agent_partial_information.algos_y.algo_y import AlgoY
from agent_partial_information.algos_y.algo_y_based_on_history_example import AlgoYBasedOnHistoryExample
from agent_partial_information.algos_z.algo_z import AlgoZ
from agent_partial_information.algos_z.algo_z_based_on_history_example import AlgoZBasedOnHistoryExample
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise
from agent_partial_information.algos_on_x.algo_on_x_history_x_hat import AlgoOnXHistoryXHat
from agent_partial_information.algos_y.algo_y_based_on_x_hat_example import AlgoYBasedOnXHatExample
from agent_partial_information.algos_z.algo_z_based_on_y_example import AlgoZBasedOnYExample
from agent_partial_information.algos_x_hat.algo_x_hat_exact import AlgoXHatExact


class AgentDelegateAlgos(Agent):
    """Generic agent that delegates the task to an `AlgoY` and an `AlgoZ`.

    Examples
    --------
    Define our compositions:

        >>> measurer_x = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> recorder_measures_x = AlgoOnXHistoryXHat(measurer_x)
        >>> algo_y = AlgoYBasedOnHistoryExample(recorder_measures_x)
        >>> algo_z = AlgoZBasedOnHistoryExample(recorder_measures_x)
        >>> agent = AgentDelegateAlgos(algo_y, algo_z)

    And here we go:

        >>> np.random.seed(42)
        >>> agent(x=12, t=0)  # doctest: +ELLIPSIS
        <...>
        >>> agent.y_
        24.993428306022466
        >>> agent.z_
        156.16786462207125

    In the setting above, note that the algos for `y` and `z` share the same measures and the same history
    (which is generally desired):

        >>> algo_y.algo_on_x_history_x_hat.history_
        {0: 12.496714153011233}
        >>> algo_z.algo_on_x_history_x_hat.history_
        {0: 12.496714153011233}

    However, in principle, it is also possible to model a situation where each algorithm has its own measures
    (and history) of `x_hat_`:

        >>> measurer_x_for_y = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> measurer_x_for_z = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> recorder_measures_x_for_y = AlgoOnXHistoryXHat(measurer_x_for_y)
        >>> recorder_measures_x_for_z = AlgoOnXHistoryXHat(measurer_x_for_z)
        >>> algo_y = AlgoYBasedOnHistoryExample(recorder_measures_x_for_y)
        >>> algo_z = AlgoZBasedOnHistoryExample(recorder_measures_x_for_z)
        >>> agent = AgentDelegateAlgos(algo_y, algo_z)

    And here we go again:

        >>> np.random.seed(42)
        >>> agent(x=12, t=0)  # doctest: +ELLIPSIS
        <...>
        >>> agent.y_
        24.993428306022466
        >>> agent.z_
        140.70077378886992

    The same can be achieved with some big composition, like this:

        >>> agent = AgentDelegateAlgos(
        ...     algo_y=AlgoYBasedOnHistoryExample(
        ...         algo_on_x_history_x_hat=AlgoOnXHistoryXHat(
        ...             algo_x_hat=AlgoXHatAddGaussianNoise(noise_intensity=1.)
        ...         )
        ...     ),
        ...     algo_z=AlgoZBasedOnHistoryExample(
        ...         algo_on_x_history_x_hat=AlgoOnXHistoryXHat(
        ...             algo_x_hat=AlgoXHatAddGaussianNoise(noise_intensity=1.)
        ...         )
        ...     )
        ... )

    The algorithms do not need to be "independent". For example, the algorithm for `z` can be based on the
    computation of `y`:

        >>> measurer_x = AlgoXHatExact()
        >>> algo_y = AlgoYBasedOnXHatExample(measurer_x)
        >>> algo_z = AlgoZBasedOnYExample(algo_y)
        >>> agent = AgentDelegateAlgos(algo_y, algo_z)
        >>> agent(x=12, t=0)  # doctest: +ELLIPSIS
        Long computation...
        <...>
        >>> agent.y_
        24
        >>> agent.z_
        'Some value of `z` based on y=24'
    """

    def __init__(self, algo_y: AlgoY, algo_z: AlgoZ):
        super().__init__()
        self.algo_y = algo_y
        self.algo_z = algo_z

    def _receive_new_value(self, x, t):
        self.y_ = self.algo_y(x, t).y_
        self.z_ = self.algo_z(x, t).z_
