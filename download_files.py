import ftputil

with ftputil.FTPHost('64.226.120.146', 'hafsa1319', 'meleK1319') as host:
    host.download_if_newer('/httpdocs', 'httpdocs')
