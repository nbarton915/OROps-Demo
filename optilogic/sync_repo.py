from install_requirements import ensure_requirements
ensure_requirements()

import git
import os

REPOSITORY_DIRECTORY = f'{os.getcwd()}/..'

repository = git.cmd.Git(git_dir)
try:
    repository.pull()
except:
    print(f'There was a problem pulling latest from the remote repository')
    raise