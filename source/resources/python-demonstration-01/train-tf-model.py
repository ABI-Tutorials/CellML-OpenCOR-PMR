"""
MLP approximation for action potential of the ORd cardiac electrophysiology model.

@author: Gonzalo D. Maso Talou and David Nickerson
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import OpenCOR as oc

from MLP import MLP

def extract_samples_at_random(t_dataset, x_dataset, num_samples):
    random_idexes = np.random.choice(t_dataset.shape[0], num_samples, replace=False)
    t_training = t_dataset[random_idexes]
    x_training = x_dataset[random_idexes]

    return t_training, x_training

def train(NN,t_train,x_train):
    x_node = tf.placeholder(tf.float32, shape=[None, 1],name="x")
    #   Mean square loss function
    NN.loss_function = tf.reduce_sum(tf.square(NN.Y[0] - x_node))
    NN.optimizer = tf.contrib.opt.ScipyOptimizerInterface(NN.loss_function,
                                                       var_list=NN.weights + NN.biases,
                                                       method='L-BFGS-B',
                                                       options={'maxiter': 50000,
                                                                'maxfun': 50000,
                                                                'maxcor': 100,
                                                                'maxls': 100,
                                                                'ftol': 1.0 * np.finfo(float).eps})

    NN.session = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                                                  device_count={'GPU': 0},
                                                  log_device_placement=True))
    init = tf.global_variables_initializer()
    NN.session.run(init)
    NN.optimizer.minimize(NN.session,
                       feed_dict = {NN.X[0]: t_train[:,None], x_node: x_train[:,None]},
                       fetches = [NN.loss_function],
                       loss_callback = NN.loss_callback)




if __name__ == "__main__":

    #   Data generation or loading - This section can be replaced by more complex models for which we want to create a surrogate model.
    #v0 = 5                                                      # m/s
    #a  = 4                                                      # m/s^2
    #t_dataset = np.linspace(0,10,1001)                          # s
    #x_dataset = v0 * t_dataset + 0.5 * a * np.square(t_dataset) # m

    # load the ORd model with periodic stimulus and simulate it for 4seconds
    simulation = oc.openRemoteSimulation("https://models.physiomeproject.org/workspace/51a/rawfile/ea7c791f6923be6dfe2a8b9549cfc741e6d9165e/periodic_stimulus.sedml")
    data = simulation.data()
    data.setStartingPoint(0)
    data.setEndingPoint(4000)
    data.setPointInterval(1.0)
    # set the stimulus period
    data.constants()['stimulus_protocol/period'] = 800   # ms
    # and run the simulation
    simulation.run()
    # extract the data to use for training the ML model
    ds = simulation.results().dataStore()
    variables = ds.voiAndVariables()
    t_dataset = variables['stimulus_protocol/time'].values()
    x_dataset = variables['outputs/v'].values()

    #   Creating training dataset - creates a model using "num_training_samples" elements from the dataset.
    num_training_samples = 256  # Can change this parameter to obtain trainings with smaller or bigger datasets
    t_train, x_train = extract_samples_at_random(t_dataset, x_dataset, num_training_samples)

    #   Creating MLP - Given t estimates x
    neurons_per_layer = [1, 64, 64, 1]
    input_mins = np.array([0.0])
    input_maxs = np.array([4000.0])

    NN = MLP("ANN",neurons_per_layer, input_mins, input_maxs)
    NN.initialize()
    NN.generate_graph()

    #   Training an MLP
    train(NN,t_train,x_train)

    #   Estimating x for the entire dataset using the trained MLP
    x_predicted = NN.predict(t_dataset)

    #   Ploting the results
    print("Prediction L2-error : ", np.linalg.norm(x_dataset[:,None] - x_predicted, 2) / np.linalg.norm(x_dataset, 2))

    plt.rc('text', usetex=False)
    plt.rc('font', family='serif')

    fig, ax1 = plt.subplots()
    ax1.plot(t_dataset,x_dataset, color='red', label="Simulation")
    ax1.plot(t_dataset,x_predicted, color='blue', label="Network prediction")
    ax1.set_ylabel('x')
    ax1.set_xlabel('t')
    ax1.scatter(t_train,x_train, marker='x', color='blue', label="Training data")
    ax1.legend()

    plt.show()
