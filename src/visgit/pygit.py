import subprocess
import re

def init(): 
    cmd = 'git init'
    subprocess.run(cmd, stdout=subprocess.DEVNULL, shell=True)

# .strip().removeprefix('* ')
def branches(): 
    cmd = "git branch"
    branch_list = [b for b in subprocess.check_output(cmd, shell=True).decode().split('\n') if len(b) > 0]
    return branch_list

def current_branch(): 
    for branch in branches(): 
        if '*' in branch: 
            return branch

def commit():
    cmd = "git commit --allow-empty --allow-empty-message -m ''"
    subprocess.run(cmd, stdout=subprocess.DEVNULL, shell=True)

def head(): 
    cmd = "git rev-parse --short HEAD"
    return subprocess.check_output(cmd, shell=True).decode().strip()

def log(branch): 
    cmd = f'git log {branch} --oneline --tags'
    commits = []
    for line in subprocess.check_output(cmd, shell=True).decode().split('\n'):
        if len(line) > 0: 
            # match = re.search("^(.*) (\(.*\))$", line)
            # if match: 
            #     commit = [match.group(1), match.group(2)]
            # else:
            #     commit = [line, '']
            commit = line.split()[0].strip()
            commits.append(commit)
    commits.reverse()
    return commits

def checkout(branch, create=False): 
    cmd = f'git checkout -b {branch}'
    if not create:
        cmd = f'git checkout {branch}'
    subprocess.run(cmd, stdout=subprocess.DEVNULL, shell=True)

def merge(branch):
    cmd = f'git merge {branch}'
    subprocess.run(cmd, stdout=subprocess.DEVNULL, shell=True)
