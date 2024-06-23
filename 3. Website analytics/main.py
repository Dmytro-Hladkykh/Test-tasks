import csv
from collections import defaultdict

def find_target_users(file1, file2):
    # Hash table to store visited products by each user and day
    visited_products = defaultdict(lambda: defaultdict(set))

    # Read and process 1st CSV
    with open(file1, 'r', newline='') as f1:
        reader1 = csv.reader(f1)
        for row in reader1:
            user_id, product_id, _ = row
            visited_products[user_id]['day1'].add(product_id)  

    # Read and process 2nd CSV
    with open(file2, 'r', newline='') as f2:
        reader2 = csv.reader(f2)
        for row in reader2:
            user_id, product_id, _ = row
            visited_products[user_id]['day2'].add(product_id)  

    # Find users who visited on both days and check for different products
    target_users = set()
    for user_id, visits in visited_products.items():
        if 'day1' in visits and 'day2' in visits:
            if visits['day1'] != visits['day2']:
                target_users.add(user_id)

    print("Target Users:", target_users)

if __name__ == "__main__":
    file1 = '3. Website analytics/day1.csv'
    file2 = '3. Website analytics/day2.csv'
    find_target_users(file1, file2)
