# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science
# => CAPÍTULO 17

### Introdução a Deep Learning com TensorFlow ###

### Problema de Negócio: ###
# Construir um modelo de Inteligência Artificial capaz de classificar imagens
# considerando 10 categorias: ['airplane', 'automobile', 'bird', 'cat', 'deer',
# 'dog', 'frog', 'horse', 'ship', 'truck']. Dada uma nova imagem de uma dessas
# categorias o modelo deve ser capaz de classificar e indicar o que é a imagem.

# Imports
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Carregando os Dados
# https://www.cs.toronto.edu/~kriz/cifar.html

# Carrega o dataset CIFAR-10
(imagens_treino, labels_treino), (imagens_teste, labels_teste) = datasets.cifar10.load_data()