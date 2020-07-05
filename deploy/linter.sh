#!/bin/bash
pwd
ls -la
cd ~
mkdir .config
pwd
ls -la

# python ../opt/atlassian/pipelines/agent/build/deploy_scripts/build_linter_profile.py
# cd ../opt/atlassian/pipelines/agent/build

# # Type which folders you would like do test with flake8
# flake8 src/ tests/ deploy/

# if [ $? -eq 1 ]
# then
#     echo "Build has failed because flake8 found errors."
#     exit 1
# else
#     echo "Build has succeeded. Flake8 couldn't found any error. Congratulations!"
#     exit 0
# fi

