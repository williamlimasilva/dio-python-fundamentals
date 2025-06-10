from sklearn.cluster import KMeans
import numpy as np

class Product:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

products = [
    Product("Product A", 10.99, 1.2),
    Product("Product B", 15.49, 0.8),
    Product("Product C", 7.99, 1.5),
    Product("Product D", 12.99, 1.0),
    Product("Product E", 9.49, 1.3),
    Product("Product F", 14.99, 0.9)
]

# Prepare data for clustering
prices = [[product.price, product.weight] for product in products]
matrix = np.array(prices)
# print(f"Data matrix for clustering:\n{matrix}")

# Apply KMeans clustering
kmeans = KMeans(n_init='auto', n_clusters=3, random_state=0)
kmeans.fit(matrix)
labels = kmeans.labels_
# print(f"Cluster labels: {labels}")
# Print the cluster centers
centers = kmeans.cluster_centers_
print(f"Cluster centers:\n{centers}")

# Print the cluster labels for each product
for i in range(kmeans.n_clusters):
    print(f"Cluster {i} center: {centers[i]}")
    for j, product in enumerate(products):
        if labels[j] == i:
            print(f"  {product.name} (Price: {product.price}, Weight: {product.weight})")