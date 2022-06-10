import re
pattern_1 = r"10:[0-5][0-9]:[0-5][0-9].*([4-5][0-9][0-9]).*"
input_file = open("../../../../Desktop/access.log.txt", mode='r')
my_log_file = input_file.read()
result = re.findall(pattern_1 , my_log_file)
print(result)
print(len(result))