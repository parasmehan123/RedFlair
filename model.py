from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import praw
import string
import pickle

tf=pickle.load(open('tfidf','rb'))

stemmer = WordNetLemmatizer()


def stopwords_removal(tokens):
    stop_words = list(stopwords.words("english"))
    filtered_sentence = [w for w in tokens if not w in stop_words]              
    final=' '.join(filtered_sentence)
    return final

def remove_punctuation(text):
    obj=str.maketrans('', '',string.punctuation)
    answer=text.translate(obj)
    return answer

def simple_lemma(data):
    lemmatizer = WordNetLemmatizer()
    filtered=[lemmatizer.lemmatize(word) for word in data.split()]
    text = ' '.join(filtered)
    return text

def pre_process(x,flag):
    for i in range(len(x)):
        if x[i]!='nan':
            if flag:
                x[i]=x[i].split('/')
                x[i]=' '.join(x[i])
            x[i]=simple_lemma(remove_punctuation(stopwords_removal(word_tokenize(str(x[i]).lower()))))
        else:
            x[i]=''
    return x

    
flair_dict={0:'Political',1:'Non-Political',2:'[R]eddiquette',3:'AskIndia',4:'Science/Technology',5:'Policy/Economy',6:'Finance/Business',7:'Sports',8:'Food',9:'Photography',10:'AMA'}

clf = pickle.load(open('model','rb')) 

def get_flair(u):
    reddit=praw.Reddit(client_id='ST0obmq3HAomHQ',client_secret='ECeazJYbpZ5Kx83g6RrWPDyPO0A',user_agent='Precog Project',username='parasmehan123',password='')
    s=reddit.submission(url=u)
    bo=[s.selftext]
    ti=[s.title]
    ur=[s.url]
    pre_process(ti,False)
    pre_process(bo,False)
    pre_process(ur,True)
    text=[ti[0]+' '+bo[0]+' '+ur[0]]
    # print(text)
    return flair_dict[clf.predict(tf.transform(text))[0]]