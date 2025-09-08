import requests
async def getTweet(id):
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAK4U4AEAAAAA4Z9yKLbRY9mIlDP%2Bh8oH078ydKQ%3DDV8CYtXBHV3T08OkZzxbU0ibUA1Z7Lk5tk0qcHGJ4HlhfvPiD6"
    tweet_id = id
    # Endpoint de ejemplo: búsqueda de tweets recientes con una palabra clave
    url = "https://api.twitter.com/2/tweets"
    params = {
        "ids": tweet_id,
        "tweet.fields": "text,created_at",
        "expansions": "author_id",
        "user.fields": "username,name"
    }

# Encabezados de autorización
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
# Hacer la petición
    text = 'default'
    response = await requests.get(url, headers=headers, params=params)
    
# Verificar el resultado
    if response.status_code == 200:
        data = response.json()
    
        tweet = data["data"][0]
        author_id = tweet["author_id"]
    
        # Buscar autor en los datos expandidos
        users = {user["id"]: user for user in data["includes"]["users"]}
        author = users.get(author_id, {})
    
        print(f"Tweet ID: {tweet['id']}")
        print(f"Texto: {tweet['text']}")
        text = tweet['text']
        print(f"Fecha: {tweet['created_at']}")
        print(f"Autor: {author.get('name')} (@{author.get('username')})")
    else:
        print(f"Error {response.status_code}: {response.text}")
    return text




