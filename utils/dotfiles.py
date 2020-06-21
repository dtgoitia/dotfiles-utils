from pathlib import Path, PosixPath
import os


def repo_path() -> PosixPath:
    path = os.environ.get('DOTFILES_REPO_PATH', '~/projects/tmp/dotfiles')
    return Path(path).expanduser()
