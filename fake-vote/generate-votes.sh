#!/bin/sh

ab -n 100 -c 50 -p post-a -T "application/x-www-form-urlencoded" http://vote.homelain.click/
ab -n 220 -c 50 -p post-b -T "application/x-www-form-urlencoded" http://vote.homelain.click/

ab -n 20 -c 10 -p post-b -T "application/x-www-form-urlencoded" http://vote.in/
ab -n 50 -c 10 -p post-a -T "application/x-www-form-urlencoded" http://vote.in/

#ab -n 100 -c 50 -p post-a -T "application/x-www-form-urlencoded" http://localhost:8080/
#ab -n 220 -c 50 -p post-b -T "application/x-www-form-urlencoded" http://localhost:8080/

#ab -n 20 -c 10 -p post-b -T "application/x-www-form-urlencoded" http://vote.in/
#ab -n 50 -c 10 -p post-a -T "application/x-www-form-urlencoded" http://vote.in/
