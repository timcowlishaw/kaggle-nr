import csv
import sys
if __name__ == "__main__":
  filename =  sys.argv[1]
  csv_file = open(filename)
  data = csv.reader(csv_file)
  with open(filename.replace("csv", "arff"), "w") as arff_file:
    data_list = list(data)
    header = data_list[0]
    arff_file.write("@RELATION digits\n")
    for field in header[1:]:
      arff_file.write("@ATTRIBUTE %s NUMERIC\n" % (field,))
    arff_file.write("@ATTRIBUTE class {0,1,2,3,4,5,6,7,8,9}\n")
    arff_file.write("\n")
    arff_file.write("@DATA\n")
    for row in data_list[1:]:
      arff_file.write(",".join(row[1:]+[row[0]]))
      arff_file.write("\n")

