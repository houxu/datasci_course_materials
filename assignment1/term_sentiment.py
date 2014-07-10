import sys
import json

def compute_term_sentiment(scores, tweet_list):
	"""	
	Return a dict, the key is a key, and the value is the score
	The key are splited from tweet_list, and score is average of the 
	words in the tweet which can be found in the scores	
	"""

	new_scores_dict = {}

	for tweet in tweet_list:
		if tweet == None:
			continue

		score_tweet = 0.0
		# get the words in the tweet
		words = tweet.strip().split()

		unscored = [] # store the word having no score\
		for word in words:
			if word in scores: # computer the total scores of the tweet
				score_tweet += scores[word]
			else:
				unscored.append(word)

		# append all the score for new word

		if len(unscored) == len(words):
			continue

		for word in unscored:
			if word == None:
				continue

			if (word in new_scores_dict):
				new_scores_dict[word].append(score_tweet)

			else:
				new_scores_dict[word] = [score_tweet]

	# the finally score of new word are the average of all score_tweet
	for (word, value_list) in new_scores_dict.items():
		new_scores_dict[word] = sum(value_list) / len(value_list)

	return new_scores_dict

def build_score_dict(sent_file):
	scores = {}
	for line in sent_file:
		term, score = line.split('\t')
		scores[term] = int(score)

	return scores


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # get scores
    scores = build_score_dict(sent_file)

    # get tweet
    tweet_list = [json.loads(tweet).get('text') for tweet in tweet_file]

    # close the file
    sent_file.close()
    tweet_file.close()

    # compute the new term score
    new_scores_dict = compute_term_sentiment(scores, tweet_list)
    
    # print out the result
    for (term, score) in new_scores_dict.items():
    	print term, score



if __name__ == '__main__':
   main()
