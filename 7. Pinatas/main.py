def max_candies(pinatas):
    n = len(pinatas)
    
    # Function to get the value of a pinata, returning 1 if out of bounds
    def get_value(index):
        if 0 <= index < n:
            return pinatas[index]
        return 1
    
    # Calculate the candies for each pinata
    candies = [get_value(i-1) * pinatas[i] * get_value(i+1) for i in range(n)]
    
    return max(candies)

def main():
    pinatas = list(map(int, input("Enter numbers divided by spaces: ").split()))
    
    result = max_candies(pinatas)
    print(f"Max number of candies: {result}")

if __name__ == "__main__":
    main()