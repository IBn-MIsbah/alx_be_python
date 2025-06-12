import datetime 

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

print('Current date and time: ' + display_current_datetime())

def calculate_future_date(days):
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")

# Get user input
days_to_add = int(input('Enter the number of days to add to the current date: '))
print('Future date:', calculate_future_date(days_to_add))
