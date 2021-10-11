#!/usr/bin/env python
r'''
 ./hw2.py
 Implements, tests and compares 2 ML algorithms: (1) k-NN and (2) the
 "pocket" algorithm.

 By        : Leomar Durán <https://github.com/lduran2/>
 When      : 2021-10-11t16:52
 For       : CIS 4526
 Version   : 1.0.1
 Canonical : https://github.com/lduran2/cis-4526-hw2-kNN-vs-pocket/blob/master/hw2.py

 CHANGELOG :
    v1.0.1 - 2021-10-11t16:52
        copied over the attribute names

    v1.0 - 2021-10-11t15:23
        filled out the template

    v0.0 - ????-??-??t??:??
        the tempate
 '''

# Any reference to a "matrix" or "array" or "vector" for input and
# output should be of the type numpy.ndarray. DO NOT use another type
# (e.g., lists, dictionary, numpy.mat).
from numpy import ndarray as matrix
import csv                  # for DictReader
from typing import Final    # for constants


def test_knn(train_x, train_y, test_x, num_nn):
    r'''
     @params
        train_x : (num_train, num_dims) data matrix
        test_x  : (num_test, num_dims) data matrix
        train_y : (num_train ,) label vector
        num_nn  := the number of nearest neighbors for classification
     @return pred_y  : (num_test,) label vector
     '''
    pred_y = None
    return pred_y


def train_pocket(train_x, train_y, num_iters):
    r'''
     @params
        train_x   : (num_train, num_dims) data matrix
        train_y   : (num_train,) +1/-1 label vector
        num_iters := # iterations for the algorithm
     @return w : vector of learned perceptron weights
     '''
    w = None
    return w


def test_pocket(w, test_x):
    r'''
     @params
        w : vector of learned perceptron weights
        test_x : (num_test, num_dims) data matrix
     @return pred_y : (num_test,) +1/-1 label vector
     '''
    pred_y = None
    return pred_y


def compute_accuracy(test_y, pred_y):
    r'''
     @params
        test_y : (num_test,) label vector
        pred_y : (num_test,) label vector
     @return acc : float[0.0, 1.0] = classification accuracy
    '''
    acc = None
    return acc


def get_id():
    r'''
     @return id := a string representing your Temple Accessnet
                   (e.g., "tua12345")
     '''
    id = r'tuh24865'
    return id


def main():
    r'''
     For the algorithms (k-NN, pocket), run the following experiments
        Randomly subsample the training data for num_train
            = {100, 1000, 2000, 5000, 10000, 15000}
        For k-NN, use the following values for k
            = {1,3,5,7,9} (5 versions of k-NN)
        Note: You should run at least 6 (algorithms) * 6 (values of N)
            = 36 total experiments
     '''

    # the file name of the data set
    DATASET: Final = r'./letter-recognition.data'

    # http://archive.ics.uci.edu/ml/datasets/Letter+Recognition
    # 7. Attribute Information:
    FEATURE_NAMES: Final = [
        'lettr',    # 01.	capital letter	(26 values from A to Z)
        'x-box',    # 02.	horizontal position of box	(integer)
        'y-box',    # 03.	vertical position of box	(integer)
        'width',    # 04.	width of box			(integer)
        'high ',    # 05.	height of box			(integer)
        'onpix',    # 06.	total # on pixels		(integer)
        'x-bar',    # 07.	mean x of on pixels in box	(integer)
        'y-bar',    # 08.	mean y of on pixels in box	(integer)
        'x2bar',    # 09.	mean x variance			(integer)
        'y2bar',    # 10.	mean y variance			(integer)
        'xybar',    # 11.	mean x y correlation		(integer)
        'x2ybr',    # 12.	mean of x * x * y		(integer)
        'xy2br',    # 13.	mean of x * y * y		(integer)
        'x-ege',    # 14.	mean edge count left to right	(integer)
        'xegvy',    # 15.	correlation of x-ege with y	(integer)
        'y-ege',    # 16.	mean edge count bottom to top	(integer)
        'yegvx',    # 17.	correlation of y-ege with x	(integer)
    ]

    # open the dataset
    with open(DATASET) as dataFile:
        # place a dictionary reader on it
        reader = csv.DictReader(dataFile, fieldnames=FEATURE_NAMES)
        # dictionaries are ordered in Python 3.6,
        # so we can just slice off the result field
        print(reader)
    # end with open(DATASET) as data

    # num_train = number of training examples
    # num_test = number of testing examples
    # num_dims be the dimensionality of the examples
    return None


if __name__ == "__main__":
    main()
