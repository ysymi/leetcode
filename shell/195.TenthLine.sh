#! /usr/bin/bash

sed -n '10 p' file.txt

# other solution
# awk 'NR==10 {print}' file.txt
# head -10 file.txt | tail -1
