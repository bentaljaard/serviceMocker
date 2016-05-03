#!/bin/sh
locust -f load_test.py --slave --master-host=localhost --host=http://localhost:8888