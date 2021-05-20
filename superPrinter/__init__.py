# SuperPrinter | SuperPrinter is pretty much like print(), but with superpowers
# Copyright (C) 2021 ItsTheGuy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from . import logger
from . import levels
from . import globals
import os
import platform
import datetime
import requests

colors = {levels.info: "\033[36m", levels.warning: "\033[94m", levels.error: "\033[33m", levels.critical: "\033[31m"}

class printer:
    def __init__(self, logFile=None, postURL=None):
        if postURL is not None:
            self.post = True
            self.postURL = str(postURL)
        else: self.post = False
        if logFile is not None:
            self.log = True
            self.logWrite = logger.logger(logFile)
        else: self.log = False

    @staticmethod
    def __notify(caller, message):
        if platform.system() == "Darwin":
            os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(message, caller))

    def __tunnel(self, caller, message, path, level, time=True, actualTime=None):
        if path is not None: f_url = "{}/{}".format(self.postURL, path)
        else: f_url = "{}".format(self.postURL)
        comp_send = ({"caller": caller, "message": message, "level": level}) if not time and actualTime is not None else ({"caller": caller, "message": message, "level": level, "time": actualTime})
        requests.post(f_url, data=comp_send, headers={'User-Agent': 'SuperPrinter-{}'.format(globals.__version__)})

    def sprint(self, caller, message, end="\n", level=levels.info, log=False, show=True, colored=True, time=True, post=False, postPath=None, notify=False, catch=False):
        if not self.log and log: raise Exception("Logging fileName not defined")
        if not self.post and post: raise Exception("Post path and port not defined")
        actualTime = str(datetime.datetime.now())
        composedString = ("{}: {}".format(caller, message)) if not colored else ("{}{}: \033[0m{}".format(colors[level], caller, message))
        if time: composedString = "{} | Time: {}".format(composedString, actualTime)
        if self.log and log:
            for logType in logger.logTypes:
                if level == logType: self.logWrite.write((str("({}) {}: {}".format(str(logger.logTypes.get(level)), caller, message))) if not time else (str("({}) {}: {} | Time: {}".format(str(logger.logTypes.get(level)), caller, message, actualTime))))
        if self.post and post: self.__tunnel(caller, message, postPath, level, time, actualTime)
        if notify: printer.__notify(caller, message)
        if show: print(composedString, end=end)
        if catch: return "{}: {}".format(caller, message)
        else: return
