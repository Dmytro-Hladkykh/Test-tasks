import logging

# Configure logging
logging.basicConfig(filename='transactions.log', level=logging.INFO,
                    format='%(asctime)s - BUYER: %(buyer)d - SELLER: %(seller)d - AMOUNT: %(amount)d UAH @ %(price).2f USD')

def log_transaction(buyer_id, seller_id, amount, price):
    logging.info('', extra={'buyer': buyer_id, 'seller': seller_id, 'amount': amount, 'price': price})
