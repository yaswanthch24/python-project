from google.colab import drive
drive.mount('/content/drive')

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)



medicines = pd.read_csv('/content/drive/MyDrive/Drug Recomendation/medicine.csv')

medicines.head()

medicines.shape

medicines.isnull().sum()

medicines.dropna(inplace=True)

medicines.duplicated().sum()

medicines['Description']

a = medicines['Reason'].unique()
a

len(a)

medicines['Description'].apply(lambda x:x.split())

medicines['Reason'] = medicines['Reason'].apply(lambda x:x.split())
medicines['Description'] = medicines['Description'].apply(lambda x:x.split())

medicines['Description'] = medicines['Description'].apply(lambda x:[i.replace(" ","") for i in x])

medicines['Description'] = medicines['Description'].apply(lambda x:[i.replace(" ","") for i in x])

medicines['tags'] = medicines['Description'] + medicines['Reason']

new_df = medicines[['index','Drug_Name','tags']]

new_df

new_df['tags'].apply(lambda x:" ".join(x))

new_df

new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))

new_df

new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())

new_df
pip install nltk

import nltk

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(stop_words='english',max_features=5000)

def stem(text):
  y = []

  for i in text.split():
    y.append(ps.stem(i))

  return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

cv.fit_transform(new_df['tags']).toarray().shape

vectors = cv.fit_transform(new_df['tags']).toarray()

from sklearn.metrics.pairwise import cosine_similarity

cosine_similarity(vectors)

similarity = cosine_similarity(vectors)

similarity[1]

def recommend(medicine):
    medicine_index = new_df[new_df['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in medicines_list:
        print(new_df.iloc[i[0]].Drug_Name)


recommend("Paracetamol 125mg Syrup 60mlParacetamol 500mg Tablet 10'S")

recommend("A CN Gel(Topical) 20gmA CN Soap 75gm")

recommend("T Muce Ointment 5gm")