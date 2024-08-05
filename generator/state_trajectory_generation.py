import numpy as np
from generator.trajectory_generator import Generator
from config.parameter_carrier import ParameterCarrier


class StateGeneration:

    def __init__(self, cc: ParameterCarrier):
        self.cc = cc

    def generate_trajectories(self, markov_model):
        generator1 = Generator(self.cc)
        generator1.load_generator(markov_model)
        number = self.cc.trajectory_number_to_generate
        usable_trajectory_list = generator1.generate_many(number, neighbor_check=False)
        print('State generation complete')
        real_trajectory_list = self.trans_many_usable_trajectories(usable_trajectory_list, markov_model.grid)
        return real_trajectory_list

    # this function transfers a usable state trajectory to real state trajectory
    def trans_to_real_state_trajectory(self, usable_to_real_dict: np.ndarray, usable_state_trajectory: np.ndarray):
        real_state_trajectory = usable_to_real_dict[usable_state_trajectory]
        return real_state_trajectory

    # this function transfers a list of usable state trajectory to real state trajectory
    def trans_many_usable_trajectories(self, usable_state_trajectories: list, grid1) -> list:
        usable_to_real_dict = grid1.usable_subcell_index_to_real_index_dict
        tr_list2 = []
        for usable_trajectory in usable_state_trajectories:
            real_trajectory = self.trans_to_real_state_trajectory(usable_to_real_dict, usable_trajectory)
            tr_list2.append(real_trajectory)
        return tr_list2