# This code is a simple example of how to use TensorFlow to filter and analyze product data.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress all TensorFlow logging (including INFO and WARNING)
import tensorflow as tf

# Define a simple Product class to hold product information
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

products = [
    Product("Cellphone", 532.99, "Electronics"),
    Product("T-Shirt", 15.49, "Clothing"),
    Product("Laptop", 1007.99, "Electronics"),
    Product("Jeans", 32.99, "Clothing"),
    Product("Headphones", 29.49, "Electronics"),
    Product("Jacket", 14.99, "Clothing")
]

names = tf.constant([product.name for product in products])
prices = tf.constant([product.price for product in products])
categories = tf.constant([product.category for product in products])

def filter_products_by_category(category):
    mask = tf.equal(categories, category)
    filtered_names = tf.boolean_mask(names, mask)
    filtered_prices = tf.boolean_mask(prices, mask)
    return filtered_names, filtered_prices
def calculate_average_price(category):
    filtered_names, filtered_prices = filter_products_by_category(category)
    if tf.size(filtered_prices) == 0:
        return tf.constant(0.0)
    return tf.reduce_mean(filtered_prices)
def find_most_expensive_product(category):
    filtered_names, filtered_prices = filter_products_by_category(category)
    if tf.size(filtered_prices) == 0:
        return tf.constant("")
    max_index = tf.argmax(filtered_prices)
    return tf.gather(filtered_names, max_index)
def find_cheapest_product(category):
    filtered_names, filtered_prices = filter_products_by_category(category)
    if tf.size(filtered_prices) == 0:
        return tf.constant("")
    min_index = tf.argmin(filtered_prices)
    return tf.gather(filtered_names, min_index)
def main():
    category = "Electronics"
    print(f"Products in category '{category}':")
    names, prices = filter_products_by_category(category)
    for name, price in zip(names.numpy(), prices.numpy()):
        print(f"{name.decode('utf-8')}: ${price:.2f}")

    average_price = calculate_average_price(category)
    print(f"\nAverage price in category '{category}': ${average_price:.2f}")

    most_expensive = find_most_expensive_product(category)
    print(f"Most expensive product in category '{category}': {most_expensive.numpy().decode('utf-8')}")

    cheapest = find_cheapest_product(category)
    print(f"Cheapest product in category '{category}': {cheapest.numpy().decode('utf-8')}")

if __name__ == "__main__":
    main()