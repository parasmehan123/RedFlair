# Red-Flair
## Table Of Content.
1. [Introduction]
2. [How to Use the App]
3. 

## Introduction
Red-Flair is a flair detector for posts belonging to [r/india](https://www.reddit.com/r/india/) subreddit on Reddit. Its web app is deployed using Heroku which can be accessed [here](http://redflair.herokuapp.com). It scrapes post's using the URL and then uses an SVM model to predict the flair of that post.

## How to Use the App 
### Steps to use the Web-app to predict flairs of posts.
1. Open the app at [Red-Flair](http://redflair.herokuapp.com).
![](images/1.png)

2. Open the reddit post belongin to [r/india](https://www.reddit.com/r/india/) subreddit. Copy the full URL of the post. 
![](images/2.png)

3. Paste the Link in the Url Box and click submit. 
![](images/3.png)

4. This will redirect you to [Flairs Detected](http://redflair.herokuapp.com/Flair_Detected) Page. Here it will display your submitted URL on the top, and the flair that has been predected. By clicking on the link which is highlighted in blue, it would re-direct to the URL which was submitted earlier.
![](images/4.png))

## Directory Structure
<pre>
RedFlair
├── data
│   ├── csv_files
│   └── mongodb
├── images
├── others
├── static
└── templates
</pre>
* / : It contains all the files and directories.
  * app.py : The Main Python file for Flask Based Web App.
  * forms.py : A Python file for taking input from the user using Flask-WTF library.
  * model : A Pickled-version of ML model which is used to make predictions.
  * model.py : A Python file for predicting Flair.
  * nltk.txt : A txt file for Heroku for downloading "stopwords","wordnet","punkt" which are used for data cleaning.
  * Procfile : A file which contains the command which are required to run the flask based app on Heroku.
  * requirements.txt : A txt file for Heroku to satisfy the requirements to run the web app.
  * tfidf : A Pickled-version of TF-IDF VECTORIZER for converting words into vectors.
* Data : It contains all the data used in the project.
  * csv_files : It contains the data in .csv files.
  * mongodb : It contains the data in .json and .bson (mongodb instance) form.
* images : It contains all the images used to create this README.md
* others : It contains the .ipynb files which are used for scraping data, cleaning data, combining data, training various models and analysing data. 
* static : It contains the .css files for the web-app.
* templates : It contains the .html files for the web-app.

## Steps To Run Red-Flair on Local System.
### For Hosting Red-Flair on Local Host
1. Clone The Repository.
```bash
git clone https://github.com/parasmehan123/RedFlair.git
```
2. change directory to RedFlair.
```bash
cd RedFlair
```
3. Run the app.py file.
```bash
python3 app.py
```
### For Re-training the model or data-analysis or data-scarping or data-combining.
1. Clone The Repository.
```bash
git clone https://github.com/parasmehan123/RedFlair.git
```
2. change directory to RedFlair.
```bash
cd RedFlair
```
3. Copy and Paste the .ipynb files from ./others/  to ./data/csv_files
```bash
cp ./others/<file>.ipynb ./data/csv_files
```
4. Open Jupyter 
``` bash
jupyter notebook
```
5. Go the the .ipynb file in /data/csv_files and select Cell > "Run All".
6. Copy paste the "model" and "tfidf" files back to /RedFlair for using it on the web app.

## Dependicies
* Flask==1.0.2
* Flask-WTF==0.14.2
* jupyter==1.0.0
* nltk==3.4
* numpy==1.16.2
* pandas==0.24.2
* praw==6.3.1
* prawcore==1.0.1
* scikit-image==0.14.2
* scikit-learn==0.20.3
* WTForms==2.2.1
* xgboost==0.90

## Project Approach
### Data Acquisition 
For data acquisition I've used 2 Methods.
### 1. Using Praw Library :
Using Python Praw library, I was able to scrape around 1800 posts for eleven flairs, using a simple API calls. The code for data scraping is saved in [data_scraping.ipynb](/others/data_scraping.ipynb) and the data is in [data.csv](/data/csv_files/data.csv).

### 2. Using Database on Google Big-Query.
I've found a database containing Reddit posts on google big-query.
Using the below SQL query I've been able to scrape data of 16000 posts belonging to 8 flair categories from January, February, and March 2019. I searched way back till 2017, but couldn't find posts belonging to Political, AMA, Finance/Business flair types, in the database.
```SQL

SELECT *
FROM [fh-bigquery:reddit_posts.2019_01],[fh-bigquery:reddit_posts.2019_02],[fh-bigquery:reddit_posts.2019_03]
WHERE subreddit == "india" && link_flair_text == "flair" 
LIMIT 20000
```

## Analysis of Data
* Table of number of posts in each flair category in the data that is analysed.

| Flair     | No.of Posts |
|:--------- |:------------|
| Political | 246         |
| Non-Political | 6026 |
|[R]eddiquette|1176|
|AskIndia|5399|
|Science/Technology|1169|
|Policy/Economy|1205|
|Finance/Business|171|
|Sports|430|
|Food|305|
|Photography|507|
|AMA|210|

### Flair Wise Analysis [Link](http://redflair.herokuapp.com/data1)
* Multi-Bar Chart for analysing average/median, scores/comments of posts belonging to different flairs.
![](images/5.png)

* Bar charts for analysing hour of the day at which post of different flairs are posted.
![](images/6.png)
![](images/7.png)
![](images/8.png)

### Content Analysis [Link](http://redflair.herokuapp.com/data2)
* Bar Charts for analysis frequency of words in the title of posts in different flairs categories. 
![](images/9.png)
![](images/10.png)
![](images/11.png)

## Sources
* For Data-Scraping:
  * https://bigquery.cloud.google.com/table/fh-bigquery:reddit_posts.2019_02?pli=1
  * http://www.storybench.org/how-to-scrape-reddit-with-python/
* For D3.js Bar Charts:
  * http://bl.ocks.org/jonahwilliams/2f16643b999ada7b1909
  * https://bl.ocks.org/curran/af72fd9c1fb61d2133d273cd8a3ca557
