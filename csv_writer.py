import csv

# function that writes its parameters into a csv
# if the csv file does not exist, it creates one and writes in it
# if it exists it appends to it


def write_csv(file_path, *args):

    with open(file_path, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(args)

# for testing

if __name__ == '__main__':
    write_csv('test.csv', 'a', 'b', 'c', 'd', 'e', 'f')
    write_csv('test.csv', 'g', 'h', 'i', 'j', 'k', 'l')