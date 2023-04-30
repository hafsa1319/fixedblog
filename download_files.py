import ftputil
import os

ftp_host = '64.226.120.146'
ftp_user = 'hafsa1319'
ftp_password = 'meleK1319'
remote_path = '/httpdocs'
local_path = 'httpdocs'

if not os.path.exists(local_path):
    os.makedirs(local_path)

with ftputil.FTPHost(ftp_host, ftp_user, ftp_password) as host:
    for root, dirs, files in host.walk(remote_path):
        local_root = os.path.join(local_path, root[len(remote_path):].lstrip('/'))
        for d in dirs:
            os.makedirs(os.path.join(local_root, d), exist_ok=True)
        for f in files:
            remote_file = os.path.join(root, f)
            local_file = os.path.join(local_root, f)
            if host.download_if_newer(remote_file, local_file):
                print(f'Downloaded {remote_file} to {local_file}')
            else:
                print(f'Skipped {remote_file}')
