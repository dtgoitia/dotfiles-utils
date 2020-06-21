from pathlib import Path
from subprocess import PIPE, run
from typing import List
from dataclasses import dataclass


CONFIG_DIR = Path.home() / 'Library/Application Support'


@dataclass
class App():
    command: str
    osx_name: str
    config_path: str


def installed_apps() -> List[str]:
    cmd = ['mdfind', "kMDItemKind == 'Application'"]
    proc = run(cmd, stdout=PIPE)
    return proc.stdout.decode('utf-8').strip().split('\n')


def is_installed(app: App) -> bool:
    for app_path in installed_apps():
        if app.osx_name in app_path:
            return True
    return False
