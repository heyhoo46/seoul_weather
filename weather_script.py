# openweather api로 요청을 해서
# 그 결과를 csv로 저장하는 py 만들기

# openweather api로 요청을 해서
# 그 결과를 csv로 저장하는 py
import requests
import csv
from datetime import datetime
import os
API_KEY  = os.getenv("OPENWEATHER_API_KEY")
CITY = "Seoul"
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(url)
data = response.json()

# main -> temp
# main -> humidity
# weather -> description

temp = data["main"]["temp"]
humidyty = data["main"]["humidity"]
description = data["weather"][0]["description"]

timezone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(temp, humidyty, description, timezone)

# 위의 4개의 데이터를 가지는 csv 파일 생성
csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "description"]

# csv가 존재하면 True
file_exist = os.path.isfile("seoul_weather.csv")

# mode "a" -> if not file -> create
# is is file -> write
with open("seoul_weather.csv", "a", newline="") as file:
    writer = csv.writer(file)

    # 파일이 존재하지 않는다 -> 헤더가 없다
    if not file_exist:
        writer.writerow(header)

    writer.writerow([timezone, temp, humidyty, description])

    print("csv 저장완료")
