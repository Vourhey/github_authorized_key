#!/usr/bin/env python3
import sys
import urllib.request
import json
import os
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage:\nmain.py 'username' [number]")
        sys.exit()

    keynumber = 0
    if len(sys.argv) == 3:
        keynumber = int(sys.argv[2])

    username = sys.argv[1]
    url = 'https://api.github.com/users/{}/keys'.format(username)

    github = urllib.request.urlopen(url)
    data = github.read()
    jsonobj = json.loads(data.decode('utf-8'))
    key = jsonobj[keynumber]['key']
    
    p = '{}/.ssh/'.format(Path.home())
    if not os.path.exists(p):
        os.makedirs(p)

    f = open(p + 'github_authorized', 'w')
    f.write(key)
    print("Writing key: {}".format(key))
    f.close()

if __name__ == "__main__":
    main()


