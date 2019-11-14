#!/bin/sh
cd /home/ubuntu/cloud-APS1 && uvicorn server:app --host 0.0.0.0 --port 8000