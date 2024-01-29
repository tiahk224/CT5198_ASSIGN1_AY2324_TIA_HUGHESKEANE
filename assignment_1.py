#Tia Hughes Keane Assignment 1 23202109 29/01/2024

def main():
    # Creating an empty list to store the number of daily customers
    customer_num = []

    # Iterate over 7 days using a for loop (inclusive of 1 but exclusive of 8)
    for day in range(1, 8):
        # Allowing for interger only, as a customer can only be a whole value
        customers = int(input(f"Enter the number of customers for day {day}: "))
        # Appending number of customers for current day to the list
        customer_num.append(customers)

    # Calculating maximum, minimum, and average number of customers
    customers_max = max(customer_num)
    customers_min = min(customer_num)
    customers_avg = round(sum(customer_num) / len(customer_num))

    # Displaying the results
    print("\nMaximum number of customers:", customers_max)
    print("Minimum number of customers:", customers_min)
    print("Average number of customers:", customers_avg)

if __name__ == "__main__":
    main()
