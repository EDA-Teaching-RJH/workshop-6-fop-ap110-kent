# Task 1.1: The stoarge bay 
sample_bay = ["Basalts", "Silica", "Iron", "Dust"]

print("First Bay Sample: ", sample_bay[0])
print("Last Bay Sample: ", sample_bay[-1])
print("Total Number of Samples: ",len(sample_bay))

# Task 1.2: Analsying Samples (Iteration)

for sample in sample_bay:
    print(f"Transmitting data for: {sample}")

# Task 1.3: Collection Duty (Appending)
new_findings = [ ]
for _ in range(3):
    rocks = input("Type of Rocks found: ")
    new_findings.append(rocks)

#Task 1.4: Jettisoning waste (Extension)
sample_bay = ["Basalts", "Silica", "Iron", "Dust"]
sample_bay.remove("Dust")
print(sample_bay)