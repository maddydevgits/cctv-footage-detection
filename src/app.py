from flask import Flask ,render_template,request,redirect,session
from web3 import Web3,HTTPProvider
import json

def connectWithBlockchain(acc):
    web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
    if acc==0:
        web3.eth.defaultAccount=web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=acc
    
    artifact_path="./build/contracts/CCTVFootage.json"

    with open(artifact_path) as f:
        artifact_json=json.load(f)
        contract_abi=artifact_json['abi']
        contract_address=artifact_json['networks']['5777']['address']
    
    contract=web3.eth.contract(abi=contract_abi,address=contract_address)
    return contract,web3


app = Flask(__name__)
@app.route('/')
def lan():
    return render_template('landing.html')

@app.route('/signup')
def signup():
    return render_template('SelectSignUp.html')

@app.route('/signin')
def signin():
    return render_template('SelectSignIn.html')

@app.route('/govtsignup')
def govtsigup():
    return render_template('GovtSignUpForm.html')

@app.route('/pvtsignup')
def pvtsignup():
    return render_template('PvtSignUpForm.html')

@app.route('/signinform')
def siginform():
    return render_template('SignInForm.html')

@app.route('/pvtsignupform',methods=['post'])
def pvtsignupform():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    repassword=request.form['repassword']
    if(password!=repassword):
        return render_template('PvtSignUpForm.html',err='Passwords didnt matched')
    else:
        try:
            contract,web3=connectWithBlockchain(0)
            tx_hash=contract.functions.addPrivateOfficial(name,email,password).transact()
            web3.eth.wait_for_transaction_receipt(tx_hash)
            return render_template('PvtSignUpForm.html',res='Signup Successful')
        except:
            return render_template('PvtSignUpForm.html',err='Already exist')
    
@app.route('/govtsignupform',methods=['post'])
def govtsignupform():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    repassword=request.form['repassword']
    if(password!=repassword):
        return render_template('GovtSignUpForm.html',err='Passwords didnt matched')
    else:
        try:
            contract,web3=connectWithBlockchain(0)
            tx_hash=contract.functions.addGovernmentOfficial(name,email,password).transact()
            web3.eth.wait_for_transaction_receipt(tx_hash)
            return render_template('GovtSignUpForm.html',res='Signup Successful')
        except:
            return render_template('GovtSignUpForm.html',err='Already exist')


if __name__=="__main__":
    app.run(host='0.0.0.0',port=9001,debug=True)