#!/bin/bash

git status
git add .
git commit -m 'udpate'
git push



git rm --cached use_git.sh
git commit -m 'delete remote somefile'
git push

