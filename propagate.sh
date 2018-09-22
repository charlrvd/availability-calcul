#!/bin/bash

# update availability.py from tests directory to other directory using it
for dir in appengine docker cloudfunction
do
  cp -a tests/availability.py ${dir}/
done

# update main.py from tests
for dir in appengine docker
do
  cp -a tests/main.py ${dir}/
done
