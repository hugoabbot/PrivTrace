from data_preparation.trajectory import Trajectory
from data_preparation.trajectory_set import TrajectorySet
from tools.data_reader import DataReader
from config.parameter_carrier import ParameterCarrier


class DataPreparer:

    def __init__(self, args):
        self.cc = args

    def get_trajectory_set(self):
        tr_set = TrajectorySet()
        data_reader = DataReader()
        tr_list = data_reader.read_trajectories_from_data_file(self.cc.dataset_file_name)
        for tr_array in tr_list:
            tr = Trajectory()
            tr.trajectory_array = tr_array
            tr_set.add_trajectory(tr)
        return tr_set
