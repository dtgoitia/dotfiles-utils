from pathlib import Path, PosixPath
import os
import subprocess
from typing import Generator, Iterator, List

from utils import dotfiles, osx, shell, vscode


def vscode_dotfiles_path() -> PosixPath:
    return dotfiles.repo_path() / '.config' / 'Code' / 'User'


def vscode_dotfiles() -> List[PosixPath]:
    all_nested_paths = vscode.VSCODE_DOTFILES_PATH.glob('**/*')
    return [path for path in all_nested_paths if path.is_file()]


def install_config(app: osx.App) -> None:
    if not osx.is_installed(app):
        return
    path = vscode_dotfiles_path()
    dotfiles = vscode_dotfiles()
    for file in dotfiles:
        relative_path = file.relative_to(path)
        target = app.config_path / relative_path
        print(f'Configuring {relative_path} for {app.osx_name}...', end='')
        if target.exists():
            if target.resolve() == file:
                print(' already configured')
                continue
            target.unlink()
        if not target.parent.exists():
            target.parent.mkdir(parents=True)
        target.symlink_to(file)
        print(' success!')


def main() -> None:
    shell.override_sigint()
    for app in [vscode.code, vscode.code_insiders]:
        vscode.install_extensions_from_dotfiles(app)
        install_config(app)


if __name__ == '__main__':
    main()
