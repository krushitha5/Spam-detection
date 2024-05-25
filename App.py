From flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import gunicorn


app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def hello_world():
    return render_template('new.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    message=request.form['message']
    print(message)
    # new=model.classify(message)
    pbs,pbns,res=model.classify(message)

    # return render_template('index.html',pred='The probability of given data to be spam is {}\n The probability of given data to be ham is {} \n Hence Given data is {}'.format(pbs,pbns,res))
    
    return render_template('new.html',pred='The probability of given data to be spam is {}'.format(pbs),
                           pred1='The probability of given data to be ham is {} '.format(pbns),
                           pred2='Hence Given Data is {}'.format(res))


    # return render_template('index.html',pred='The resultant decision is {} {} {}'.format(pbs,pbns,res))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
