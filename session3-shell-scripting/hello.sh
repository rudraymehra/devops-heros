#!/usr/bin/env bash

mkdir -p hello
cd hello || exit 1
touch app.log
echo "This is my logfile" > app.log
cat app.log
