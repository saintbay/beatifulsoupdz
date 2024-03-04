import requests
from bs4 import BeautifulSoup

def get_books(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        books = []

        for book in soup.find_all('h3'):
            title = book.a['title']
            books.append(title)

        return books

    else:
        print(f"Error: Unable to fetch data from {url}")
        return None

def display_books(books):
    print("Какую книгу желаете приобрести?")
    for i, book in enumerate(books, 1):
        print(f"{i}) {book}")

def get_book_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1').text.strip()
        description = soup.find('meta', {'name': 'description'})['content']
        price = soup.find('p', class_='price_color').text.strip()
        image_url = soup.find('img')['src']

        return title, description, price, image_url

    else:
        print(f"Error: Unable to fetch data from {url}")
        return None

if __name__ == "__main__":
    base_url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"


    books_list = get_books(base_url)

    if books_list:

        display_books(books_list)

        user_choice = int(input("Введите номер книги, которую желаете приобрести: "))

        if 1 <= user_choice <= len(books_list):
            selected_book_url = f"{base_url}/{user_choice}-index.html"

            title, description, price, image_url = get_book_details(selected_book_url)

            print(f"\nХорошо! Вот данные об этой книге:")
            print(f"Название: {title}")
            print(f"Описание: {description}")
            print(f"Цена: {price}")
            print(f"Картинка: {image_url}")

        else:
            print("Ошибка: Неверный выбор.")
