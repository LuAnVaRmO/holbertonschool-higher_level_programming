#!/bin/bash
# Displays body of response
curl -sX POST -H "Content-Type: application/json" -d  @"$2" "$1"
