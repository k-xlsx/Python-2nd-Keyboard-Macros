import os
import psutil


def kill_proc_by_name(proc_name: str):
    for proc in psutil.process_iter():
        if proc.name() == proc_name:
            proc.kill()


def set_low_proc_priority():
    p = psutil.Process(os.getpid())
    p.nice(psutil.IDLE_PRIORITY_CLASS)
