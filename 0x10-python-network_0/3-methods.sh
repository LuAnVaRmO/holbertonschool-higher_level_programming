#!/bin/bash
# display methods
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2
