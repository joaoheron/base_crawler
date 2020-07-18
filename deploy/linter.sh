#!/bin/bash

cd ~
mkdir .config
pwd
ls -la

python ../home/runner/work/base_crawler/base_crawler/deploy/build_linter_profile.py
cd ../home/runner/work/base_crawler/base_crawler

# Type which folders you would like do test with flake8
flake8 base_crawler/ tests/ deploy/

if [ $? -eq 1 ]
then
    echo "Build has failed because flake8 found errors."
    exit 1
else
    echo "Build has succeeded. Flake8 couldn't found any error. Congratulations!"
    exit 0
fi

