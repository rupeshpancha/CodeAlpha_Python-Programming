# Simple stock tracker program

def main():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 320,
        "GOOGL": 140
    }

    print("Simple Stock Tracker")
    print("--------------------")

    total_value = 0

    while True:
        stock_name = input("Enter stock symbol (or 'done' to finish): ").upper()

        # Stop taking input
        if stock_name == "DONE":
            break

        # Check if stock exists in dictionary
        if stock_name not in stock_prices:
            print("Stock not found. Please try again.")
            continue

        # Get quantity from user
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Calculate cost
        stock_cost = stock_prices[stock_name] * quantity
        total_value += stock_cost

        print("Added:", stock_name, "x", quantity, "=", stock_cost)
        print()

    # Display final total
    print("Your total investment value is:", total_value)

    # Optional: save to file
    save_answer = input("Save result to a file? (yes/no): ").lower()

    if save_answer == "yes":
        file_name = "stock_results.txt"
        with open(file_name, "w") as file:
            file.write("Total Investment Value: " + str(total_value))
        print("Saved to", file_name)


# Run the program
main()
