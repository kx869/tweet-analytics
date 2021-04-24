# Tweet Analytics Project

# function to be used in the compute_tweets function
def calculate_score(tweet_word_list, keyword_value_list):
    keyword_count = 0
    tweet_total_score = 0
    for tweet_word in tweet_word_list:
        for keyword_pairing in keyword_value_list:
            if tweet_word == keyword_pairing[0]:
                keyword_count += 1
                tweet_total_score += keyword_pairing[1]
    if keyword_count > 0:
        tweet_score = tweet_total_score / keyword_count
        return tweet_score
    else:
        return "no results"
        # allows for if != "no results" in compute_tweets() lines 97, 109, 119, 129

def compute_tweets(tweet_file, keyword_file):
    keyword_list = []
    stripped_kh_pair = []
    stripped_tweet_info = []
    # coordinates (p4, p6, p8, and p10 were not used)
    p1 = (49.189787, -67.444574)
    p2 = (24.660845, -67.444574)
    p3 = (49.189787, -87.518395)
    p5 = (49.189787, -101.998892)
    p7 = (49.189787, -115.236428)
    p9 = (49.189787, -125.242264)

    pacific_tweet_count, mountain_tweet_count, central_tweet_count, eastern_tweet_count = 0, 0, 0, 0

    pacific_total_score, mountain_total_score, central_total_score, eastern_total_score = 0, 0, 0, 0

    eastern_average, central_average, mountain_average, pacific_average = 0, 0, 0, 0

    pacific_keyword_tweet_count, mountain_keyword_tweet_count = 0, 0
    central_keyword_tweet_count, eastern_keyword_tweet_count = 0, 0
    total_tweet_count = 0

    try:
        # keywords file (code from assignment document)
        keywordfile = open(keyword_file,"r",encoding="utf-8")

        for line in keywordfile:

            keyword_happiness_pair = line.split(",")

            # strip /n from number
            for word in keyword_happiness_pair:
                stripped_kh_pair.append(word.strip())
            # convert happiness value to integer
            stripped_kh_pair[1] = int(stripped_kh_pair[1])

            keyword_list.append(stripped_kh_pair)

            # resets so that the previous pair is not appended again
            stripped_kh_pair = []
        # closes keywords file
        keywordfile.close()
    # generates an exception if either file does not exists, function returns an empty list
    except IOError:
        return []

    try:
        # tweets file (code from assignment document)
        tweetfile = open(tweet_file,"r",encoding="utf-8")

        for line in tweetfile:
            total_tweet_count += 1
            tweet_info = line.split()

            # remove value, date, time
            tweet_info.pop(4)
            tweet_info.pop(3)
            tweet_info.pop(2)

            # stripped separately from words because the negative sign "-" must be kept
            longitude = float(tweet_info.pop(1).strip(" [],"))
            latitude = float(tweet_info.pop(0).strip(" [],")) # may need to strip more?

            # tweet_info now contains  each word of the tweet with punctuation (2+)
            for element in tweet_info:
                stripped_element = element.strip(" !@#$%^&*()-_+=;:\"\'/.>,<{[}]|\\~`")
                stripped_tweet_info.append(stripped_element)
            # stripped_tweet_info contains each word of the tweet without leading/trailing spaces/punctuation
            # remove empty elements from list (previously consisted of only punctuation)
            while "" in stripped_tweet_info:
                stripped_tweet_info.remove("")
            # word_list is a list of each word in lowercase with no punctuation
            word_list = [word.lower() for word in stripped_tweet_info]

            # latitude must be between 24.660845 and 49.189787
            if (latitude >= float(p2[0])) and (latitude <= float(p1[0])):
                if (longitude >= p9[1]) and (longitude < p7[1]):
                    pacific_tweet_count += 1
                    pacific_results = calculate_score(word_list, keyword_list)
                    # only executes if at least a keyword match is found in the tweet
                    # avoids ZeroDivisionError
                    if pacific_results != "no results":
                        pacific_total_score += pacific_results
                        pacific_keyword_tweet_count += 1
                        pacific_average = pacific_total_score / pacific_keyword_tweet_count

                if (longitude >= p7[1]) and (longitude < p5[1]):
                    mountain_tweet_count += 1
                    mountain_results = calculate_score(word_list, keyword_list)
                    if mountain_results != "no results":
                        mountain_total_score += mountain_results
                        mountain_keyword_tweet_count += 1
                        mountain_average = mountain_total_score / mountain_keyword_tweet_count

                if (longitude >= p5[1]) and (longitude < p3[1]):
                    central_tweet_count += 1
                    central_results = calculate_score(word_list, keyword_list)
                    if central_results != "no results":
                        central_total_score += central_results
                        central_keyword_tweet_count += 1
                        central_average = central_total_score / central_keyword_tweet_count

                if (longitude >= p3[1]) and (longitude <= p1[1]):
                    eastern_tweet_count += 1
                    eastern_results = calculate_score(word_list, keyword_list)
                    if eastern_results != "no results":
                        eastern_total_score += eastern_results
                        eastern_keyword_tweet_count += 1
                        eastern_average = eastern_total_score / eastern_keyword_tweet_count

            # resets so that the previous tweet info is not appended again
            stripped_tweet_info = []
        # closes tweets file
        tweetfile.close()

    # generates an exception if either file does not exists, function returns an empty list
    except IOError:
        return []
    #return list of tuples (one for each time zone)  (average, count_of_keyword_tweets, count_of_tweets)
    eastern_tuple = (round(eastern_average, 2), eastern_keyword_tweet_count, eastern_tweet_count)
    central_tuple = (round(central_average, 2), central_keyword_tweet_count, central_tweet_count)
    mountain_tuple = (round(mountain_average, 2), mountain_keyword_tweet_count, mountain_tweet_count)
    pacific_tuple = (round(pacific_average, 2), pacific_keyword_tweet_count, pacific_tweet_count)

    return [eastern_tuple, central_tuple, mountain_tuple, pacific_tuple]
