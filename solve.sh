#!/bin/bash

for f in data/*; do 
  python3 main.py $f
done;
