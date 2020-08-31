import numpy as np
import pandas as pd
import tensorflow as tf
from scipy.stats import multivariate_normal


import gpflow
import gpflow.multioutput.kernels as mk
import gpflow.multioutput.features as mf

import pickle

import sys
sys.path.insert(1, "../ipsc_gp_clustering")
from splitgpm import SplitGPM
import gpflow.training.monitor as mon
import os
import matplotlib.pyplot as plt

C=5
G=17066
T=5
K1=1
K2=20
N=C*T


def normalize(X):
    return X / X.sum(1)[:, None]


def save_model(m, fname="../data/splitgpm.trained.pickle"):
    savedict = m.read_values()
    f = open(fname, 'wb')
    pickle.dump(savedict, f)
    f.close()


def main():
  X = np.loadtxt("../data/neur.X.txt")
  Y = np.loadtxt("../data/neur.Y.txt")

  gpflow.reset_default_graph_and_session()
  name = 'test'
  minibatch_size = 500

  W1_init = normalize(np.random.random(size=(C, K1)))
  W2_init = normalize(np.random.random(size=(G, K2)))


  with gpflow.defer_build():
    kernel = mk.SharedIndependentMok(gpflow.kernels.RBF(1, active_dims=[0]), K1 * K2)
    Z = np.linspace(0, 1, T)[:, None].astype(np.float64)
    feature = gpflow.features.InducingPoints(Z)
    feature = mf.SharedIndependentMof(feature)

    model = SplitGPM(X, Y, np.log(W1_init + 1e-5), np.log(W2_init + 1e-5), kernel, gpflow.likelihoods.Gaussian(), feat=feature, minibatch_size=minibatch_size, name=name)
  model.compile()

  model.W1.set_trainable(True)  # learn cell assignments
  model.W2.set_trainable(True)  # learn gene assignments
  model.feature.set_trainable(True)  # move inducing points
  model.kern.set_trainable(True)  # learn kernel parameters
  model.likelihood.set_trainable(True)  # lear likelihood parameters

  adam = gpflow.train.AdamOptimizer(0.005)
  adam.minimize(model, maxiter=10000)

  save_model(model)


if __name__=="__main__":
  main()
