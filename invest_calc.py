# My first investment analysis tool
# Goal: Calculate compound interest for my future goals in Madrid 2028

def calculate_wealth(initial_investment, monthly_deposit, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    total = initial_investment
    
    for month in range(months):
        total = (total + monthly_deposit) * (1 + monthly_rate)
    
    return round(total, 2)

# Initial data for my journey
starting_amount = 1000  # Start small, grow big
monthly_save = 200      # Freelance income investment
expected_return = 10    # 10% average annual return (S&P 500 style)
period = 2              # Years until I reach Spain (2028)

final_wealth = calculate_wealth(starting_amount, monthly_save, expected_return, period)

print(f"--- Investment Projection ---")
print(f"After {period} years, my portfolio will be: ${final_wealth}")
print(f"Path to Madrid is clear. Keep coding! 🚀")