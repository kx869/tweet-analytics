# Tweet Analytics Project

from tweet_analytics import compute_tweets

# prompt for name of keyword file and tweet file
f_tweet = input("Please enter the name of the file containing tweets.")
f_keyword = input("Please enter the name of the file containing keywords.")

final_results = compute_tweets(f_tweet, f_keyword)
# empty list is returned by compute_tweets in the case of IOError
if final_results == []:
    print("\nSorry, at least one of the file names entered is invalid.")

else:
    print("\nEastern Results:")
    print("Average happiness value:", final_results[0][0])
    print("Number of keyword tweets:", final_results[0][1])
    print("Total number of tweets:", final_results[0][2])
    print()

    print("Central Results:")
    print("Average happiness value:", final_results[1][0])
    print("Number of keyword tweets:", final_results[1][1])
    print("Total number of tweets:", final_results[1][2])
    print()

    print("Mountain Results:")
    print("Average happiness value:", final_results[2][0])
    print("Number of keyword tweets:", final_results[2][1])
    print("Total number of tweets:", final_results[2][2])
    print()

    print("Pacific Results:")
    print("Average happiness value:", final_results[3][0])
    print("Number of keyword tweets:", final_results[3][1])
    print("Total number of tweets:", final_results[3][2])
