# Multilingual-NLP-for-Islamic-Theology

This is a Data Driven Theological App that uses Cross Lingual  sentence embeddings for making search engines for Holy Quran and Sahih Hadiths

# Understanding the problem

The aim of this project is to develop a search engine that will take input query for Holy Quran and Sahih Hadiths from any language like arabic,hindi,bangla,english etc (it also supports code mixed language input like mixture of english and arabic in input query) and provide output in english and in bangla language separately. this is an asymmetric semantic search problem.means, you usually have a short query (like a question or some keywords) and you want to find a longer paragraph answering the query. 

# Supported Languages:

Afrikaans, Albanian, Amharic, Arabic, Armenian, Aymara, Azerbaijani, Basque, Belarusian, Bengali, Berber languages, Bosnian, Breton, Bulgarian, Burmese, Catalan, Central/Kadazan Dusun, Central Khmer, Chavacano, Chinese, Coastal Kadazan, Cornish, Croatian, Czech, Danish, Dutch, Eastern Mari, English, Esperanto, Estonian, Finnish, French, Galician, Georgian, German, Greek, Hausa, Hebrew, Hindi, Hungarian, Icelandic, Ido, Indonesian, Interlingua, Interlingue, Irish, Italian, Japanese, Kabyle, Kazakh, Korean, Kurdish, Latvian, Latin, Lingua Franca Nova, Lithuanian, Low German/Saxon, Macedonian, Malagasy, Malay, Malayalam, Maldivian (Divehi), Marathi, Norwegian (Bokmål), Occitan, Persian (Farsi), Polish, Portuguese, Romanian, Russian, Serbian, Sindhi, Sinhala, Slovak, Slovenian, Somali, Spanish, Swahili, Swedish, Tagalog, Tajik, Tamil, Tatar, Telugu, Thai, Turkish, Uighur, Ukrainian, Urdu, Uzbek, Vietnamese, Wu Chinese and Yue Chinese.


# Solution/Pipeline

1. we process bangla and english quran with tafsir and sahih bukhari-muslim dataset here -> https://www.kaggle.com/datasets/mobassir/bangla-quran-with-tafsir and here -> https://www.kaggle.com/datasets/mobassir/en-bn-sahih-bukhari-muslim the code used for scraping bangla translated quran and tafsir can be found here -> https://github.com/mnansary/hadith-srcapper
2. Number of bukhari-muslim hadiths and chapters compiled in english language is different in number than bangla compiled hadith version,for that reason we couldn't use english and bangla human translated hadith's together for our task as number of rows are different (hadith orders are different).that's why we translate english hadith's into bangla using meta's nllb-200-1.3B model (ref -> https://ai.facebook.com/research/no-language-left-behind/). code used for english to bangla hadith translation can be found here -> https://github.com/mobassir94/Multilingual-NLP-for-Islamic-Theology/blob/main/demo_notebooks/nllb_en_bn_translator.ipynb

3. we create multilingual laser embeddings(let's call it corpus embedding) in this directory -> https://github.com/mobassir94/Multilingual-NLP-for-Islamic-Theology/tree/main/create%20laserembeddings to learn more about facebook's laser read this -> https://engineering.fb.com/2019/01/22/ai-research/laser-multilingual-sentence-embeddings/

4. Our flask app  takes user's multilingual input,then converts user query into laser embedding(let's call it query embedding)

5. using dot product or pairwise euclidean distance metric measure, we retrive top n (n is user input here, ranges from 1-10) similar rows from our corpus embedding that are closest to query embedding/user's input

# How to install the app?

1. go to terminal and cd to the root directory of this project,then

2. !pip install -r requirements.txt (make sure no error occured)
then,

3. from this google drive link -> https://drive.google.com/drive/folders/1Zw64MRFvQxxwDLYFTdNki7HwNQOM30gy?usp=sharing download these 7 files and store them in assets folder

4. python app.py

5. Now,go to browser and hit -> http://127.0.0.1:33507/

# Future Goals

1. Replace laser2 with laser3
2. improve bangla translation quality with a bangla spell-checker
3. Data Driven Similarity checking between Quran and Bible

# References

1. https://arxiv.org/pdf/1812.10464v2.pdf
2. https://arxiv.org/ftp/arxiv/papers/2207/2207.04672.pdf
3. https://github.com/alizahidraja/QURAN-NLP

"Everything is easy until you work for it" ☺

# Acknowledgements

1. Apsis Solutions Ltd.
2. bengali.ai

