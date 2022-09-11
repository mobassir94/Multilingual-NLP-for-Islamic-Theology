# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 11:39:33 2022

@author: MOBASSIR
"""
from flask import Flask, render_template, url_for, request
import pandas as pd


# Cleaning the texts
#import re
from inference_utils import Multilingual_Quran_Hadith_Search_Engine
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
  
    if request.method == 'POST':
        query = request.form['comment']
    n_quran = int(request.form.get('show_quran_top_results'))
    n_hadith = int(request.form.get('show_hadith_top_results'))

    if request.form.get('predict'):
        mlt_quran,mlt_hadiths =Multilingual_Quran_Hadith_Search_Engine(query,size=n_quran,language = 'en',metric = 'dot',n_hadith=n_hadith)
    elif request.form.get('predict1'):
        mlt_quran,mlt_hadiths = Multilingual_Quran_Hadith_Search_Engine(query,size=n_quran,language = 'en',metric = 'l2',n_hadith=n_hadith)
     
        
        
    return render_template('result.html', prediction=mlt_quran,prediction1=mlt_hadiths)

if __name__ == '__main__':
    app.run(debug=False, port=33507)


