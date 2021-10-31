# -*- coding: utf-8 -*-
import requests
import json
from esc_sync import logger

class GistApi:
    apiPrefix = "https://api.github.com/gists"

    def __init__(self, token, gistId, filename):
        session = requests.Session()
        session.headers.update({
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github.v3+json",
        })
        self.session = session
        self.gistId = gistId
        self.filename = filename

    def downloadContent(self):
        resp = self._get(self.apiPrefix + "/" + self.gistId)
        file = resp["files"].get(self.filename, {})
        return file.get("content", "")

    def uploadContent(self, content):
        data = {
            "files": {
                self.filename: {
                    "content": content,
                }
            }
        }
        self._patch(self.apiPrefix + "/" + self.gistId, data)

    def remoteInfo(self):
        return "gistId[%s], remoteFilename[%s]"%(self.gistId, self.filename)

    def _get(self, url):
        resp = self.session.get(url, timeout=5)
        respDict = json.loads(resp.text)
        logger.debug("url[%s],method[GET],response[%s]"%(url,resp.text))
        return respDict

    def _patch(self, url, data):
        resp = self.session.patch(url, json.dumps(data), timeout=5)
        respDict = json.loads(resp.text)
        logger.debug("url[%s],method[POST] response[%s]"%(url,resp.text))
        return respDict
