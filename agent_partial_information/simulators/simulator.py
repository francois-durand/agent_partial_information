import numpy as np
from agent_partial_information.algos_y.algo_y_based_on_history_example import AlgoYBasedOnHistoryExample
from agent_partial_information.algos_z.algo_z_based_on_history_example import AlgoZBasedOnHistoryExample
from agent_partial_information.algos_misc.algo_history_x_hat import AlgoHistoryXHat
from agent_partial_information.algos_x_hat.algo_x_hat_add_gaussian_noise import AlgoXHatAddGaussianNoise
from agent_partial_information.agents.agent_delegate_algos import AgentDelegateAlgos


class Simulator:
    """Simulator of the whole system.

    At each time slot, the value of `x` is generated. Then the agent computes `y_` and `z_`. Then the performance
    of the system is evaluated, depending on `x`, `y_` and `z_`.

    Examples
    --------
        >>> np.random.seed(42)
        >>> measurer_x = AlgoXHatAddGaussianNoise(noise_intensity=1.)
        >>> recorder_measures_x = AlgoHistoryXHat(measurer_x)
        >>> algo_y = AlgoYBasedOnHistoryExample(recorder_measures_x)
        >>> algo_z = AlgoZBasedOnHistoryExample(recorder_measures_x)
        >>> agent = AgentDelegateAlgos(algo_y, algo_z)
        >>> simulator = Simulator(n_time_slots=5, agent=agent)
        >>> simulator.run()
        Evaluate performance depending on x=-1.254598811526375, y=-4.732957859146591, z=5.600222524114371.
        Evaluate performance depending on x=-3.4400547966379733, y=-5.4876315415218855, z=7.386141892158995.
        Evaluate performance depending on x=-4.419163878318005, y=-7.261275198066458, z=12.921954423449135.
        Evaluate performance depending on x=2.0807257779604544, y=-1.0488815233508868, z=-12.79811694309658.
        Evaluate performance depending on x=-4.7941550570419755, y=-2.2837921282985096, z=-16.615523313957084.
    """

    def __init__(self, n_time_slots, agent):
        self.n_time_slots = n_time_slots
        self.agent = agent

    def run(self):
        for t in range(self.n_time_slots):
            x = np.random.rand() * 10 - 5
            self.agent(x, t)
            y = self.agent.y_
            z = self.agent.z_
            print(f"Evaluate performance depending on {x=}, {y=}, {z=}.")
