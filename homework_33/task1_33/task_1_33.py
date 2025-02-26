import requests, json

WIKI_URL = 'https://wikipedia.org/robots.txt'
TWITTER_URL = 'https://twitter.com/robots.txt'
PANDORA_URL = 'https://pandora.com/robots.txt'
TOUS_URL = 'https://tous.com/robots.txt'

wik_req = requests.get(WIKI_URL)
twit_req = requests.get(TWITTER_URL)
pandora_req = requests.get(PANDORA_URL)
tous_req = requests.get(TOUS_URL)

with open('wiki_robots.txt', 'w') as w_f:
    w_f.write(f'from {WIKI_URL}\n {wik_req.text}')

with open('pandora_robots.txt', 'w') as p_f:
    p_f.write(f'from {PANDORA_URL}\n {pandora_req.text}')

with open ('tous_robots.txt', 'w') as t_f:
    t_f.write(f'{TOUS_URL}\n {tous_req.text}')