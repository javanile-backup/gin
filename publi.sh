#!/bin/bash

#
sudo rm -fr dist

#
sudo python setup.py sdist

#
twine upload dist/*

