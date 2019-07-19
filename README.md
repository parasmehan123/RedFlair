https://bigquery.cloud.google.com/table/fh-bigquery:reddit_posts.2019_02?pli=1
https://bigquery.cloud.google.com/table/fh-bigquery:reddit_posts.2019_03?pli=1
2019_04

SELECT *
FROM [fh-bigquery:reddit_posts.2019_02]
WHERE subreddit == "india" && ( link_flair_text == "Political" || link_flair_text == "Non-Political" || link_flair_text == "AskIndia" || link_flair_text == "Reddiquette" || link_flair_text == "Science & Technology" || link_flair_text == "Policy & Economy" || link_flair_text == "Finance & Business" || link_flair_text == "Entertainment" || link_flair_text == "Sports" || link_flair_text == "Food" || link_flair_text == "Photography" || link_flair_text == "AMA")
LIMIT 20000