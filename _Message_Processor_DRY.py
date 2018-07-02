import csv
import os


input_file = "test.txt"
dictionary = "dictionary.csv"
output_file = os.path.splitext(input_file)[0] + "_translated.txt"
# x12file = "C:/Users/p365739/PycharmProjects/Python/data.txt"
# x12file = "/Users/p365739/PycharmProjects/Python/data.txt"
print("")
print("")

# Reference for CSV usage https://www.alexkras.com/how-to-read-csv-file-in-python/
with open(dictionary, "r") as csv_file:
    reader = csv.reader(csv_file)
    dict_data = [row for row in reader]  # Declare variable data to store csv columns into a table
    print("DICTIONARY: " + str(dict_data))
    print("")


# Read input file into list
with open(input_file, "r+") as file:
    file_lines = str(file.readlines())
    print("INPUT: " + str(file_lines))
    print("")



# Replace the target string
# Reference For/In loop at http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
for key, value in dict_data:
    file_lines = file_lines.replace(key, value)


print("OUTPUT: " + str(file_lines))
