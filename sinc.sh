#!/bin/bash
git checkout master
git fetch github
git rebase github/master

git push