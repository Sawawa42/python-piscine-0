import time, datetime

unixtime = time.time()
now = datetime.datetime.now()
formatted_time = now.strftime("%b %d %Y")

# 4fで小数点以下4桁まで表示する
# 2eで小数点以下2桁までの指数表記で表示する
print("Seconds since January 1, 1970:", f"{unixtime:.4f}", "or", f"{unixtime:.2e}", "in scientific notation")
print(formatted_time)