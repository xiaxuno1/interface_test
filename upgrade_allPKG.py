# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: upgrade_allPKG
# Author: xiaxu
# DATA: 2022/10/26
# Description:y:用于更新所有的包
# ---------------------------------------------------
import pkg_resources
from subprocess import call

for packages in [dist.project_name for dist in pkg_resources.working_set]:
    call("pip3 install --upgrade " + ''.join(packages) + ' --user', shell=True)
