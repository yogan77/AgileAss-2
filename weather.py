# Sample 7-day weather dataset (Day, Temp in °C, Humidity %, Rainfall in mm)
weather_data = [
    {"day": "Day 1", "temperature": 32.5, "humidity": 65, "rainfall": 12.0},
    {"day": "Day 2", "temperature": 41.2, "humidity": 40, "rainfall": 0.0},
    {"day": "Day 3", "temperature": 43.0, "humidity": 35, "rainfall": 0.0},
    {"day": "Day 4", "temperature": 38.0, "humidity": 55, "rainfall": 4.5},
    {"day": "Day 5", "temperature": 22.1, "humidity": 85, "rainfall": 25.0},
    {"day": "Day 6", "temperature": 28.4, "humidity": 70, "rainfall": 8.0},
    {"day": "Day 7", "temperature": 35.0, "humidity": 50, "rainfall": 0.0}
]

# 1. Find the hottest day
hottest_day = max(weather_data, key=lambda x: x["temperature"])
print(f"Hottest Day: {hottest_day['day']} ({hottest_day['temperature']}°C)")

# 2. Find the coldest day
coldest_day = min(weather_data, key=lambda x: x["temperature"])
print(f"Coldest Day: {coldest_day['day']} ({coldest_day['temperature']}°C)")

# 3. Calculate average temperature
avg_temp = sum(day["temperature"] for day in weather_data) / len(weather_data)
print(f"Average Temperature: {avg_temp:.2f}°C")

# 4. Count rainy days (rainfall > 0)
rainy_days_count = sum(1 for day in weather_data if day["rainfall"] > 0)
print(f"Number of Rainy Days: {rainy_days_count}")

# 5. Identify heatwave days (temperature > 40°C)
heatwave_days = [day["day"] for day in weather_data if day["temperature"] > 40]
print(f"Heatwave Days (>40°C): {', '.join(heatwave_days) if heatwave_days else 'None'}")

# 6. Display data sorted by rainfall (descending order)
sorted_by_rainfall = sorted(weather_data, key=lambda x: x["rainfall"], reverse=True)
print("\nData Sorted by Rainfall (Highest to Lowest):")
print(f"{'Day':<8} | {'Rainfall (mm)':<13} | {'Temperature':<12} | {'Humidity (%)'}")
print("-" * 52)
for day in sorted_by_rainfall:
    print(f"{day['day']:<8} | {day['rainfall']:<13} | {day['temperature']:<12} | {day['humidity']}%")
