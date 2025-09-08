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
    api_key = "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"
)

