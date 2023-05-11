import getpass
import os
import shlex
import signal
import subprocess
import sys

from django.core.management.base import BaseCommand
from django.utils import autoreload
from utilities.logger import logger


def restart_celery():
    celery_worker_cmd = "celery -A core worker"
    # cmd = f"pkill -f {celery_worker_cmd}"
    pid_cmd = f"ps -f -u {getpass.getuser()} | grep '{celery_worker_cmd}' | grep -v grep | awk '{{print $2}}" # noqa
    if sys.platform == "win32":
        cmd = "taskkill /f /t /im celery.exe"
    else:
        try:
            celery_pid = int(subprocess.check_output(shlex.split(pid_cmd)))
            os.kill(celery_pid, signal.SIGTERM)
        except (subprocess.CalledProcessError, ValueError):
            logger.error("Process is not running or PID is invalid")
            pass

    subprocess.call(
        shlex.split(f"{celery_worker_cmd} --loglevel=info --autoscale-10,1 --concurrency=12") # noqa
    )


class Command(BaseCommand):
    """Base command for restarting Celery workers."""

    def handle(self, *args, **kwargs):
        logger.info("Starting Celery worker with autoreload...")
        autoreload.run_with_reloader(restart_celery)