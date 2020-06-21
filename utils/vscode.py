from subprocess import run, PIPE
import os
import pathlib
from typing import List

from . import dotfiles, osx


code = osx.App(
    command='code',
    osx_name = 'Visual Studio Code.app',
    config_path = osx.CONFIG_DIR / 'Code/User',
)

code_insiders = osx.App(
    command = 'code-insiders',
    osx_name = 'Visual Studio Code - Insiders.app',
    config_path = osx.CONFIG_DIR / 'Code - Insiders/User',
)

VSCODE_DOTFILES_PATH = dotfiles.repo_path()/'.config/Code/User'


def installed_extensions() -> List[str]:
    proc = run(['code', '--list-extensions'], stdout=PIPE)
    return proc.stdout.decode('utf-8').strip().split('\n')


def extensions_from_dotfiles() -> List[str]:
    with open(dotfiles.repo_path()/'.config/vscode-extensions') as file:
        return file.read().strip().split('\n')


def install_extension(app: osx.App, extension: str) -> None:
    proc = run([app.command, '--install-extension', extension], stdout=PIPE)
    stdout = proc.stdout.decode('utf-8').strip().split('\n')
    print('\n'.join(stdout[1:]))


def install_extensions_from_dotfiles(app: osx.App) -> None:
    print(f'Installing extensions for {app.osx_name} from dotfiles...')
    for extension in extensions_from_dotfiles():
        install_extension(app, extension)
