numbers = [3, 5, -7, 8, -88]
total_positives = 0

for number in numbers:
    if number >= 0:
        print(number)
        total_positives += 1

print("Total positives:", total_positives)
        