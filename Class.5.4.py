words = ["model", "data", "python", "data",
         "model", "analysis", "data"]

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

repeated_words = []

for word in frequency:
    if frequency[word] > 1:
        repeated_words.append(word)

print("Frequency:", frequency)
print("Repeated words:", repeated_words)
