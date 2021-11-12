import sys
import csv

def combineCSV(filePaths):
    """
    combineCSV takes a list of file paths of the
    CSV files to be combined as parameter, combines
    them along with adding a third column displaying 
    the filename from which the row came from, and
    outputs the combined csv file to stdout.

    :param filePaths: a list of file paths of the CSV files to be combined
    :return: a tuple containing the headers in a list and the combined rows in a list
    """ 

    # declaring empty lists to store the headers and rows
    headers = []
    rows = []   

    for filePath in filePaths:
        
        # reading csv file
        with open(filePath, 'r') as csvfile:
            # creating a CSV reader object
            csvreader = csv.reader(csvfile)
        
            # extracting field names through first row
            headers = next(csvreader)

            # extracting the filename from the filePath
            filename = filePath.split('/')[2]

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row + [filename])

    # appending the filename column to the headers list
    headers.append('filename') 

    return (headers,rows)

if __name__ == '__main__':
    filePaths = sys.argv[1:]

    # retreiving the headers and rows from returned tuple
    (headers,rows) = combineCSV(filePaths)   

    # creating a csv writer object
    csvwriter = csv.writer(sys.stdout, delimiter='\t',lineterminator='\n')
        
    # writing the headers
    csvwriter.writerow(headers)
        
    # writing the data rows
    csvwriter.writerows(rows)
    