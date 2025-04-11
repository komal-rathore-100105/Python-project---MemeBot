import json
import random

def get_random_quote():
    with open("funny_quotes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)
    
    quote_obj = random.choice(quotes)
    quote_text = quote_obj["quote"]
    author = quote_obj["author"]

    return f"{quote_text} - {author}"

# Test run
if __name__ == "__main__":
    print("🎲 Random Quote:")
    print(get_random_quote())

    
