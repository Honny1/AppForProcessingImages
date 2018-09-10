import os
import paramiko

ssh = paramiko.SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect(server, username=username, password=password)
sftp = ssh.open_sftp()
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()