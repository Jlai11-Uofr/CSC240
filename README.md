# FaceOff-Polarzing-Opinions-on-use-of-Masks-


Code behind the Paper Face-Off. Full Paper is in Repo!
FaceOff.pdf

In order to run this. Please obtain your own Twitter API Keys from https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens

If you are unable to do so, I have provided two open keys in client1 and client2.

Please DO NOT abuse these twitter accounts as these are my OWN.


The goal of this paper is to analyze sentiment toward face masks in the U.S across a 3 week time period March 22 - April 13.

This was done by using Twitter tweets as our main source of data. Due to large sizes of the JSON objects, Tweet data can be gathered in two ways

Using Tweet_Ids from a public database and using our Tweetinformation.py file. This results in a HUGE JSON file for each tweets.



If you wish to stream Data contonously use our Streaming.py and modify to get the appropiate fields. Will output to CSV
https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object 
Summary of tweet object here.



Sentiment Analysis was used using a rule based lexicon tool that is attuned to emjojis,slang, and social media type text.
Text was pre-processed for removing upper cases, hashtags,@, links, and various things. Improving performance of college classfication 
might also be to implement speech tagging using NLTK.


M3inference.py produces Age/Gender from twitter userobject  ( extracted from JSON or CSV)

Race Produces Race  twitter userobject ( extracted from JSON or CSV)

College Classifcation.py needs a training set. Due to twitter laws, I can not share the gold standard of twitter users I used as my training set.
A good way to obtain your own training set is to go to twitter and look at the top 100 colleges and group label users untill you have a
BALANCED dataset of training.
 You can use Collegetool.ipyb to label.
 
 

Latent dirichlet allocation (LDA)  for topical analysis is also in the analysis scripts. Can also be viewed via the paper.










