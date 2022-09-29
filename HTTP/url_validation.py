from colorama import Fore, Style
import httpx
import sys
import re

"""
Script that checks if all links in a file are valid
Also creates a new clean file with only valid links
"""

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except IndexError:
    raise SystemExit(f'Usage: {sys.argv[0]} <input_file> <output_file>')

urls = []
failed_urls = []

link_name = r'[^\[]+'
link_url = r'http[s]?://.+'
markup_regex = f'\[({link_name})]\(\s*({link_url})\s*\)'

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

try:
    with open(input_file) as file:
        lines = file.readlines()
        for line in lines:
            url = re.findall(markup_regex, line)
            if url and 'http' in url[0][1]:
                urls.append(url[0][1])
except FileNotFoundError:
    print('Input File Not Found!')
    sys.exit(1)

print(f'{Fore.BLUE}Total URLs: {len(urls)}{Style.RESET_ALL}')
print(f'{Fore.BLUE}Scanning URLs...{Style.RESET_ALL}\n')

for n, url in enumerate(urls, start=1):
    try:
        r = httpx.get(url, follow_redirects=True, verify=False, headers=header)      
        if r.status_code is 200:
            status = f'{Fore.GREEN}{r.status_code}{Style.RESET_ALL}'
            print(f'{Fore.BLUE}[{n:>02}]{Style.RESET_ALL} Status: {status} | URL: {Fore.GREEN}{r.url}{Style.RESET_ALL}')
        else:
            status = f'{Fore.RED}{r.status_code}{Style.RESET_ALL}'
            print(f'{Fore.BLUE}[{n:>02}]{Style.RESET_ALL} Status: {status} | URL: {Fore.RED}{r.url}{Style.RESET_ALL}')
            failed_urls.append(url)
    except Exception as e:
        status = f'{Fore.RED}Exception{Style.RESET_ALL}'
        print(f'{Fore.BLUE}[{n:>02}]{Style.RESET_ALL} Status: {status} | URL: {Fore.RED}{url}{Style.RESET_ALL}')
        failed_urls.append(url)
    except KeyboardInterrupt:
        sys.exit(1)

print(f'\n{Fore.BLUE}Total failed URLs: {len(failed_urls)}{Style.RESET_ALL}')
print(f'{Fore.BLUE}Creating new file {output_file} with valid URLs...{Style.RESET_ALL}')

with open(input_file) as oldfile, open(output_file, 'w') as newfile:
    for line in oldfile:
        if not any(failed_url in line for failed_url in failed_urls):
            newfile.write(line)