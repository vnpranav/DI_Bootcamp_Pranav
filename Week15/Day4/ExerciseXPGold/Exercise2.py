import requests

def fetch_gifs():
   """Fetches 10 random gifs from giphy.com and returns a list of urls"""
   base = "https://api.giphy.com/v1/gifs/search"
   query = input("enter category: ")
   rating = "g"
   api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
   limit = 10
   url = f"{base}?q={query}&api_key={api_key}&rating={rating}&limit={limit}"

   response = requests.get(url)

   if response.status_code ==200:
      data = response.json()

      filtered_gifs = [gif for gif in data['data'] if gif['images']['original']['height'] > 100]

      return len(filtered_gifs), filtered_gifs
   
   else:
      print("Fail")
   
   return None, None

count, gifs = fetch_gifs()

if gifs:
   for gif in gifs:
      print(gif['images']['original']['url'])
else:
   print("No gifs found")


