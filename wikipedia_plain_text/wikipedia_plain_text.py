#!/usr/bin/env python

import requests
import argparse

argpareparser = argparse.ArgumentParser(
    prog='WikipediaPlainText',
    description='Wikipedia article as plain text',
    epilog='Fuck yeah API bitch.')

argpareparser.add_argument('article_name')           # positional argument
argpareparser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag

args = argpareparser.parse_args()

article_name = str(args.article_name)

response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
        'action': 'query',
        'format': 'json',
        'titles': article_name,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
        'AcceptEncoding': 'gzip'
    }
)

print("response: " + str(response))
response_json = response.json()
print("response_json: " + str(response_json))
page = next(iter(response_json['query']['pages'].values()))
print("page:" + str(page))
print(page['extract'])
