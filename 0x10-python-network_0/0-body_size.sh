#!/bin/bash
# Get the size on bytes
curl -s "$1" | wc -c
