import pandas as pd
import sqlite3

# type_enterd = input("enter the type of the file entered: ")
# path = input("enter the path of the file to convert(if it is in this directory just enter it's name): ")
# type_to_convert, name_of_converted = input("enter the type of the file to convert to and the name of the desired file:(please enter two names and between them a space) ").split(max=2)
# if type_entered.replace(".", "").lower() == "csv":
# 	s = input("if the seperator is not (,) please enter the seperator in your file: ")
# 	h = int(input("if there is a header in the file, enter it's row, the index of the first row is 0: "))
# 	if (s != ""):
# 		if h == "":
# 			dt = pd.read_csv(path, sep=s, header=None, na_values=["NA", ""], parse_dates=[Dates], dayfirst=True)
# 		else :
# 			dt = pd.read_csv(path, sep=s, header=h, na_values=["NA", ""], parse_dates=[Dates], dayfirst=True)
# 	else :
# 		if h == "":
# 			dt = pd.read_csv(path, header=None, na_values=["NA", ""], parse_dates=[Dates], dayfirst=True)
# 		else :
# 			dt = pd.read_csv(path, header=h, na_values=["NA", ""], parse_dates=[Dates], dayfirst=True)
# if type_entered.replace(".", "").lower() == "xlsx" or type_entered.replace(".", "").lower() == "xls" or type_entered.lower() == "excel":)
def get_type(name: str):
	d = {"csv":"csv", ("xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt"): "excel", "txt":"text", "json":"json", "xml":"xml", ("sqlite", "sqlite3", "db"):"sql"}
	splitted = name.split('.')
	for key in d:
		if type(key) is tuple:
			for sublist in key:
				if splitted[1] == sublist:
					return d[key]
		else :
			if splitted[1] == key:
				d[key]
	return None

types = ["csv", "text", "excel", "json", "sql", "database", "xml"]
check = 0
while (1):
	type_entered = input("enter the type of the file entered: ")
	for item in types:
		if type_entered.lower().strip() == item:
			check = 1
			break
	if check == 1:
		break
	print(f"the supported types are: csv, sql, text (.txt), database, excel, json, xml.")
	print(f"if you are unsure about the type of file you have, please choose the auto-detect option")


path = input("enter the path of the file to convert(if it is in this directory just enter it's name): ")
if '/' in path:
	splitted = path.split('/')
	new_path = splitted[-1]
else :
	new_path = path
our_type = get_type(new_path)
if our_type == None:
	print("Not a valid type")
else :
	type_entered = our_type
check = 0
while (1):
	type_to_convert = input("enter the type of the file to convert to: ")
	for item in types:
		if type_to_convert.lower() == item:
			check = 1
			break
	if check == 1:
		break
	print(f"the supported types are: csv, sql, text (.txt), database, excel, json, xml.")
name_of_converted = input("enter the name of the desired file: ")
if type_entered == "csv" or type_entered == "text":
	dt = pd.read_csv(path)
elif type_entered == "xml":
	dt = pd.read_xml(path)
elif type_entered == "json":
	dt = pd.read_json(path)
elif type_entered == "excel":
	dt = pd.read_excel(path)
elif type_entered == "sql":
	dt = pd.read_sql_table(path)

if type_to_convert == "csv" or type_to_convert == "text":
	dt.to_csv(name_of_converted)
elif type_to_convert == "xml":
	dt.to_xml(name_of_converted)
elif type_to_convert == "json":
	dt.to_json(name_of_converted)
elif type_to_convert == "excel":
	dt.to_excel(name_of_converted)
elif type_to_convert == "sql":
	dt.to_sql(name_of_converted)


