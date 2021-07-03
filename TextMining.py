########################Task 1 - Snapdeal#####################################

#Packages needed
import requests 
from textblob import TextBlob# Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 
from wordcloud import WordCloud
import nltk
import nltk.corpus
from nltk.corpus import stopwords


#Extracting reviews from snapdeal website
lenovo_snapdeal=[]
url1 = "https://www.snapdeal.com/product/lenovo-a7000-8-gbwhite/660909822842/reviews?page="
url2 = "&sortBy=HELPFUL"

for i in range(1,10):
  ip=[]  
  base_url = url1+str(i)+url2
  response = requests.get(base_url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  temp = soup.findAll("div",attrs={"class","user-review"})# Extracting the content under specific tags  
  for j in range(len(temp)):
    ip.append(temp[j].find("p").text)
  lenovo_snapdeal=lenovo_snapdeal+ip  # adding the reviews of one page to empty list which in future contains all the reviews

#DATA PREPROCESSING AND CLEANING

#Removing repeated reviews 
lenovo_snapdeal = list(set(lenovo_snapdeal))

# Writing reviews into text file 
with open("ip_snapdeal.txt","w",encoding="utf-8") as snp:
    snp.write(str(lenovo_snapdeal))
    
# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(lenovo_snapdeal)

# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ",ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ",ip_rev_string)

# words that contained in lenovo reviews
ip_reviews_words = ip_rev_string.split(" ")

stoplist = stopwords.words('english')

with open("C:/Users/hp/Desktop/python codes/stop.txt","r") as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")

#removing stop words
ip_reviews_words = [w for w in ip_reviews_words if not w in stoplist]

# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)

# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(ip_rev_string)
token

# finding the frequency distinct in the tokens
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(token)
fdist

# To find the frequency of top 10 words
fdist1 = fdist.most_common(10)
fdist1

# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()

# Importing Lemmatizer library from nltk and lemmatizing the data
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
ip_rev_string = lemmatizer.lemmatize(ip_rev_string)

#Parts of speech tagging and printing POST
for toke in token:
  print(nltk.pos_tag([toke]))


#Named entity recognition
#importing chunk library from nltk
from nltk import ne_chunk
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
tags = nltk.pos_tag(token)
chunk = ne_chunk(tags)
chunk

#Sentimental ANALYSIS 

wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)

#IMPORT POSITIVE WORD FILE
with open("C:/Users/hp/Desktop/python codes/datasets/positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
#IMPORT NEGATIVE WORD FILE
with open("C:/Users/hp/Desktop/python codes/datasets/negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

# Positive word cloud
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in ip_reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_pos_in_pos)

plt.imshow(wordcloud_pos_in_pos)

# negative word cloud
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in ip_reviews_words if w in negwords])
wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_neg_in_neg)

plt.imshow(wordcloud_neg_in_neg)

#########################################TASK 1 - Amazon###############################
#Packages needed
import requests 
from textblob import TextBlob# Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 
from wordcloud import WordCloud
import nltk
import nltk.corpus
from nltk.corpus import stopwords


#Extracting reviews from snapdeal website
alexa_amazon=[]


for i in range(1,20):
  ip=[]  
  
  url = "https://www.amazon.in/Echo-Dot-3rd-Gen/product-reviews/B07PFFMP9P/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber="+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})# Extracting the content under specific tags  
  for j in range(len(reviews)):
    ip.append(reviews[j].text)  
  alexa_amazon=alexa_amazon+ip  # adding the reviews of one page to empty list which in future contains all the reviews
  # adding the reviews of one page to empty list which in future contains all the reviews

#DATA PREPROCESSING AND CLEANING

#Removing repeated reviews 
alexa_amazon = list(set(alexa_amazon))

# Writing reviews into text file 
with open("ip_amazon.txt","w",encoding="utf-8") as snp:
    snp.write(str(alexa_amazon))
    
# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(alexa_amazon)

# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ",ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ",ip_rev_string)

# words that contained in lenovo reviews
ip_reviews_words = ip_rev_string.split(" ")

stoplist = stopwords.words('english')

with open("E:/DATA SCIENCE ASSIGNMENT/Class And Assignment Dataset/class/Text Mining(NLP)/stopwords_en.txt","r") as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")

#removing stop words
ip_reviews_words = [w for w in ip_reviews_words if not w in stoplist]

# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)

# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(ip_rev_string)
token

# finding the frequency distinct in the tokens
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(token)
fdist

# To find the frequency of top 10 words
fdist1 = fdist.most_common(10)
fdist1

# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()

# Importing Lemmatizer library from nltk and lemmatizing the data
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
ip_rev_string = lemmatizer.lemmatize(ip_rev_string)

#Parts of speech tagging and printing POST
for toke in token:
  print(nltk.pos_tag([toke]))


#Named entity recognition
#importing chunk library from nltk
from nltk import ne_chunk
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
tags = nltk.pos_tag(token)
chunk = ne_chunk(tags)
chunk

#Sentimental ANALYSIS 
wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)

#IMPORT POSITIVE WORD FILE
with open("E:/DATA SCIENCE ASSIGNMENT/Class And Assignment Dataset/class/Text Mining(NLP)/positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
#IMPORT NEGATIVE WORD FILE
with open("E:/DATA SCIENCE ASSIGNMENT/Class And Assignment Dataset/class/Text Mining(NLP)/negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

# Positive word cloud
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in ip_reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_pos_in_pos)

plt.imshow(wordcloud_pos_in_pos)

# negative word cloud
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in ip_reviews_words if w in negwords])
wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_neg_in_neg)

