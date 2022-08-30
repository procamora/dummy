#!/bin/bash

git add .
git commit -m "automatico `date +'%Y-%m-%d'`"
git status
git push
