import sys
import json

def compute_frequence(tweet_list):
	"""
	Return a dict, the key is the term, the value is the frequence
	"""

	words_dict = {} # the value is the number appearing

	for tweet in tweet_list:
		if tweet is None:
			continue
		else:
			words = tweet.strip().split()
			for word in words:
				if word is None:
					continue
				else:
					if (word in words_dict):
						words_dict[word] += 1
					else:
						words_dict[word] = 1

	# total term appear
	num_total_words = float(len(words_dict))

	freq_term = {}
	for (term, value) in words_dict.items():
		freq_term[term] = value / num_total_words

	return freq_term

def main():
    tweet_file = open(sys.argv[1])
    tweet_list = [json.loads(tweet).get('text') for tweet in tweet_file]
    tweet_file.close()

    freq_term = compute_frequence(tweet_list)

    #print out the result
    for (term, value) in freq_term.items():
    	print term, value

if __name__ == '__main__':
   main()
