#!/bin/bash

echo -n "commit title : "
read commit
git add .
git commit -m "${commit}"
git push -u origin main

