import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f'{MESSAGE_COLOR}Almost done!')
print(f'{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}')

# Initialize a git repository 
subprocess.call(['git', 'init'])

# Install the necessary dependencies
subprocess.call(['conda', 'env', 'create', '--file', 'environment.yml'])

print(f'{MESSAGE_COLOR}Done!{RESET_ALL}')