import tweepy

# Credenciales - usa Bearer Token para v2 (mejor)
#bearer_token = "AAAAAAAAAAAAAAAAAAAAAPBd4AEAAAAAcrvvoACyYBhKy9PS2Fhhus7%2Flx4%3D3yK2MHyq5Eo9C3S6RUymSOjOokNaBI6q1EU1TReW8WD4bYDZ6s"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAK4U4AEAAAAAFtuqjUPJg4g5tN%2BHPXBjdE%2Fp6TM%3DenpVR9OusZq7h1INXlZtlZoMWEPNOw2Cn99Bd4JzuaSKKzH52o"
client = tweepy.Client(bearer_token=bearer_token)

def getTweet(idTweet):
    try:
        response = client.get_tweet(idTweet, tweet_fields=["text"])
        if response.data:
            return response.data.text
        else:
            return None
    except tweepy.TweepyException as e:
        print(f"Error al obtener el tweet: {e}")
        return None