from os import (getcwd as cwd)
from CronJob import (CronJob)

if __name__ == '__main__':
    job = CronJob()

    job.minute = 0
    job.hour = 0
    job.command = f'{cwd()}/update_pkgs.sh'

    job.register()
