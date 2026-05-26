from collections import Counter
fileName = "app.log"
count = Counter()

with open(fileName, 'r') as file:
    for line in file:
        if "INFO" in line:
            count["INFO"] += 1
        elif "ERROR" in line:
            count["ERROR"] += 1
        elif "WARNING" in line:
            count["WARNING"] += 1

print("\nSummary Table")
print("-" * 20)
print(f"{"Level":<10} {"Count":<10}")
print("-" * 20)

for key,value in count.items():
    print(f"{key:<10} {value:<10}")