plt.imshow(wordcloud_neg_in_neg)

############################################TASK 2 - IMDB#################################
from selenium import webdriver

# below code opens the chrome browser
#download latest version of chromebrowser.exe from https://sites.google.com/a/chromium.org/chromedriver/home
#store downloaded file in C:\\webdrivers
browser = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe") 
from bs4 import BeautifulSoup as bs

#Black Panther Movie
page= "https://www.imdb.com/title/tt1825683/reviews?ref_=tt_ov_rt"
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementNotVisibleException


browser.get(page)
import time
reviews = []
i=1
# Below while loop is to load all the reviews into the browser till load more button dissapears
while (i>0):
    #i=i+25
    try:
        # Storing the load more button page xpath which we will be using it for click it through selenium 
        # for loading few more reviews
        button = browser.find_element_by_xpath('.collapsable+ .collapsable .show-more__control') # //*[@id="load-more-trigger"]
        button.click()
        time.sleep(5)
    except NoSuchElementException:
        break
    except ElementNotVisibleException:
        break

# Getting the page source for the entire imdb after loading all the reviews
ps = browser.page_source 
#Converting page source into Beautiful soup object
soup=bs(ps,"html.parser")

#Extracting the reviews present in div html_tag having class containing "text" in its value
reviews = soup.findAll("div",attrs={"class","text"})
for i in range(len(reviews)):
    reviews[i] = reviews[i].text
 

# Creating a data frame 
import pandas as pd
movie_reviews = pd.DataFrame(columns = ["reviews"])
movie_reviews["reviews"] = reviews

movie_reviews.to_csv("movie_reviews.csv",encoding="utf-8")

reviews_panther = ' '.join(reviews)

import re
from nltk.corpus import stopwords

# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ",reviews_panther).lower()
ip_rev_string = re.sub("[0-9" "]+"," ",reviews_panther)

# words that contained in iphone XR reviews
ip_reviews_words = ip_rev_string.split(" ")

#TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer(ip_reviews_words,use_idf=True,ngram_range=(1, 3))
X=vectorizer.fit_transform(ip_reviews_words)

with open("C:/Users/hp/Desktop/python codes/stop.txt","r") as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")

ip_reviews_words = [w for w in ip_reviews_words if not w in stopwords]


# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)

# Simple word cloud
##plotting wordcloud on TFIDF
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)

# positive words # Choose the path for +ve words stored in system
with open("C:/Users/hp/Desktop/python codes/datasets/positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")

# negative words  Choose path for -ve words stored in system
with open("C:/Users/hp/Desktop/python codes/datasets/negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

# Positive word cloud
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in ip_reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_pos_in_pos)

plt.imshow(wordcloud_pos_in_pos)

# negative word cloud
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in ip_reviews_words if w in negwords])

wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_neg_in_neg)

plt.imshow(wordcloud_neg_in_neg)

###################################TASK 2 - Tesla review############################
from selenium import webdriver

# below code opens the chrome browser
#download latest version of chromebrowser.exe from https://sites.google.com/a/chromium.org/chromedriver/home
#store downloaded file in C:\\webdrivers
browser = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe") 
from bs4 import BeautifulSoup as bs

#Tesla car review
page= "https://www.cardekho.com/tesla/model-s/user-reviews"
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import ElementNotVisibleException


browser.get(page)
import time
reviews = []
i=1
# Below while loop is to load all the reviews into the browser till load more button dissapears
while (i>0):
    try:
        # Storing the load more button page xpath which we will be using it for click it through selenium 
        # for loading few more reviews
        button = browser.find_element_by_xpath('.contentspace') # //*[@id="load-more-trigger"]
        button.click()
        time.sleep(5)
    except NoSuchElementException:
        break
    except ElementNotVisibleException:
        break

# Getting the page source for the entire imdb after loading all the reviews
ps = browser.page_source 
#Converting page source into Beautiful soup object
soup=bs(ps,"html.parser")

#Extracting the reviews present in div html_tag having class containing "text" in its value
reviews = soup.findAll("div",attrs={"class","contentspace"})
for i in range(len(reviews)):
    reviews[i] = reviews[i].text
 

# Creating a data frame 
import pandas as pd
car_reviews = pd.DataFrame(columns = ["reviews"])
car_reviews["reviews"] = reviews

car_reviews.to_csv("car_reviews.csv",encoding="utf-8")

reviews_tesla = ' '.join(reviews)

import re
from nltk.corpus import stopwords

# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ",reviews_tesla).lower()
ip_rev_string = re.sub("[0-9" "]+"," ",reviews_tesla)

# words that contained in iphone XR reviews
ip_reviews_words = ip_rev_string.split(" ")

#TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer(ip_reviews_words,use_idf=True,ngram_range=(1, 3))
X=vectorizer.fit_transform(ip_reviews_words)

with open("C:/Users/hp/Desktop/python codes/stop.txt","r") as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")

ip_reviews_words = [w for w in ip_reviews_words if not w in stopwords]


# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)

# Simple word cloud
##plotting wordcloud on TFIDF
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)

# positive words # Choose the path for +ve words stored in system
with open("C:/Users/hp/Desktop/python codes/datasets/positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")

# negative words  Choose path for -ve words stored in system
with open("C:/Users/hp/Desktop/python codes/datasets/negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

# Positive word cloud
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in ip_reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_pos_in_pos)

plt.imshow(wordcloud_pos_in_pos)

# negative word cloud
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in ip_reviews_words if w in negwords])

wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_neg_in_neg)

plt.imshow(wordcloud_neg_in_neg)

#####################################END#########################################