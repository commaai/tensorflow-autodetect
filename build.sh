#!/bin/bash
set -e

VERSIONS=$(curl -s https://pypi.org/pypi/tensorflow/json | jq '.releases|keys_unsorted[]' | sed -e 's/^"//' -e 's/"$//')
for VERSION in $VERSIONS; do
    echo "[BUILDING ${VERSION}]"
    sudo VERSION=${VERSION} python setup.py sdist
done
