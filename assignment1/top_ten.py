import sys
import json
from operator import itemgetter


def get_hashtags_account(tweet_file):

    all_hashtags = []
    for tweet in tweet_file:
        tweet = json.loads(tweet)

        if 'entities' not in tweet:
            continue

        hashtags = tweet['entities'].get('hashtags')

        if hashtags == None or hashtags == []:
            continue

        for hashtag in hashtags:
            all_hashtags.append(hashtag['text'])

    # get the counts of hashtag
    hashtag_counts = {}

    for hashtag in all_hashtags:
        if hashtag in hashtag_counts:
            hashtag_counts[hashtag] += 1
        else:
            hashtag_counts[hashtag] = 1

    return hashtag_counts


def main():

    tweet_file = open(sys.argv[1])

    hashtag_counts = get_hashtags_account(tweet_file)
    tweet_file.close()

    top10_counts = sorted(hashtag_counts.items(), key = itemgetter(1), reverse = True)[:10]
    
    # print out
    for hashtag, count in top10_counts:
        print hashtag, count


if __name__ == '__main__':
    main()



    