from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator


def get_content(product):
    USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    LANGUAGE = 'en-US,en;q=0.5'

    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    # Get the webpage content
    html_content = session.get(f'https://www.jumia.co.ke/catalog/?q={product}')
    return html_content


def home(request):
    product_info_list = []
    page_obj = None

    if 'product' in request.GET:
        product = request.GET.get('product')
        html_content = get_content(product)

        if html_content.status_code == 200:
            soup = BeautifulSoup(html_content.text, 'html.parser')
            product_list = soup.find_all('article', class_='prd _fb col c-prd')

            min_price = request.GET.get('min_price')
            max_price = request.GET.get('max_price')

            for product in product_list:
                name_tag = product.find('h3', class_='name')
                price_tag = product.find('div', class_='prc')

                # Filter products by price
                if price_tag:
                    price_text = price_tag.text.replace('KSh', '').replace(',', '').strip()  # Clean price text
                    try:
                        price = float(price_text)  # Convert to float for comparison
                    except ValueError:
                        price = None  # Handle invalid price gracefully

                    if min_price and price is not None and price < float(min_price):
                        continue
                    if max_price and price is not None and price > float(max_price):
                        continue
                else:
                    price = None  # Set price to None if no price tag is found

                img_tag = product.find('img', class_='img')
                stars_tag = product.find('div', class_='stars _s')
                rating_tag = product.find('div', class_='in')

                # Extract only the numeric part of the rating, if it exists
                rating = stars_tag.text if stars_tag else 'No rating'
                rating_value = rating.split(' ')[0] if rating != 'No rating' else '0'  # Extract '4.1' from '4.1 out of 5'

                product_info = {
                    'name': name_tag.text if name_tag else 'N/A',
                    'price': price_text if price_tag else 'N/A',  # Use cleaned price text
                    'image': img_tag.get('data-src') if img_tag else None,
                    'rating': rating_value,  # Store the numeric part for sorting
                    'rating_percentage': rating_tag.text if rating_tag else 'No percentage',
                }
                product_info_list.append(product_info)

            # Sort products
            sort_by = request.GET.get('sort')
            if sort_by == 'price_asc':
                product_info_list.sort(key=lambda x: float(x['price'].replace('KSh', '').replace(',', '').strip()) if x['price'] != 'N/A' else float('inf'))
            elif sort_by == 'price_desc':
                product_info_list.sort(key=lambda x: float(x['price'].replace('KSh', '').replace(',', '').strip()) if x['price'] != 'N/A' else -float('inf'), reverse=True)
            elif sort_by == 'rating_desc':
                product_info_list.sort(key=lambda x: float(x['rating']) if x['rating'] != 'N/A' else -float('inf'), reverse=True)

            # Setup pagination only if there are products
            paginator = Paginator(product_info_list, 12)  # 12 items per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)  # Get paginated products


    context = {
        'product_info_list': product_info_list,
        'page_obj': page_obj,
    }
    return render(request, 'core/home.html', context)
