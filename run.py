from flask import Flask, escape, request,jsonify
import pandas as pd
import time
import csv
import json
app = Flask(__name__)
data2=pd.read_csv("combined.csv")
data2=data2.values.tolist()


@app.route('/',methods=['POST','GET'])
def run():
    return "i am running in heroku"

@app.route('/api',methods=['POST','GET'])
def hello():
        i=0
        d=[]
        dd=request.json        
        # print(dd['queryResult'] ['queryText'])
        # send = request.args.get('arg')
        send=dd['queryResult'] ['queryText']
        print(send,"*************")
        try:
            i=0
            for data in data2:
                i=i+1
                send=send.lower()
                data[3]=data[3].lower()
                if send in data[3]:
                    if(data2[i][2]=="Bestiee "):
                        # print(data2[i],i+1)
                        # d.append(data)  
                        d.append(data2[i][3])            
            
        except:
            pass
        if(len(d)!=0):
            reply = {
                "fulfillmentText": d[0],
            }
            print(reply)
            return jsonify(reply)
        else:
            reply = {
                "fulfillmentText": "enti"
            }
            return jsonify(reply)
if __name__ == '__main__':
    app.run(debug=True)

