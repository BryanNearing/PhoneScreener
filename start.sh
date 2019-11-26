#!/bin/bash

xterm -e ./ngrok http 5000 &
xterm -e 'python3 AnsweringMachine.py' &
python3 DB.py 
