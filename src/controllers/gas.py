from flask import Flask, request
import json
from flask_restx import Api, Resource
from src.server.instance import server
import urllib.request
from bs4 import BeautifulSoup

app, api = server.app, server.api

wallet = ''

@api.route('/', methods=['GET', 'POST'])
class GasTotal(Resource):
  def get(self, ):
    return 200
    
  def post(self, ):
    print(request.method)
    response = api.payload
    print(api.payload)
    wallet = 'https://bscscan.com/txs?a={wallet}&ps={perPage}&p={page}'.format(wallet=response['wallet'], perPage=response['perPage'], page=response['page'])
    req = urllib.request.Request(wallet, headers={'User-Agent': 'Mozilla/5.0'})
    page = urllib.request.urlopen(req).read()
    webpage = page.decode('utf-8')
    soup = BeautifulSoup(page, 'html5lib')
    list_item = soup.find_all('span', attrs={'class': 'small text-secondary'})
    def gasTotal():
      total = 0
      for item in list_item:
        if item.text == '' or len(item.text) > 43:
          pass
        else:
          total = total + float(item.text)
      print(total)
      return total
    return gasTotal(), 200
    