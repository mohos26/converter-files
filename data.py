import pandas as pd
import sqlite3


def get_type(name: str):
	d = {
		"csv": "csv",
		("xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt"): "excel",
		"txt": "text",
		"json": "json",
		"xml": "xml",
		("sqlite", "sqlite3", "db"): "sql"
	}
	splitted = name.split('.')
	for key in d:
		if type(key) is tuple:
			for sublist in key:
				if splitted[1] == sublist:
					return d[key]
		else :
			if splitted[1] == key:
				return d[key]
	return None


def convert(type_entered :str, type_to_convert: str, path: str, name_of_converted: str):
	types = ["csv", "text", "excel", "json", "sql", "database", "xml"]
	splitted = path.split('/')
	new_path = splitted[-1]
	our_type = get_type(new_path)
	if our_type == None:
		print("Not a valid type")
	else :
		type_entered = our_type
	if type_entered == "csv" or type_entered == "text":
		dt = pd.read_csv(path)
	elif type_entered == "xml":
		dt = pd.read_xml(path)
	elif type_entered == "json":
		dt = pd.read_json(path)
	elif type_entered == "excel":
		print("entered")
		dt = pd.read_excel(path)
	elif type_entered == "sql":
		dt = pd.read_sql_table(path)

	if type_to_convert == "csv" or type_to_convert == "text":
		print("here", name_of_converted)
		dt.to_csv(name_of_converted)
	elif type_to_convert == "xml":
		dt.to_xml(name_of_converted)
	elif type_to_convert == "json":
		dt.to_json(name_of_converted)
	elif type_to_convert == "excel":
		dt.to_excel(name_of_converted)
	elif type_to_convert == "sql":
		dt.to_sql(name_of_converted)


