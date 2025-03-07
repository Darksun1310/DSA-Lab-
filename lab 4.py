# E-Commerce Platform with Product Sorting

def merge_sort(products, key, reverse=False):
    if len(products) <= 1:
        return products

    def merge(left, right, key):
        sorted_list = []
        while left and right:
            if getattr(left[0], key) < getattr(right[0], key):
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        sorted_list.extend(left or right)
        return sorted_list

    middle = len(products) // 2
    left_half = merge_sort(products[:middle], key)
    right_half = merge_sort(products[middle:], key)

    result = merge(left_half, right_half, key)
    return result[::-1] if reverse else result

class Product:
    def __init__(self, name, price, popularity):
        self.name = name
        self.price = price
        self.popularity = popularity

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, popularity={self.popularity})"

# Function to display sorted products
def display_products(products, title):
    print(f"\n{title}")
    for product in products:
        print(product)

# Function to add a product
def add_products(products, name, price, popularity):
    products.append(Product(name, price, popularity))
    return products

# Function to search for a product
def search_product(products, key, value):
    return [product for product in products if getattr(product, key) == value]

# Product list
products = [
    Product('Laptop', 800, 90),
    Product('Smartphone', 600, 95),
    Product('Tablet', 400, 85),
    Product('Headphones', 200, 80),
    Product('Smartwatch', 300, 88)
]

# Sort by different criteria
sorted_by_price = merge_sort(products, 'price')
sorted_by_popularity = merge_sort(products, 'popularity', reverse=True)
sorted_by_name = merge_sort(products, 'name')

# Display sorted products
display_products(sorted_by_price, "Products Sorted by Price (Ascending)")
display_products(sorted_by_popularity, "Products Sorted by Popularity (Descending)")
display_products(sorted_by_name, "Products Sorted by Name (Alphabetical)")
