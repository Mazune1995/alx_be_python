# finance_calculator.py

def main():
    # Prompt the user for financial inputs
    try:
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your total monthly expenses: "))
    except ValueError:
        print("Please enter valid numeric values for income and expenses.")
        return

    # Correct monthly savings calculation
    monthly_savings = monthly_income - monthly_expenses

    # Project annual savings with 5% interest
    annual_savings = monthly_savings * 12
    interest_rate = 0.05
    projected_annual_savings = annual_savings + (annual_savings * interest_rate)

    # Display results
    print(f"\nYour monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")

if __name__ == "__main__":
    main()
#
