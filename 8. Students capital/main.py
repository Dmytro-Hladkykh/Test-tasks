def max_capital(n, c, gains, prices):
    # Creating a list of tuples (gain, price) and sort by gain/price ratio in descending order
    laptops = sorted(zip(gains, prices), key=lambda x: x[0]/x[1], reverse=True)
    
    for i in range(min(n, len(laptops))):
        gain, price = laptops[i]
        if c >= price:
            c += gain - price  # Buy and sell the laptop
    
    return c

def main():
    n = int(input("Enter the number of laptops you can buy (N): "))
    c = int(input("Enter your initial capital (C): "))
    gains = list(map(int, input("Enter the gains for each laptop (separated by spaces): ").split()))
    prices = list(map(int, input("Enter the prices for each laptop (separated by spaces): ").split()))

    result = max_capital(n, c, gains, prices)
    print(f"Your capital at the end of the summer: {result}")

if __name__ == "__main__":
    main()