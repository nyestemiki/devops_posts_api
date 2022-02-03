from datetime import datetime


class Log:
    def __init__(self, method, path) -> None:
        self.method = method
        self.path = path


def log(inputLog):
    with open('./posts_api/logs/debug.log', 'a') as f:
        now = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        _log = "{} : {} {}\n".format(now, inputLog.method, inputLog.path)
        f.write(_log)
        print(_log)
