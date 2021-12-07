import sys
import unittest

sys.path.insert(0,'..')
csvCombiner = __import__('csv-combiner')

class TestCSVCombiner(unittest.TestCase):

    def test_csvCombiner(self):

        # declaring the filePaths
        filePaths = ['./fixtures/accessories.csv', './fixtures/clothing.csv']

        # calling the combineCSV function
        (headers,rows) = csvCombiner.combineCSV(filePaths)

        # testing length
        self.assertEqual(len(headers), 3, "Should be 3")
        self.assertEqual(len(rows), 4, "Should be 4")

        # testing headers values
        self.assertEqual(headers[0], 'email_hash', "Should be email_hash")
        self.assertEqual(headers[1], 'category', "Should be category")
        self.assertEqual(headers[2], 'filename', "Should be filename")

        # testing rows values
        self.assertEqual(rows[0][0], 'b9f6f2227', "Should be b9f6f2227")
        self.assertEqual(rows[0][1], 'Satchels', "Should be Satchels")
        self.assertEqual(rows[0][2], 'accessories.csv', "Should be accessories.csv")
        self.assertEqual(rows[1][0], 'a9e09ef2', "Should be a9e09ef2")
        self.assertEqual(rows[1][1], 'Purses', "Should be Purses")
        self.assertEqual(rows[1][2], 'accessories.csv', "Should be accessories.csv")
        self.assertEqual(rows[2][0], 'b9f6f2227', "Should be b9f6f2227")
        self.assertEqual(rows[2][1], 'Blouses', "Should be Satchels")
        self.assertEqual(rows[2][2], 'clothing.csv', "Should be clothing.csv")
        self.assertEqual(rows[3][0], 'c2b5fa9e0', "Should be c2b5fa9e0")
        self.assertEqual(rows[3][1], 'Shirts', "Should be Shirts")
        self.assertEqual(rows[3][2], 'clothing.csv', "Should be clothing.csv")
    
if __name__ == '__main__':
    unittest.main()