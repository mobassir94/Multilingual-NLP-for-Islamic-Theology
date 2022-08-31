# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:22:11 2022

@author: MOBASSIR
"""

import numpy as np
import pandas as pd
from laserembeddings import Laser
from metrics import dot_product_similarity,pairwise_euclidean_dists

import site
import shutil
import os
import gdown

# assets folder
url = "https://drive.google.com/drive/folders/1Zw64MRFvQxxwDLYFTdNki7HwNQOM30gy?usp=sharing"

id = "1Zw64MRFvQxxwDLYFTdNki7HwNQOM30gy"

loc = site.getsitepackages() 
root = site.getusersitepackages()
data_path = loc[0]+'/laserembeddings/data'

gdown_infer = True

if not os.path.exists(data_path):
    data_path = root+'/laserembeddings/data'

if(not gdown_infer):
    files = os.listdir(data_path)
    if(len(files)<3):
        print("online...")
        os.system('python -m laserembeddings download-models')
else: 
    files = os.listdir('./assets/')

    if(len(files)<7):
        print("downloading necessary files....")
        gdown.download_folder(id=id, quiet=True, use_cookies=False)    
    shutil.copy('./assets/93langs.fcodes', data_path)
    shutil.copy('./assets/93langs.fvocab', data_path)
    shutil.copy('./assets/bilstm.93langs.2018-12-26.pt', data_path)
print("copy done...")
laser = Laser()

corpus_emb_quran = np.load('./assets/Holy_Quran_mlt_emb.npy')
corpus_emb_hadith = np.load('./assets/en_emb_bukhari_muslim.npy')

en_bn_bukhari_muslim = pd.read_csv('./assets/en_bn_bukhari_muslim.csv')
en_bn_quran_tafsir = pd.read_csv('./assets/en_bn_quran_tafsir.csv')

def MLT_Sahih_Hadith_Search_Engine(query,size=1,language = 'en',metric = 'dot',query_embedding=None):

    if(metric == 'dot'):
        query_embedding = np.squeeze(np.asarray(query_embedding))
        linear_similarities = dot_product_similarity(corpus_emb_hadith, query_embedding)
    else:
        linear_similarities = pairwise_euclidean_dists(corpus_emb_hadith, query_embedding)
        linear_similarities = np.squeeze(np.asarray(linear_similarities))
        linear_similarities = np.array(linear_similarities, dtype=np.float32)

    if(metric == 'dot'):
        Top_index_doc = linear_similarities.argsort()[:-(size+1):-1]
    else:
        Top_index_doc = linear_similarities.argsort()[:-(size+1):]
        Top_index_doc = Top_index_doc[:size]

    linear_similarities.sort()
    find = pd.DataFrame()
    for i,index in enumerate(Top_index_doc):
        find.loc[i,'source'] = str(en_bn_bukhari_muslim['source'][index])
        find.loc[i,'chapter_no'] = str(en_bn_bukhari_muslim['chapter_no'][index])
        find.loc[i,'hadith_no'] = str(en_bn_bukhari_muslim['hadith_no'][index])
        find.loc[i,'chapter'] = str(en_bn_bukhari_muslim['chapter'][index])
        find.loc[i,'text_ar'] = str(en_bn_bukhari_muslim['text_ar'][index])
        find.loc[i,'text_en'] = str(en_bn_bukhari_muslim['text_en'][index])
        find.loc[i,'text_bn'] = str(en_bn_bukhari_muslim['text_bn'][index])
        find.loc[i,'narrators'] = str(en_bn_bukhari_muslim['narrators'][index])
        

    for j,simScore in enumerate(linear_similarities[:-(size+1):-1]):
        find.loc[j,'Score'] = simScore
 
    return find

def Multilingual_Quran_Hadith_Search_Engine(query,size=1,language = 'en',metric = 'dot',n_hadith = 1):

    query_embedding = laser.embed_sentences(query, lang=language)

    mlt_hadiths = MLT_Sahih_Hadith_Search_Engine(query,size=n_hadith,language = 'en',metric = metric,query_embedding=query_embedding)
    
    if(metric == 'dot'):
        query_embedding = np.squeeze(np.asarray(query_embedding))
        linear_similarities = dot_product_similarity(corpus_emb_quran, query_embedding)
    else:
        linear_similarities = pairwise_euclidean_dists(corpus_emb_quran, query_embedding)
        linear_similarities = np.squeeze(np.asarray(linear_similarities))
        linear_similarities = np.array(linear_similarities, dtype=np.float32)

    if(metric == 'dot'):
        Top_index_doc = linear_similarities.argsort()[:-(size+1):-1]
    else:
        Top_index_doc = linear_similarities.argsort()[:-(size+1):]
        Top_index_doc = Top_index_doc[:size]

    linear_similarities.sort()
    find = pd.DataFrame()
    
    for i,index in enumerate(Top_index_doc):
        find.loc[i,'Name'] = str(en_bn_quran_tafsir['Name'][index])
        find.loc[i,'Surah'] = str(en_bn_quran_tafsir['Surah'][index])
        find.loc[i,'Ayat'] = str(en_bn_quran_tafsir['Ayat'][index])
        find.loc[i,'Verse'] = str(en_bn_quran_tafsir['Verse'][index]) 
        find.loc[i,'Tafseer'] = str(en_bn_quran_tafsir['Tafseer'][index]) 
        find.loc[i,'ar_text'] = str(en_bn_quran_tafsir['ar_text'][index])
        #bangla....
        find.loc[i,'আল_বায়ান'] = str(en_bn_quran_tafsir['আল_বায়ান'][index])
        find.loc[i,'tafsir_bayan'] = str(en_bn_quran_tafsir['tafsir_bayan'][index])
        

    for j,simScore in enumerate(linear_similarities[:-(size+1):-1]):
        find.loc[j,'Score'] = simScore
 
    return find,mlt_hadiths
    
    
    
