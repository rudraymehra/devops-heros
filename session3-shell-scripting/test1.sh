#!/bin/bash

mkdir -p result_file
cd result_file || exit 1
touch result.log
echo "This is my result file" > result.log
date
hostname
whoami
df -h
ps > process.log

read -r -p "Enter your name: " name
read -r -p "Enter your roll number: " roll_no

current_date=$(date)
{
  echo "My name is $name"
  echo "My roll number is $roll_no"
  echo "Generated on $current_date"
} >> result.log
