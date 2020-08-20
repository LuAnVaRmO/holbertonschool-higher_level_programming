#!/bin/bash
# Get the size on bytes with curl
curl -s "$1" | wc -c
