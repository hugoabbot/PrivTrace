import config.folder_and_file_names as fname
from discretization.get_discretization import DiscretizationData
from primarkov.build_markov_model import ModelBuilder
from generator.state_trajectory_generation import StateGeneration
from generator.to_real_translator import RealLocationTranslator
from config.parameter_carrier import ParameterCarrier
from config.parameter_setter import ParameterSetter
from tools.data_writer import DataWriter
from data_preparation.data_preparer import DataPreparer
import datetime


if __name__ == "__main__":
    writer = DataWriter()

    print('Starting PrivTrace Algorithm')
    print(datetime.datetime.now())

    # Parameters stored
    parameter_setter = ParameterSetter().set_up_args() 
    parameter_carrier = ParameterCarrier(parameter_setter) 
    
    # Trajectories intialized into list
    data_preparer = DataPreparer(parameter_carrier)
    trajectory_set = data_preparer.get_trajectory_set()

    # 1. 2-Layer discretization
    discretization_data = DiscretizationData(parameter_carrier)
    grid = discretization_data.get_discrete_data(trajectory_set)

    # 2. Model learning and trip distribution estimation
    model_builder = ModelBuilder(parameter_carrier)
    model = model_builder.build_model(grid, trajectory_set)
    model_builder = ModelBuilder(parameter_carrier)
    model = model_builder.filter_model(trajectory_set, grid, model)

    # 3. Trajectory generation with state prediction
    state_generation = StateGeneration(parameter_carrier)
    synthetic_trajectory_list = state_generation.generate_trajectories(model)

    # Mapping states to real coordinates
    rlt = RealLocationTranslator(parameter_carrier)
    real_trajectory_list = rlt.translate_trajectories(grid, synthetic_trajectory_list)
    writer.save_trajectory_data_in_list_to_file(real_trajectory_list, fname.result_file_name)

    print('Ending PrivTrace Algorithm')
    print(datetime.datetime.now())

    pass
