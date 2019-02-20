# Course Planner

### Overview
This application is used to help Augsburg students evaluate their progress toward
any given degree at the university.

### Functionality
This application will allow students to do the following
* Upload a transcript on our website.
* Analyze resulting data displaying the a student's percentage toward all majors
and minors offered at Augsburg.

### Current Status of Software
Currently, this project has a frontend website designed by Ikram using
bootstrap. The frontend also has a script that Max wrote using node.js that
scans the user's transcript and pulls relevant information such as class names
and credits.

This project also contains a python script, degreq.py, that Chase wrote, which
iterates across all of the major/minor programs listed online, scraping the text
displayed on each page to create objects out of each degree. These objects are 
then written to a .csv file to allow for comparison later.

Finally, the original authors created a Java scanner that builds objects out of
each class offered at Augsburg, listing the course number, title, description,
prerequisites, and more. We planned to use this to display information to the
frontend for the user.

At this point in time, these different pieces are working independently, and are
not yet linked together.

### Original Authors
Beteab

Matt

Mo

Tim

### This Project is being Completed by
Maxwell Herron

Ikram Mohamed

Chase Strickler


###### File Update History
Created 9/17/2018 - Matthew Muller

Updated 2/20/2019 - Chase Strickler
