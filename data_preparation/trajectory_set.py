import numpy as np
from data_preparation.trajectory import Trajectory


class TrajectorySet:

    def __init__(self):
        self.trajectory_list = []
        self.trajectory_number = 0

    # Updates 'trajectory_number', which is the size of the trajectory list
    def refresh_trajectory_number(self):
        self.trajectory_number = len(self.trajectory_list)

    # Returns 'trajectory_number'
    def get_trajectory_number(self):
        return self.trajectory_number

    # Updates 'trajectory_list' with an inputted list of trajectories
    def give_trajectory_list(self, trajectory_list_input):
        if not isinstance(trajectory_list_input, list):
            raise TypeError('TrajectorySet must receive a list of trajectories as the parameter')
        self.trajectory_list += trajectory_list_input
        self.refresh_trajectory_number()

    # Add a new singular trajectory into 'traject_list'
    def add_trajectory(self, trajectory, give_index=True):
        sample = Trajectory()
        if type(sample) is not type(trajectory):
            raise TypeError('Must add trajectory to set')
        current_trajectory_number = self.get_trajectory_number()
        if give_index:
            trajectory.give_index(current_trajectory_number + 1)
        self.trajectory_list.append(trajectory)
        self.refresh_trajectory_number()

    # Returns the trajectory at the input index
    def give_trajectory_by_index(self, index) -> Trajectory:
        try:
            trajectory = self.trajectory_list[index]
        except IndexError:
            print(index)
            raise IndexError

        return trajectory

    # this function calculate all point number in this trajectory set
    def get_whole_point_number(self) -> int:
        point_number = 0
        trajectory_number = self.get_trajectory_number()
        for trajectory_index in range(trajectory_number):
            trajectory1 = self.give_trajectory_by_index(trajectory_index)
            this_trajectory_point_number = trajectory1.get_point_number()
            point_number = point_number + this_trajectory_point_number
        return point_number

    # this function gives discrete trajectory the sample trajectory (unrepeated cell index array and its frequency)
    def get_simple_trajectory(self, dict1: np.ndarray):
        for trajectory in self.trajectory_list:
            trajectory.give_simple_trajectory(dict1)
