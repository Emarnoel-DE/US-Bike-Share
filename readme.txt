Project Overview

Overview

In this project, I made use of Python to explore data related to bike share systems for three major cities in the United States— "Chicago", "New York City", and "Washington". I wrote a python script to import the data and answer interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

What Software was Needed?
In achieving completion of this project, the following software requirements was applied:

Python 3, NumPy, and pandas installed using Anaconda
Jupiter Notebook.

Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I used data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I compared the system usage between three large cities: Chicago, New York City, and Washington, DC.

The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:

Gender
Birth Year



Statistics Computed
I learned about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, I wrote code to provide the following information:

#1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day
#2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)
#3 Trip duration

total travel time
average travel time
#4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

The Files:
chicago.csv
new_york_city.csv
washington.csv


References used
1. Python Beginner Tutorial 6 - Exceptions and Loops - https://www.youtube.com/watch?v=-4tA5PAH9uU&t=470s
2. JournalDev - https://www.journaldev.com/33182/python-add-to-list
3. Calculate minimums in Pandas without `zero`-values? - https://stackoverflow.com/questions/35608893/calculate-minimums-in-pandas-without-zero-values
4. Linuxhint - https://linuxhint.com/numpy-non-zero-min/
5. SparkByExamples - https://sparkbyexamples.com/pandas/pandas-convert-column-to-int/#:~:text=To%20convert%20a%20column%20that,use%20astype()%20to%20convert.&text=Copy-,Use%20DataFrame.,values%20with%20integer%20value%20zero.
6. LearnPython.com - https://learnpython.com/blog/python-case-sensitive/#:~:text=Approach%20No%201%3A%20Python%20String,easier%20to%20compare%20two%20strings.
7. Pandas - https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.weekday.html
8. PythonGuides - https://pythonguides.com/get-first-n-rows-of-pandas-dataframe/
9. DelftStack - https://www.delftstack.com/howto/python/keyboard-interrupt-python/#:~:text=The%20KeyboardInterrupt%20error%20occurs%20when,use%20exception%20handling%20in%20Python.
10. W3Schools - https://www.w3schools.com/python/ref_string_isdigit.asp
11. Python for Everybody "Exploring Data Using Python 3"- Dr. Charles R. Severance
12. https://review.udacity.com/?utm_campaign=ret_000_auto_ndxxx_submission-reviewed&utm_source=blueshift&utm_medium=email&utm_content=trigger_enterprise_eng_3001_submission_reviewed&bsft_clkid=95b6b579-afa2-4cc7-8d1f-118de99b89d2&bsft_uid=205c4ff5-649e-4e81-ba2c-0f5f5d1f0a1c&bsft_mid=746573b4-90e8-4233-8fa9-10e8ae6376e9&bsft_eid=958a87a5-d024-4cf3-9067-8f5314206556&bsft_txnid=32aa1218-e028-458c-9fb5-3d326483f2ef&bsft_mime_type=html&bsft_ek=2022-07-08T11%3A55%3A26Z&bsft_aaid=17bf3774-8c65-47da-9a84-c4f6169cf022&bsft_lx=2&bsft_tv=3#!/reviews/3584758
13. https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
14. https://stackoverflow.com/questions/32238886/numpy-module-has-no-attribute-arrange
15. https://pypi.org/project/tabulate/
16. https://pandas.pydata.org/docs/user_guide/options.html#overview