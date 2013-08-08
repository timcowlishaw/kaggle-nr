import sqlite3
import csv
if __name__ == "__main__":
  datasets = ["train", "test"]
  conn = sqlite3.connect("data/data.sqlite")
  cur = conn.cursor()
  for dataset in datasets:
    print dataset
    csv_file = open("data/%s.csv" % (dataset,))
    data = csv.reader(csv_file)
    data_list = list(data)
    header = data_list[0]
    fields = ",".join(["%s INT" % (name,) for name in header])
    string = "CREATE TABLE %s (%s)" % (dataset, fields)
    cur.execute(string)
    for row in data_list[1:]:
      cur.execute("INSERT INTO %s VALUES (%s)" % (dataset, ",".join(row)))
  conn.commit()
