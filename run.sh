#!/usr/bin/env bash

# how to run
python data.py make_db train

python classifier.py train ./data/train ./model/train

python classifier.py predict ./data/train ./model/train ./data/train/ dev predict.tsv

python evaluate.py evaluate predict.tsv ./data/train/data.h5py dev ./data/y_vocab.py3.cPickle

# create an output file to submit

python data.py make_db dev ./data/dev --train_ratio=0.0

python classifier.py predict ./data/train ./model/train ./data/dev/ dev baseline.predict.tsv

# zip and submit baseline.predict.tsv file