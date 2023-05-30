import csv

# Write to CSV file

def write_csv(file_path, *args):
     with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(args)

# Test

if __name__ == '__main__':
    write_csv('test.csv', 'a', 'b', 'c')
    write_csv('test.csv', 'd', 'e', 'f')