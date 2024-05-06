The attached file tokenGen.py takes string input from the user. That string is tokenized and then has the stop words filtered out.

This module requires nltk be downloadad (pip install).

Nltk is dependent on the data in the 'nltk_data' folder that should created in C:/nltk_data on Windows or /usr/local/share/nltk_data on Mac with subfolders 'corpus' and 'tokenizers'. To download the data visit https://www.nltk.org/nltk_data/ and download Stopwords Corpus and unzip into the nltk_data/corpus folder and download Punkt Tokenizer Models and unzip into the nltk_data/tokenizers folder.