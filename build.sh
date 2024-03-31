#/bin/sh

set -xe
clear
python main.py > out.md
glow out.md
