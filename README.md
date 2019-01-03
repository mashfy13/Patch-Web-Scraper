# Patch-Web-Scraper
Web Scraper to pull information from FAQ pages using the HTML tags of the web page 

Simple Patch Scraper Version 1.0 08/10/2018

GENERAL USAGE NOTES
--------------------------------------------------------------------------

- This application uses a Python Library called BeautifulSoup to 
  scrape information from webpages based on the user specified 
  HTML tags. 
  
- The purpose of this application is to scrape questions and answers
  from different FAQ pages about health insurance and employee benefits.
  
- The user must right click on the desired webpage and inspect element 
  on the site. The user must then find the main HTML tag where the main
  content to be scraped is all under. Specify the tag, its attribute type, 
  and name in the corresponding boxes of the application. Then find the 
  tag that all of the content is separated into (i.e. most answers of a 
  question will be in 'p' tags) and specify that as the internal tag. 
  The internal tag can have attributes as well but it is not required 
  in order to get the scraper to pull information. 
  
- Be very specific with the tags that you are choosing to scrape the 
  desired information and make sure that all of the pieces of 
  information are formatted with the same tags and attributes in order to 
  maximize the scraping results. 
  
Installing under Windows/Mac OS/Linux 
---------------------------------------------------------------------------
In order to run the Simple Patch Scraper, after the downloading the files,
you must make sure that you have Python installed on your device as well as
the Tkinter package for GUI. Follow the instructions on the following page, 
based on your OS (Windows, Mac, Linux), with the exception of Step #3 to 
install python and the Tkinter package:  
- http://www.greenteapress.com/thinkpython/swampy/install.html
After intsalling python and the Tkinter package you must install the 
BeautifulSoup library which allows web scraping functionalities. Follow the 
instructions in the following link to acquire this library. 
- https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python
Once you have all of these things installed on your device, go on terminal, 
navigate to the folder containing the patch_scraper.py file, and then type 
in 'python patch_scraper.py' to run the program. A small desktop application
should appear where you can begin scraping. 
**NOTE: if you are using python version 3, you may have to use the command:
  'python3 patch_scraper.py' INSTEAD
===========================================================================

The creator of Simple Patch Scraper can be reached at: 

Voice: 347-607-4808
Email: mashfy13@gmail.com

Copyright 2018 Patch. All rights reserved. 
