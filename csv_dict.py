import csv

def csv_dict(file_name):
    f = open(file_name)
    datas = csv.reader(f)
    header = datas.next()
    for entry in datas:
        data = dict(zip(header, entry))
        yield(data)

