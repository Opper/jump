#!/usr/bin/env bash

path="/opt/jump"

git clone https://github.com/opper/jump $path
cd $path
virtualenv venv
source venv/bin/activate
pip install -r requirements