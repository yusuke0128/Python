#-*-coding:utf-8-*-
import jsm
import datetime

q = jsm.Quotes()

print("株価を知りたい会社の証券コードを入力してください\n")
num = input()
today = datetime.date.today()
start_date =datetime.date(today.year,today.month,1)
end_date = today
days = abs(start_date - today)
n = days.days

stock = q.get_historical_prices(num,jsm.DAILY,start_date=start_date,end_date=end_date)

stock_list = [each_day_data.date for each_day_data in stock]

date_list = [each_day_data.date for each_day_data in stock]

open_list = [each_day_data.open for each_day_data in stock]

close_list = [each_day_data.close for each_day_data in stock]

high_list = [each_day_data.high for each_day_data in stock]

low_list = [each_day_data.low for each_day_data in stock]

for (date, open, close, high, low) in zip(date_list[0:n], open_list[0:n],close_list[0:n],high_list[0:n],high_list[0:n]):
 print(date, open, close, high, low)
