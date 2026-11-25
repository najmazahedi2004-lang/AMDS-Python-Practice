temperatures = [29.5, 31.0, None, 33.5, 34.0, 32.0, 35.5,
                36.0, None, 30.5, 28.0, 37.0, 38.0, 34.5]

clean_temperatures = []
missing_indices = []


for i in range(len(temperatures)):
    if temperatures[i] is None:
        missing_indices.append(i)
        continue

    clean_temperatures.append(temperatures[i])


mean_temp = sum(clean_temperatures) / len(clean_temperatures)
minimum = min(clean_temperatures)
maximum = max(clean_temperatures)


above_mean = []

for temp in clean_temperatures:
    if temp > mean_temp:
        above_mean.append(temp)


hot_days = 0
current_run = 0
longest_run = 0

for temp in temperatures:
    if temp is not None and temp >= 35:
        hot_days += 1
        current_run += 1

        if current_run > longest_run:
            longest_run = current_run
    else:
        current_run = 0

print("Clean temperatures:", clean_temperatures)
print("Mean temperature:", format(mean_temp, ".2f"))
print("Minimum temperature:", format(minimum, ".2f"))
print("Maximum temperature:", format(maximum, ".2f"))
print("Temperatures above mean:", above_mean)
print("Number of hot days:", hot_days)
print("Longest consecutive run of hot days:", longest_run)
print("Indices of missing readings:", missing_indices)