## write code here!
import config
from mlh_twitter_api import get_user_tweets as fetch
from twitter_scraper_fetcher import *
import re
import random
import markovify

# remove emoji, punctuation, urls from tweets
def create_string(tweets):
    text = ""

    for tweet in tweets:
        text += (
            tweet + "\n\n"
        )  # Make sure each tweet is handled properly by markovify
    return text

def generate_bot_answer_with_text_model(twitter_handle,user_question,text_model):
  bot_answer = None
  word_list = user_question.split(' ')
  random_word = random.choice(word_list)
  bot_answer = text_model.make_sentence_with_start(random_word,strict=False)
  if bot_answer == None:
    bot_answer = text_model.make_sentence(test_output=False)
  # print("hello")
  return bot_answer
  
    ## write code here
        
# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
  tweets = fetch(twitter_handle)
  clean_tweets = clean_tweets_data(tweets)
  text = "".join(map(str,clean_tweets))
  text_model = markovify.Text(text)
  return generate_bot_answer_with_text_model(twitter_handle,user_question,text_model)