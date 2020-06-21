"""
Save Visual Studio Code extension list to dotfiles.
"""
from utils import dotfiles, vscode


def save_code_extensions_to_dotfiles() -> None:
    extensions = vscode.installed_extensions()
    repo = dotfiles.repo_path()
    with open(repo/'.config/vscode-extensions', 'w') as f:
        content = '\n'.join(extensions)
        f.write(content)


if __name__ == '__main__':
    save_code_extensions_to_dotfiles()
