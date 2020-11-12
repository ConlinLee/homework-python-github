#! /usr/bin/python
# -*- coding: utf8 -*-


import os
# os.chdir('d:\\')
cmd = r"""Set -ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" SMB1 -Type DWORD -Value 0 -Force&sc.exe config lanmanworkstation depend= bowser/mrxsmb20/nsi&sc.exe config mrxsmb10 start= disabled
"""
cmd = os.popen(cmd)
print(cmd.read())



