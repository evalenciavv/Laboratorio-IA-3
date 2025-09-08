from openai import OpenAI

async def postOpenAI(inputTweet):
    # Hacer la solicitud
    response = await client.responses.create(
        model="gpt-4o",
        instructions="Eres un asistente emocional que habla con sensatez",
        input="realiza un analisis de sentimientos de este tweet de una manera respetuosa: "+inputTweet,
    )
    print(response.output_text)
    return response.output_text

client = OpenAI(
    ##api_key = "fe"
    )

