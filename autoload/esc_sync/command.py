# -*- coding: utf-8 -*-
import os
import time

class Command:
    @classmethod
    def download(cls, api, filepath, backup):
        filepath = os.path.expanduser(filepath)
        filepath = os.path.expanduser(filepath)
        with open(filepath, 'r') as f:
            content = f.read()
            remoteContent = api.downloadContent()
            if content == remoteContent:
                print("Don't need download [%s] to [%s], they are same"%(api.remoteInfo(), filepath))
                return

        tmppath = ""
        if backup:
            (_, filename) = os.path.split(filepath)
            tmppath = "/tmp/%s_%d"%(filename, int(time.time()))
            with open(tmppath, 'w+') as f:
                f.write(content)

        with open(filepath, "w") as f:
            f.write(remoteContent)
            f.flush()
            if tmppath:
                print("Download [%s] to [%s] success, old content save to[%s]"%(api.remoteInfo(), filepath, tmppath))
            else:
                print("Download [%s] to [%s] success"%(api.remoteInfo(), filepath))


    @classmethod
    def upload(cls, api, filepath):
        filepath = os.path.expanduser(filepath)
        with open(filepath, 'r') as f:
            content = f.read()
            remoteContent = api.downloadContent()
            if content == remoteContent:
                print("Don't need upload [%s] to [%s], they are same"%(filepath, api.remoteInfo()))
                return
            api.uploadContent(content)
            print("Upload [%s] to [%s] success"%(filepath, api.remoteInfo()))

