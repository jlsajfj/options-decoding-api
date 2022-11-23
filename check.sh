#!/bin/bash

git remote update
if git status | grep -q "git pull"; then
        git fetch --all
        git reset --hard HEAD
        git merge @{u}
fi
