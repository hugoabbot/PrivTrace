from primarkov.mar_model import MarkovModel
from config.parameter_carrier import ParameterCarrier
from data_preparation.trajectory_set import TrajectorySet
from discretization.grid import Grid


class ModelBuilder:

    def __init__(self, cc: ParameterCarrier):
        self.cc = cc

    def build_model(self, grid: Grid, trajectory_set: TrajectorySet):
        model = MarkovModel(self.cc)
        model.model_building(trajectory_set, grid)
        return model

    def filter_model(self, trajectory_set, grid, model):
        model.model_filtering(trajectory_set, grid)
        return model