# Import libraries that we need (urllib, beautifulsoup, JSON, Tkinter)
import urllib.request
from bs4 import BeautifulSoup 
import json
from tkinter import *

class Scraper(Frame):
	# Initializes Scraper class
	def __init__(self, master):
		# Initializes frame
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.label1 = Label(self, text = "*Enter the webpage's URL: ")
		self.label1.grid(row = 0, column = 0, sticky = W)
		self.web_url = Entry(self)
		self.web_url.grid(row = 0, column = 100, sticky= W)
		
		self.label2 = Label(self, text = "*Enter the main HTML tag: \n('div', 'table', 'article', etc.)")
		self.label2.grid(row = 100, column = 0, sticky = W)
		self.main_tag = Entry(self)
		self.main_tag.grid(row = 100, column = 100, sticky = W)

		self.label3 = Label(self, text = "*Enter the tag's attribute type: \n('class', 'id', 'width', etc.)")
		self.label3.grid(row = 200, column = 0, sticky = W)
		self.main_attr = Entry(self)
		self.main_attr.grid(row = 200, column = 100, sticky = W)

		self.label4 = Label(self, text = "*Enter the text in the attribute: ")
		self.label4.grid(row = 300, column = 0, sticky = W)
		self.main_filter = Entry(self)
		self.main_filter.grid(row = 300, column = 100, sticky = W)

		self.label5 = Label(self, text = "*Enter the specific internal tag: ")
		self.label5.grid(row = 400, column = 0, sticky = W)
		self.in_tag = Entry(self)
		self.in_tag.grid(row = 400, column = 100, sticky = W)

		self.label6 = Label(self, text = "Enter the internal tag's attribute type (if any): ")
		self.label6.grid(row = 500, column = 0, sticky = W)
		self.in_attr = Entry(self)
		self.in_attr.grid(row = 500, column = 100, sticky = W)	

		self.label7 = Label(self, text = "Enter the text in the attribute: ")
		self.label7.grid(row = 600, column = 0, sticky = W)
		self.in_filter = Entry(self)
		self.in_filter.grid(row = 600, column = 100, sticky = W)

		# SUBMIT Button -> command will be function for web scraping
		self.submit_button = Button(self, text = "Go Scrape!", command = self.go_scrape)
		self.submit_button.grid(sticky = W)
		self.label8 = Label(self, text = "(* = REQUIRED)")
		self.label8.grid(sticky = W)

		# Text box for errors and messages
		self.error = Text(self, width = 70, height = 5, wrap = WORD)
		self.error.grid(row = 700, column = 0, columnspan = 200, sticky = W)

	def go_scrape(self):
		# Scrape information based on the user specified tags 
		url = self.web_url.get()
		# Error check for 
		if(len(url) == 0):
			self.error.delete(0.0, END)
			self.error.insert(0.0, "Please provide a webpage URL")
			return
		#download the URL and extract the content to the variable html 
		request = urllib.request.Request(str(url))
		html = urllib.request.urlopen(request).read()
		# Get rest of the entries from user 
		tag = self.main_tag.get()
		attr = self.main_attr.get()
		filt = self.main_filter.get()
		inside_tag = self.in_tag.get()
		inside_attr = self.in_attr.get()
		inside_filter = self.in_filter.get()

		# Error check for other missing information 
		if(len(tag) == 0):
			self.error.delete(0.0, END)
			self.error.insert(0.0, "Please provide a main HTML tag")
			return
		if(len(attr) == 0):
			self.error.delete(0.0, END)
			self.error.insert(0.0, "Please provide the attribute of the main tag")
			return
		if(len(filt) == 0):
			self.error.delete(0.0, END)
			self.error.insert(0.0, "Please provide the text in the attribute")
			return
		if(len(inside_tag) == 0):
			self.error.delete(0.0, END)
			self.error.insert(0.0, "Please provide an internal tag (tag within the main tag)")
			return
		
		# Pass the HTML to Beautifulsoup based off what the user inputs. 
		if (len(inside_tag) == 0):
			soup = BeautifulSoup(html, 'html.parser')
			content_area = soup.find_all(tag, attrs={attr:filt})
		elif(len(inside_attr) == 0):
			soup = BeautifulSoup(html, 'html.parser')
			main_table = soup.find(tag, attrs={attr:filt})
			if(main_table is None):
				self.error.delete(0.0, END)
				self.error.insert(0.0, "Hmm.. It seems that there is an error.\nTry changing the main tag or its properties.\nCheck for typos!!!")
			content_area = main_table.find_all(inside_tag)
		elif(len(inside_filter) == 0):
			soup = BeautifulSoup(html, 'html.parser')
			main_table = soup.find(tag, attrs={attr:filt})
			if(main_table is None):
				self.error.delete(0.0, END)
				self.error.insert(0.0, "Hmm.. It seems that there is an error.\nTry changing the main tag or its properties.\nCheck for typos!!!")
			content_area = main_table.find_all(inside_tag, attrs={inside_attr})
		else:
			soup = BeautifulSoup(html, 'html.parser')
			main_table = soup.find(tag, attrs={attr:filt})
			if(main_table is None):
				self.error.delete(0.0, END)
				self.error.insert(0.0, "Hmm.. It seems that there is an error.\nTry changing the main tag or its properties.\nCheck for typos!!!")
			content_area = main_table.find_all(inside_tag, attrs={inside_attr:inside_filter})

		extracted_records = []
		for paragraphs in content_area:
			if not (paragraphs.text == ""):
				content = paragraphs.text
				record = {
					'Content':content
				}
				extracted_records.append(record)

		if(len(extracted_records) == 0):
			self.error.delete(0.0, END)
			self.error.insert(0.0, "Hmm.. It seems that nothing was scraped.\nTry changing the tags or its properties.\nCheck for typos!!!")
		else:
			self.error.delete(0.0, END)
			self.error.insert(0.0, "Scrape Successful!\nYour data is waiting for you in the file patch_scraper_data.json")
		print(extracted_records)

		with open('patch_scraper_data.json', 'w') as outfile:
			json.dump(extracted_records, outfile)
		

root = Tk()
root.title("Simple Patch Scraper")
root.geometry("500x310")

scrape = Scraper(root)

root.mainloop()