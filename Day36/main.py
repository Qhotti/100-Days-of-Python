import requests
import datetime as dt


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = 'R1VH5AA8UR7X91T2'
NEWS_API_KEY = 'dbeb41773002420f978bad910c0789cd'
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today = dt.datetime.now()
current_date = today.date()
yesterday = current_date - dt.timedelta(days=1)
day_before_yesterday = current_date - dt.timedelta(days=2)

stock_parameters={
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

stock_response = requests.get(url = STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()['Time Series (Daily)']

news_parameters={
    'q':COMPANY_NAME,
    'sortBy': 'popularity',
    'sources': 'bbc-news',
    'apikey': NEWS_API_KEY
    
}


news_response = requests.get(url = NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()




#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_list = [value for (key, value) in stock_data.items()]

yesterday_stocks = stock_list[1]
yesterday_closing = list(yesterday_stocks.values())[3]


# print(yesterday_closing)


#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_stocks = stock_list[2]
day_before_yesterday_closing = list(day_before_yesterday_stocks.values())[3]
int_yesterday_closing = int(float(yesterday_closing))
int_day_before_yesterday_closing = int(float(day_before_yesterday_closing))
# print(day_before_yesterday_closing)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(int_yesterday_closing - int_day_before_yesterday_closing)
# print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

difference_percentage = round(abs((difference / int_day_before_yesterday_closing)* 100),1)


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if difference_percentage > 5:
    print('Get News')
    

## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
first_three = news_data['articles'][0:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
list = [f"Headline: {article['title']}. \nDescription: {article['description']}." for article in first_three]
print(list)
#TODO 9. - Send each article as a separate message via Twilio. 

#nah


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

