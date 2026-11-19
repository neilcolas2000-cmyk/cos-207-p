marks = [62, 75, 48, 90, 71] # list of int
subject = "WSU-COS 207" # str
average = sum(marks) / len(marks) # float
has_passed = average >= 50 # bool
for item in [marks, subject, average, has_passed]:
    print(f"{type(item).__name__:<6} {item}")
print(f"{subject}: n = {len(marks)}, mean = {average:.2f}")