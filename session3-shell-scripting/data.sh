#!/usr/bin/env bash

mkdir -p data1
cd data1 || exit 1
echo "This is a log file." > app.log
cat app.log
echo "This is my file" > app.log
cat app.log
