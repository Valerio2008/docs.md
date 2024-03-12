import json
import pprint

# Load compact data from JSON file
with open('compact_data.json') as f:
    data = json.load(f)

# Define Product, Category, and Attribute classes
class Attribute:
    def init(self, name, value):
        self.name = name
        self.value = value

class Product:
    def init(self, category, name, description=None, attributes=None):
        self.category = category
        self.name = name
        self.description = description
        self.attributes = attributes or []

class Category:
    def init(self, name, products=None):
        self.name = name
        self.products = products or []

# Create categories, products, and attributes from compact data
categories = []
for category_data in data['categories']:
    name = category_data['name']
    products = []
    for product_data in category_data['products']:
        category = Category(name)
        name = product_data['name']
        description = product_data.get('description')
        attributes = [Attribute(attr['name'], attr['value']) for attr in product_data['attributes']]
        product = Product(category, name, description, attributes)
        category.products.append(product)
        products.append(product)
    categories.append(Category(name, products))

# Print products with categories, names, descriptions, and attributes
for category in categories:
    print(f"Category: {category.name}")
    for product in category.products:
        print(f"Product: {product.name}")
        if product.description:
            print(f"Description: {product.description}")
        for attribute in product.attributes:
            print(f"Attribute: {attribute.name} - {attribute.value}")
        print()

def generate_slug(name):
    return ''.join(e for e in name if e.isalnum()).lower()

data = None

with open('data/compact_data.json', 'docs.md', 'data.py', 'r') as f:
    data = json.loads(''.json(f.readlines()))
    pprint(data)
