monthly_income = float(input('Enter your monthly income: '))
total_monthly_expens = float(input('Enter your total monthly expenses: '))

monthly_savings = monthly_income - total_monthly_expens

annual_interest_rate = 0.05

projection_saving = int(monthly_savings * 12 + ( monthly_savings * 12 * annual_interest_rate))

print(f'Projected savings after one year, with interest, is: {projection_saving}')