#!/bin/bash

filename="path/to/your/file"

if [ -s "$filename" ]; then
  echo "File exists and is not empty."
else
  echo "File does not exist or is empty."
fi
#
