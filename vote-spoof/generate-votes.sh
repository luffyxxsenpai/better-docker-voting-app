#!/bin/sh

ab -n 100 -c 50 -p posta -T "application/x-www-form-urlencoded" http://localhost:8080/
ab -n 220 -c 50 -p postb -T "application/x-www-form-urlencoded" http://localhost:8080/
