import os,json
import errno
import csv
def write_json(data,filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def write_csv(data,filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    data_file = open(filename,'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for i in data:
        if count == 0:
            header = i.keys()
            csv_writer.writerow(header)
            count +=1
        csv_writer.writerow(i.values())
    data_file.close()
