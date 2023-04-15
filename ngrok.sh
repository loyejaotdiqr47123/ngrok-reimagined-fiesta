#!/bin/bash
cd / && nohup ./ngrok tcp --region jp 8080 &>/dev/null &
