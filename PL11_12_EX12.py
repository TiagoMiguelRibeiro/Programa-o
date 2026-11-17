with open("logs.txt", "r", encoding="utf-8") as log_file:
	error_lines = [line for line in log_file if line.lstrip().startswith("[ERROR]")]

with open("error_logs.txt", "w", encoding="utf-8") as error_file:
	error_file.writelines(error_lines)


file = open('error_logs.txt', 'r')

print(file.read())