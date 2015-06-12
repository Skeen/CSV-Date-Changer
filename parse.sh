#!/bin/sh
./parse.py real_data.csv | tr '\n' ';' | tr '@' '\n' | sed "s/;//g"
