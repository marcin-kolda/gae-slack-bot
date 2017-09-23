#!/bin/bash
build_date=`date -u +"%Y-%m-%d %H:%M:%S"`
git_commit=`git rev-parse --short HEAD`
sed -i -e "s/git_commit/${git_commit}/g" settings.py
sed -i -e "s/build_date/${build_date}/g" settings.py
sed -i -e "s/verification_token/${VERIFICATION_TOKEN}/g" settings.py
sed -i -e "s/bot_access_token/${BOT_ACCESS_TOKEN}/g" settings.py
