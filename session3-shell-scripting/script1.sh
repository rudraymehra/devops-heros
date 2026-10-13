#!/usr/bin/env bash

mkdir -p test
cd test || exit 1
echo "this is file1" > app.log
echo "this is file2" >> app.log
cat app.log
