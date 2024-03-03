import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke = data["data"]
        content = joke["content"]
        return content
    else:
        raise Exception("Failed to fetch random jokes")
    

def main():
    try:
        content = fetch_random_jokes()
        print(f"content: {content}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()