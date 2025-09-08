import openai
import tweet

idTweet = "1964743583866761280"
async def main(idTweet):
    payloadTweet = await tweet.getTweet(idTweet)
    result = openai.postOpenAI(payloadTweet)
    print(result)

main(idTweet)
