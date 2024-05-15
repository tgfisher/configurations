#!/bin/bash

git submodule init
git submodule update

python3 ./write_toml_from_template.py
