import subprocess

def init(): 
    cmd = 'git init'
    subprocess.run(cmd, stdout=subprocess.DEVNULL, shell=True)

def branches(): 
    cmd = "git branch"
    branch_list = [b.strip() for b in subprocess.check_output(cmd, shell=True).decode().split('\n') if len(b) > 0]
    return branch_list

def commit():
    cmd = "git commit --allow-empty --allow-empty-message -m ''"
    subprocess.run(cmd, stdout=subprocess.DEVNULL, shell=True)

def head(): 
    cmd = "git rev-parse --short HEAD"
    return subprocess.check_output(cmd, shell=True).decode().strip()

def commits(branch): 
    cmd = f'git log {branch} --oneline'
    commits = [b.split(' ')[0] for b in subprocess.check_output(cmd, shell=True).decode().split('\n') if len(b) > 0]
    return commits

def checkout(branch): 
    cmd = f'git checkout -b {branch}'
    subprocess.run(cmd, stdout=subprocess.DEVNULL, shell=True)

def merge(branch):
    cmd = f'git merge {branch}'
    subprocess.run(cmd, stdout=subprocess.DEVNULL, shell=True)

