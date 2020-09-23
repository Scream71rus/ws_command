#!/bin/bash

VENV=./.venv
LOGDIR=./log
TMPDIR=./tmp

rm -rf $VENV
rm -rf $LOGDIR

mkdir $LOGDIR
mkdir $TMPDIR

chmod +x ./server.py

virtualenv -p python3.6 $VENV
source $VENV/bin/activate
pip install -r requirements