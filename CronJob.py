from os import (system as run_cmd)


class CronJob:
    minute: int = '*'
    hour: int = '*'
    day: int = '*'
    month: int = '*'
    weekday: int = '*'

    command: str = "echo"

    def register(self):
        run_cmd('sudo service cron stop')
        run_cmd(f'sudo cron job'
                f' {self.minute} {self.hour} {self.day} {self.month} {self.weekday}'
                f' {self.command}')
        run_cmd('sudo service cron start')
