import os
import paramiko
from tqdm import tqdm

files = []
def processData(localpath,repotepath):
    fileslocalpath = []
    filesremotepath = []
    src_files = os.listdir(localpath)
    for file in src_files:
        fileslocalpath.append(os.path.join(localpath, file))
    for file in src_files:
        filesremotepath.append(os.path.join(repotepath, file))
    files.append(fileslocalpath)
    files.append(filesremotepath)
    return files

def ssh(localpath, remotepath, server, username, password):
    processData(localpath, remotepath)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)

    sftp = ssh.open_sftp()
    try:
        sftp.chdir(remotepath)
    except IOError:
        sftp.mkdir(remotepath)
        sftp.chdir(remotepath)
    sftp.close()

    sftp = ssh.open_sftp()
    for i in tqdm(range(len(files[0]))):
        sftp.put(files[0][i], files[1][i])
    sftp.close()

    ssh.close()

ssh("C:\\temp\hony\\100D3300", "C:\\Hony\\test2", "WPBRN201", "rodak.jan", "******")

