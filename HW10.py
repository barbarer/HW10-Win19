# Import statements
import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import json
import unittest

## [PART 1]
# Finish writing the function getDayDict which takes a database file name and returns a
# dictionary that has the days of the weeks as the keys (using "Sun", "Mon", "Tue", 
# "Wed", "Thu", "Fri", "Sat") and the number of tweets on the named day as the values
#
# Hint: Look at the column names in the database first. Instructions are in the PDF.
#
# db_filename - the filename of the database
def get_day_dict(db_filename):

    pass

## [Part 2]
# Finish writing the function barchart_tweets_by_day which takes the dictionary and draws a bar 
# chart with the days of the week on the x axis and the number of tweets on the named day on 
# the y axis.  The chart must have an x label, y label, and title.  Save the chart as an image
# (using the save button is fine) and submit it on canvas.  
#
# day_dict - a dictionary with the days of the week as the keys and the number of tweets per
#            day as the values
def barchart_tweets_by_day(day_dict):
    
    pass    

## [Extra Credit]
# How does the number of tweets a person has compare to the number of favorites a person has?
# Finish writing the function drawBarChart which takes the database and draws a scatterplot
# with the number of tweets (the "statuses") on the x axis and the number of favorites ("favourites")
# on the y axis.  The chart must have an x label, y label, and title.  Save the chart to 
# "scatterplot.png" and submit it on canvas.  
#
# db_filename - the filename of a database with "statuses" and "favourites" columns in a table
def scatterplot_num_tweets_vs_num_favs(db_filename):

    pass


## Unittests, one for each day of the week 
class TestHW10(unittest.TestCase):

    def setUp(self):
        self.day_dict = get_day_dict("tweet_data.sqlite")

    def test_get_day_dict_mon(self):
        self.assertEqual(self.day_dict["Mon"], 1)

    def test_get_day_dict_tue(self):
        self.assertEqual(self.day_dict["Tue"], 9)

    def test_get_day_dict_wed(self):
        self.assertEqual(self.day_dict["Wed"], 2)

    def test_get_day_dict_thu(self):
        self.assertEqual(self.day_dict["Thu"], 72)

    def test_get_day_dict_fri(self):
        self.assertEqual(self.day_dict["Fri"], 2)

    def test_get_day_dict_sat(self):
        self.assertEqual(self.day_dict["Sat"], 6)

    def test_get_day_dict_sun(self):
        self.assertEqual(self.day_dict["Sun"], 39)


def main():


    # Comment out this line when you are ready to test the visualization functions!
    unittest.main(verbosity=2)

    # Uncomment to run barchart_tweets_by_day()
    #barchart_tweets_by_day(get_day_dict("tweet_data.sqlite"))

    # Uncomment to run the extra credit function
    #scatterplot_num_tweets_vs_num_favs("tweet_data.sqlite")



if __name__ == "__main__":
    
    main()
