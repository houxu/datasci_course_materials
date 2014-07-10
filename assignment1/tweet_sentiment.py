import sys
import json


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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

    sent_file.close()
    tweet_file.close()
    
    # process the tweets, and get the score for each tweet
    res = []
    for text in tweet_list:
    	score = 0.0
    	if (text != None):
    		words = text.split()

    		for word in words:
    			score += scores.get(word, 0)

    	print score


if __name__ == '__main__':
   main()
