

# Jumia Product Scraper

This Django project allows users to search for products on the Jumia website, filter by price, sort results, and view product details through a user-friendly interface. The application uses web scraping techniques to fetch real-time product data and presents it effectively.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- **Dynamic Product Search**: Search for various items available on Jumia.
- **Price Filtering**: Set minimum and maximum price ranges to refine search results.
- **Sorting Options**: Sort products by price (ascending/descending) and rating (descending).
- **Pagination**: Navigate through product results with pagination (12 items per page).
- **Search History**: Track recent searches within the session for user convenience.
- **Web Scraping**: Utilize BeautifulSoup for scraping product details from the Jumia website.

## Technologies Used

- **Django**: A high-level Python web framework.
- **BeautifulSoup**: A library for parsing HTML and XML documents.
- **Requests**: A simple HTTP library for making requests.
- **HTML/CSS**: For front-end design.
- **Python**: Programming language used for backend development.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/jumia-product-scraper.git
   cd jumia-product-scraper
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations** (if any):

   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the application**: Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Use the search bar to input the product you wish to find on Jumia.
- Set minimum and maximum price filters to narrow down your search results.
- Sort the results based on your preferences (price or rating).
- View product details including name, price, image, and rating.
- Navigate through the results using pagination.
- Check the search history at the bottom to revisit previous searches.

## Project Structure

```
jumia-product-scraper/
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── jumia_product_scraper/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

