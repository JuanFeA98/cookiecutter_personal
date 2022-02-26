import os
from sre_constants import SUCCESS
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[32m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith('x'):
    print(f'{ERROR_COLOR}Project slug cannot start with "x"{RESET_ALL}')
    sys.exit(1)

print(f'{MESSAGE_COLOR}Project slug is {project_slug}{RESET_ALL}')
print(f'Creating project at {os.getcwd()}{RESET_ALL}')