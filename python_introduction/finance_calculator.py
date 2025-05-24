monthly_income = int(input('Enter your monthly income: '))
total_monthly_expens = int(input('Enter your total monthly expenses: '))

monthly_saving = monthly_income - total_monthly_expens

annual_interest_rate = 0.05

projection_saving = int(monthly_saving * 12 + ( monthly_saving * 12 * annual_interest_rate))

print(f'Projected savings after one year, with interest, is: {projection_saving}')