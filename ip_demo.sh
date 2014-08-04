#!/bin/bash

# 避免git push等待手动输入用户名 密码
# vim .git-credentials
# https://{username}:{password}@github.com
# git config --global credential.helper store

# 获取当前时间 用于提供提交日志
now=$(date '+%Y-%m-%d %H:%M:%S')
#echo $now

# 获取外网ip
curl ifconfig.me/ip > ip

git add .
git commit -m "$now"

# 提交至github
git push

