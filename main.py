from web3 import Web3
from datetime import datetime

import requests
import json
import os

# env variables
subnav_address = os.getenv("SUBNAV_ADDRESS", "0x5FbDB2315678afecb367f032d93F642f64180aa3")
network_rpc = os.getenv("NETWORK_RPC", "https://api.avax-test.network/ext/bc/C/rpc")

# connect to the network
w3 = Web3(Web3.HTTPProvider(network_rpc))

# read the contract's abi
with open("artifacts/contracts/SubNav.sol/SubNav.json") as f:
    subnav_json = json.load(f)
subnav_abi = subnav_json["abi"]

# open the contract
contract_instance_subnav = w3.eth.contract(address=subnav_address, abi=subnav_abi)

# get the list of known SubnetIDS
subnet_ids = set(contract_instance_subnav.functions.getSubnetIDs().call())

###################################
url = "https://api.avax-test.network:443/ext/bc/P"
payload = json.dumps({
  "jsonrpc": "2.0",
  "method": "platform.getSubnets",
  "params": {},
  "id": 1
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'AWSALB=xFYw/04P12p5f6LXVPrSAEDZDVofRB3vi+g3PTwgxqfjnN0w22hW6LH/nhyFue4rjkzr+icg1uypMlE1ynYpi1OwN8wwlsBQCsbSS/waLoYlaB8XwlAhpz50ah6Z; AWSALBCORS=xFYw/04P12p5f6LXVPrSAEDZDVofRB3vi+g3PTwgxqfjnN0w22hW6LH/nhyFue4rjkzr+icg1uypMlE1ynYpi1OwN8wwlsBQCsbSS/waLoYlaB8XwlAhpz50ah6Z; __cflb=04dToSvdRcbyfpHwfXTzWXXdEyutfnMxVftyGHzvDJ'
}
response = requests.request("POST", url, headers=headers, data=payload)
response_json = json.loads(response.text)
all_subnet_ids = []
for subnet in response_json['result']['subnets']:
  all_subnet_ids.append(subnet['id'])
# print(all_subnet_ids)
###################################

for subnet_id in all_subnet_ids:
    url = "https://api.avax-test.network:443/ext/bc/P"

    payload = json.dumps({
    "jsonrpc": "2.0",
    "method": "platform.getCurrentValidators",
    "params": {
        "subnetID": subnet_id,
        "nodeIDs": []
    },
    "id": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Cookie': 'AWSALB=ulHwX+Cmg3AgStfEMpf3HQcTUdefUaVJk7G7wNTPSBWRXeBKLGJhy2kRA7VklGm+ziInlmh+iHBcT1R4Gj0vLXMDPfl0/RWEo8QcvwHWDGNojr6dgy2f14kxN3Qd; AWSALBCORS=ulHwX+Cmg3AgStfEMpf3HQcTUdefUaVJk7G7wNTPSBWRXeBKLGJhy2kRA7VklGm+ziInlmh+iHBcT1R4Gj0vLXMDPfl0/RWEo8QcvwHWDGNojr6dgy2f14kxN3Qd; __cflb=04dToSvdRcbyfpHwfXTzWXXdEyutfnMxVftyGHzvDJ'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    
    for subnet_validator in response_json['result']['validators']:
      str = []
      str.append(subnet_validator['nodeID'])
      str.append("stops validating")
      str.append(subnet_id)
      str.append("at")
      str.append(datetime.utcfromtimestamp(int(subnet_validator['endTime'])).strftime('%Y-%m-%d %H:%M:%S'))
      
      print(str)

      # print(subnet_validator)
