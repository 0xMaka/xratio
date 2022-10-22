import requests                                                        
from math import log2

from web3 import Web3
from os import getenv
from dotenv import load_dotenv

from time import sleep
import datetime

load_dotenv()
w3 = Web3(Web3.HTTPProvider(getenv('ETH')))

# Block pre state change 1:1
GEN_STATE = 10829343
# Fist state change 0.9999829783958324374770147392967674:1.000017021893907502798742018910183
FIRST_STATE = 10829344
# extremely rough
AVERAGE_BLOCKS_PER_DAY = 6500

current = w3.eth.block_number

q = '''
{   
  xsushi(id: "xSushi", block: {number: NUM}) {     
    xSushiSushiRatio     
    sushiXsushiRatio   
  } 
}
'''
                                                                                         
def run_query(q):                                                                        
  request = requests.post(                                                               
    'https://api.thegraph.com/subgraphs/name/sushi-labs/xsushi'                   
    '',                                                                            
    json={'query': q}
  )                                                         
  if request.status_code == 200:                                                         
    return request.json()                                                                
  else:                                                                                  
    raise Exception(f'Query failed. return code is {request.status_code}. {q}')

def quotient(n, m):
  return (n >> (int)(log2(m)))

def remainder(n, m):
  return ((n) &(m-1))

def main():

  start = GEN_STATE
  step = AVERAGE_BLOCKS_PER_DAY * 7
  width = current - start
  stop = start + (width - remainder(width, step))

  with open(f'ratio.md', 'w') as f:
    f.write('|  Block   |          xSushiSushiRatio            |           sushiXsushiRatio          |          Date          |\n')
    f.write('|----------|--------------------------------------|-------------------------------------|------------------------|\n')

    for i in range(start,stop,step):
      try:
        r = run_query(q.replace('NUM', str(i)))
        s = w3.eth.getBlock(i)['timestamp']
        sleep(3)
      except:
        sleep(5)
      print(datetime.fromtimestamp(stamp).strftime('%d-%m-%y'))
      f.write(f"| {i} | {v['xSushiSushiRatio']} | {v['sushiXsushiRatio']} | {datetime.fromtimestamp(s).strftime('%d-%m-%y')}|\n")
if __name__ == '__main__':
  main()
