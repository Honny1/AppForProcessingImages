import os
import paramiko
def ssh(localpath, remotepath, server, username, password):
    ssh = paramiko.SSHClient()
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath)
    sftp.close()
    ssh.close()
ssh(input("Zadej cestu k datum: "), input("Zadej cestu kam uložit data: "), input("Zadej server:"), input("Zadej username: "), input("Zadej password: "))
