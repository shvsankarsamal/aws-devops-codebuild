import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        joke = response.json()
        setup = joke['setup']
        punchline = joke['punchline']
        print(f"The Joke of a day: {setup}")
        print(f"Punchline for joke: {punchline}")
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    get_random_joke()
