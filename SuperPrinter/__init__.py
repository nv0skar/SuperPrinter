# SuperPrinter | SuperPrinter Is like print(), but with added features
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

import datetime
import requests
import os
import platform

class SuperPrinter:
    def __init__(self, log_object=None, url=None, port=None):
        if url is not None and port is not None:
            self.url = url + ":" + port
        self.log = log_object
        if self.log is not None:
            self.logtypes = {"info": self.log.info, "warning": self.log.warning, "error": self.log.error, "critical": self.log.critical}
        self.colors = {"info": "\033[36m", "warning": "\033[94m", "error": "\033[33m", "critical": "\033[31m"}
    def __notify_on_system(self, caller, message):
        os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(message, caller))
    def __tunnel(self, caller, message, path, level, time=True):
        f_url = self.url
        if path is not None:
            f_url = f_url + path
        comp_send = {"caller": caller, "message": message, "level": level}
        if time:
            comp_send.update({"time": str(datetime.datetime.now())})
        requests.post(f_url, data=comp_send)
        pass
    def print(self, caller, message, show=True, end="\n", log=False, level="info", colors=True, time=True, post=False, postPath=None, notify=False, catch=False):
        date_string = "At: " + str(datetime.datetime.now())
        string = caller + ": " + message
        colored_string = self.colors[level] + caller + ": " + "\033[0m" + message
        if time:
            string = string + " | " + date_string
            colored_string = colored_string + " | " + date_string
        if self.log is not None and log:
            for type in self.logtypes:
                if level == type:
                    self.logtypes[type](string)
        if post: self.__tunnel(caller, message, postPath, level, time)
        if notify:
            if platform.system() == "Darwin":
                try: self.__notify_on_system(caller, message)
                except: pass
        if show:
            if colors:
                print(colored_string, end=end)
            else:
                print(string, end=end)
        if catch: return string
        else: return
