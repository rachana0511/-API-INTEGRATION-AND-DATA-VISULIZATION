import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your OpenWeatherMap API key
API_KEY = "820442a1bff8e474e985d4618ea7ed22"
CITY = "New York"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(URL)
data = response.json()

# Extract relevant information
temp_list = []
date_list = []

for item in data['list']:
    temp_list.append(item['main']['temp'])
    date_list.append(item['dt_txt'])

# Create DataFrame
df = pd.DataFrame({"Date": date_list, "Temperature": temp_list})
df["Date"] = pd.to_datetime(df["Date"])

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Temperature", data=df, marker="o")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Forecast for {CITY}")
plt.xticks(rotation=45)
plt.grid()
plt.show()

