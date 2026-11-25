# Read data from input file
with open("hello.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Count number of lines
line_count = len(lines)
print("No. of lines in file =", line_count)

# Extract first two lines
first_two_lines = lines[:2]

# Write first two lines into a new file
with open("Output.txt", "w") as file:
    file.writelines(first_two_lines)

print("\n First two line succesfully written to Output.txt")
