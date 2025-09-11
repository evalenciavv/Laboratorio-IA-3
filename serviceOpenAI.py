from openai import OpenAI

def postOpenAI(inputTweet):
    # Hacer la solicitud
    response = client.responses.create(
        model="gpt-4o",
        instructions="Eres un asistente emocional que habla con sensatez",
        input="realiza un analisis de sentimientos de este tweet de una manera respetuosa: "+inputTweet,
    )
    print(response.output_text)
    return response.output_text

client = OpenAI(
    api_key = "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"
)
