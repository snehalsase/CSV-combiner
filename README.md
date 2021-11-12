# CSV-combiner

The folder is structured as mentioned in the description. I have used Python3 to finish the challenge. Some functions might not work 
if Python version earlier than 2.7 is used.

To run the csv-combiner.py script use the following command -

```
 $ python csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv  ./fixtures/household_cleaners.csv > combined.csv
 ```
On running this command in the shell, the CSV output would be written to the file whose name has been specified 
after the ```>``` character in the command, in the above command the output CSV file would be ```combined.csv``` .
Care should be taken that the ```fixtures``` directory containing the CSV files to be combined should be in the 
same folder as the csv-combiner.py script file to get the desired output (as mentioned in description of the challenge). 

## Testing

There is a test_csv-combiner.py script in the tests folder of the pmgAssesement Repository.

To run the tests in the test_csv-combiner.py script use the following command -

```
 $ python test_csv-combiner.py
 ```
 The unit tests have been designed taking into consideration the CSV files present in the fixtures directory of the tests folder.
 Care should be taken that the ```fixtures``` directory containing the CSV files to be tested should be in the
 same folder as the test_csv-combiner.py script file for the tests to pass.
 
 
