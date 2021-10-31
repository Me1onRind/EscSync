# -*- coding: utf-8 -*-

import os
import time

debugMode = False

def setDebugModel(mode):
    global debugMode
    debugMode = mode

def debug(s):
    if not debugMode:
        return
    logpath = os.path.expanduser("~/.esc_sync.log")
    with open(logpath, "a+") as f:
        f.write("[DEBUG][%s] %s"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),s))
