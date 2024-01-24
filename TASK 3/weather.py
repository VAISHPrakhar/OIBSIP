import requests
from bs4 import BeautifulSoup

def weather(city):
    city = city.replace(" ", "+")
    url = f"https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9'  # Setting language preference to English
    }

    res = requests.get(url, headers=headers)
    print("Searching...\n")
    
    soup = BeautifulSoup(res.text, 'html.parser')

    # Try to find weather information based on the updated class names or structure
    weather_info = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text

    print(weather_info)

city = input("Enter the Name of City -> ")
city = city + " weather"
weather(city)
print("Have a Nice Day:)")
