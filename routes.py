from startup import app
from flask import render_template, request, jsonify
import re
import rpc

DISABLED_METHODS = [
    'setban',
    'issue',
    'issuequalifierasset',
    'issuerestrictedasset',
    'reissuerestrictedasset',
    'issueunique',
    'reissue',
    'transfer',
    'transferfromaddress',
    'transferfromaddresses',
    'clearmempool',
    'generate',
    'generatetoaddress',
    'getgenerate',
    'setgenerate',
    'getmywords',
    'dumpprivkey',
    'dumpwallet',
    'purgesnapshot',
    'settxfee',
    'sendfromaddress',
    'sendtoaddress',
    'sendmany',
    'sendfrom',
    'sendmessage',
    'transferqualifier'
]

DEFAULT_PARAMS = {
    '':{}
}

@app.route('/<address>/balance', methods=['GET'])
def evrmore_balance(address):
    return jsonify(rpc.send("getaddressbalance", [{'addresses':[address]}]))

@app.route('/evrmore/<command>', methods=['GET', 'POST'])
def evrmore_command(command):

    if command in DISABLED_METHODS:
        return jsonify({'error': 'This method is disabled.'}), 403

    params = try_get_json()
    if params is not list:
        print("Params are not a list")

    result = rpc.send(command, params)
    return jsonify(result)
    
def try_get_json():
    try:
        params = request.json if request.json is not None else []
        return params
    except Exception as e:
        return None

def list_commands():
    commands_pattern = re.compile(r'(?m)^[a-z][a-z]*', re.M)
    help_text = rpc.send("help")
    return re.findall(commands_pattern, help_text)

def parse_name(help_text):
    name = (re.search(r'^([a-z]+)?\s', help_text)).group(1) # WORKING! DONT CHANGE THIS
    return name
def parse_desc(help_text):
    try:
        desc = (re.search(r'(\n.+?\n)', help_text)).group(1).strip().replace('Result:','').replace('Arguments:','')
    except Exception:
        try:
            desc = (re.search(r'(\n.+)', help_text)).group(1).strip().replace('Result:','').replace('Arguments:','')
        except Exception:
            desc = (re.search(r'(.+)', help_text)).group(1).strip()
    finally:
        return desc
def parse_args(help_text):
    arguments = re.search(r'\nArguments:((\n.+)+)', help_text)
    try:
        return arguments.group(1).strip()
    except Exception:
        return None
def parse_results(help_text):
    results = re.search(r'\nResult:(.*((\n.+)+))?Example', help_text, re.DOTALL)
    try:
        return results.group(1).strip()
    except Exception:
        return None
def parse_examples(help_text):
    examples = re.search(r'\nExample.*((\n.*)+)', help_text)
    try:
        return examples.group(1).strip()
    except Exception:
        return None 
    








