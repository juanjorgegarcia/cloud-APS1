#!/bin/sh
cd /home/ubuntu/cloud-APS1 && uvicorn redirect:app --host 0.0.0.0 --port 8000
