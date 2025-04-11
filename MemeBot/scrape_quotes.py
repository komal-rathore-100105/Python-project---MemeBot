# import requests
# from bs4 import BeautifulSoup
# import json
# 
# def scrape_funny_quotes():
    # url = "http://quotes.toscrape.com/tag/humor"
    # response = requests.get(url)
# 
    # if response.status_code != 200:
        # print("Failed to retrieve webpage")
        # return
# 
    # soup = BeautifulSoup(response.text, 'html.parser')
    # quotes_div = soup.find_all("div", class_="quote")
# 
    # quotes = []
# 
    # for quote_div in quotes_div:
        # text = quote_div.find("span", class_="text").get_text()
        # author = quote_div.find("small", class_="author").get_text()
        # quotes.append({"quote": text, "author": author})
# 
    # Save to JSON
    # with open("funny_quotes.json", "w", encoding="utf-8") as f:
        # json.dump(quotes, f, indent=4, ensure_ascii=False)
# 
    # print(f"✅ {len(quotes)} funny quotes saved to funny_quotes.json")
# 
# if __name__ == "__main__":
    # scrape_funny_quotes()
# 
# import requests
# from bs4 import BeautifulSoup
# import json
# 
# def get_quotes():
    # url = "http://quotes.toscrape.com/tag/humor/"
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, "html.parser")
# 
    # quotes = []
# 
    # for quote_div in soup.find_all("div", class_="quote"):
        # quote = quote_div.find("span", class_="text").text.strip()
        # quotes.append(quote)
# 
    # return quotes
# 
# funny_quotes = get_quotes()
# for i, q in enumerate(funny_quotes[:], start=1):
    # print(f"{i}. {q}")
# 
# def save_quotes_to_json(quotes, filename="funny_quotes.json"):
    # with open(filename, "w") as f:
        # json.dump(quotes, f, indent=4)
    # print(f"✅ Saved {len(quotes)} quotes to {filename}")
# 
# Run only when this file is executed directly
# if __name__ == "__main__":
    # funny_quotes = get_quotes()
    # save_quotes_to_json(funny_quotes)
# 
import requests
from bs4 import BeautifulSoup
import json

def scrape_funny_quotes():
    base_url = "http://quotes.toscrape.com/tag/humor/page/"
    page = 1
    quotes = []
    
    while True:
        url = f"{base_url}{page}/"
        print(f"Scraping page {page}...")
        response = requests.get(url)

        if response.status_code != 200:
            print("✅ Done scraping all pages.")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_div = soup.find_all("div", class_="quote")

        if not quotes_div:
            break  # No more quotes on this page

        for quote_div in quotes_div:
            text = quote_div.find("span", class_="text").get_text()
            author = quote_div.find("small", class_="author").get_text()
            quotes.append({"quote": text, "author": author})

        page += 1

    # Save to JSON
    with open("funny_quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)

    print(f"✅ Total {len(quotes)} funny quotes saved to funny_quotes.json")

if __name__ == "__main__":
    scrape_funny_quotes()


