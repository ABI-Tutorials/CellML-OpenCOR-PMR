import tensorflow as tf
import numpy as np

class MLP(object):

    def __init__(self, name, layers, lb, ub):

        self.layers = layers
        self.lb = lb
        self.ub = ub
        self.name = name
        self.weights = []
        self.biases = []
        self.X = []
        self.Y = []
        self.name = name
        self.scope = None

        self.it = 0

        self.input_dictionary = {}
        self.loss_function = None
        self.optimizer = None
        self.session = None

        self.summary_writer = None

        self.status = "Created"

    def initialize(self):
        """
        Initialize the weights and biases of the current network. Initial weights adopt a normal initialization while
        biases are zeroed.
        :return:
        """
        with tf.name_scope(self.name) as self.scope:
            self.weights = []
            self.biases = []

            for idx_layer in range(0,len(self.layers)-1):
                current_weight = tf.Variable(tf.truncated_normal([self.layers[idx_layer], self.layers[idx_layer + 1]],
                                                                 stddev=np.sqrt(2 / (self.layers[idx_layer] + self.layers[idx_layer + 1])),
                                                                 dtype = tf.float32),name="W")
                current_bias = tf.Variable(tf.zeros([1,self.layers[idx_layer+1]], dtype=tf.float32), dtype=tf.float32,name="b")

                self.weights.append(current_weight)
                self.biases.append(current_bias)

        self.status = "Initialized"

    def set_states(self,weights,biases):
        """
        Sets the internal state of network. No previous initialization is required.
        :param weights: Weight matrices in each layer [W x num_layers]
        :param biases: Bias vector in each layer [b x num_layers]
        :return:
        """
        with tf.name_scope(self.name) as self.scope:
            self.weights = weights
            self.biases = biases

        self.status = "Initialized"

    def generate_graph(self):
        """
        Initialize the tensorflow graph creating the variables X and Y in the object, being the input and output layer
        respectively.
        :return:
        """

        with tf.name_scope(self.scope):
            if self.status == "Created":
                print("Graph can not be created until the network is initialized or its states are set.")
                return

            #   Creating placeholders
            for input_idx in range(0,self.layers[0]):
                self.X.append(tf.placeholder(tf.float32, shape=[None, 1]))

            with tf.name_scope("normalization"):
                C = tf.concat(self.X,1)

                #   Creating normalization layer
                H = 2 * (C - self.lb) / (self.ub - self.lb) - 1

            #   Creating hidden layers
            for idx_layer in range(0,len(self.layers)-2):
                with tf.name_scope("layer_"+str(idx_layer)):
                    W = self.weights[idx_layer]
                    b = self.biases[idx_layer]
                    H = tf.tanh(tf.add(tf.matmul(H,W),b),name="activ_func")

            #   Creating output layer (linear = scales the solution to appropriate range)
            W = self.weights[-1]
            b = self.biases[-1]

            self.Y.append(tf.add(tf.matmul(H, W), b,name="scale_func"))

        self.status = "Untrained"

    def loss_callback(self, loss):
        """
        Callback function that reports the current loss during optimization process.
        :param loss: Current loss value
        :return:
        """
        if(self.summary_writer):
            if self.it % 5 == 0:
                s = tf.Summary(value=[tf.Summary.Value(tag=self.name+"_train_loss", simple_value=loss)])
                self.summary_writer.add_summary(s, self.it)
        print(self.name + ' - It ' + str(self.it) + ' - Loss: %e' % (loss))
        self.it += 1

    def predict(self, t_predict):
        x_predicted = self.session.run(self.Y[0], {self.X[0]: t_predict[:,None]})
        return x_predicted

    def predictDx3(self, t_predict):
        dx = tf.gradients(self.Y[0],self.X[0])[0]
        dx2 = tf.gradients(dx,self.X[0])[0]
        dx3 = tf.gradients(dx2,self.X[0])[0]
        x_predicted = self.session.run(dx3, {self.X[0]: t_predict[:,None]})
        return x_predicted