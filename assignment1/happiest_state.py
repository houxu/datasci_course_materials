import sys
import json
import re

STATES = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def build_score_dict(sent_file):
	scores = {}
	for line in sent_file:
		term, score = line.split('\t')
		scores[term] = int(score)

	return scores

def get_tweet_with_state(tweet_file):
    state_tweet = []
    for tweet in tweet_file:
        tweet = json.loads(tweet)
        if tweet.get('text') == None:
            continue

        # get state info
        state = None
        if tweet.get('place') != None:
            if (tweet['place'].get('country_code') != 'US' and 
                tweet['place'].get('country') != 'United States'):
                continue

            place_name = tweet['place'].get('full_name')
            if place_name != None:
                try:
                    state = place_name.split()[1]
                except BaseException as e:
                    print place_name, "error is -> ", e
                    return

        else:
            state = tweet.get('user').get('location')

        if (len(state) != None):
            state_tweet.append((state, tweet.get('text')))

    return state_tweet

def get_score_from_state_tweet(state_tweet, scores):
    """
    Return a dict, key is the state, and the value is the tweet score
    """
    state_tweet_score = {}


    for (state, text) in state_tweet:

        score = 0.0

        if (text != None):
            words = text.split()

            for word in words:
                score += scores.get(word, 0)

        if state in state_tweet_score:
            state_tweet_score[state] += score
        else:
            state_tweet_score[state] = score

    return state_tweet_score


def get_happiest_state(state_tweet_score):
    happiest_state_score = (None, 0)

    for (state, score) in state_tweet_score.items():

        if (score > happiest_state_score[1]):
            happiest_state_score = (state, score)

    happiest_state =  happiest_state_score[0].split(',')[0].strip()
    for (short_state, full_state) in STATES.items():

        if happiest_state in full_state.split():
            return short_state  

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    
    # get scores
    scores = build_score_dict(sent_file)

    # get tweet info
    state_tweet = get_tweet_with_state(tweet_file)

    sent_file.close()
    tweet_file.close()

    state_tweet_score = get_score_from_state_tweet(state_tweet, scores)

    happiest_state = get_happiest_state(state_tweet_score)

    print  happiest_state

if __name__ == '__main__':
    main()



    