#!/bin/bash
#######################################################
# Copies py into a temp directory to run it
# This way, __pycache__ is not created
# and the dir stays clean
# doing this since .gitignore is not working properly
#######################################################

if [ ! -d "./../anton_temp" ]; then
	mkdir ./../anton_temp
fi

cp -R ./* ./../anton_temp/
sudo python3 ./../anton_temp/app.py
