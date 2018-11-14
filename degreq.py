from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys

class DegreeRequirements:

	def __init__(self, major, classes):
		self.name = major
		self.courses = classes.copy()

def print_arr(list):
	"""
	Prints out a given list.
	"""
	for i in range(len(list)-1):
		print("----------", list[i].name, "----------")
		print()
		for j in range(len(list[i].courses)):
			print(list[i].courses[j])
		print()

def get_site(url):
	"""
	Given a url, this function will get the contents of the page.
	"""
	page_response = requests.get(url, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#gets the page

	content = page_content.find(class_='entry-content')
	return(content)

def create_url(str):
	"""
	Concatenates a strings to make a url of a given item in the degree requirements list.
	"""
	if "biology" in str:
		return("http://www.augsburg.edu/" + str)
	else:
		return("http://www.augsburg.edu/" + str + "/degree-requirements")

def create_major(majors, titles, degrees, uls, majorkeyword, minorkeyword):
	for k in range(len(titles)-1): #Only adds item to the major list if it has the word major or minor in it
		if majorkeyword in str(titles[k]):
			#print("Appended: ", titles[k])
			this_ul = []
			children = uls.findChildren("li", recursive=False)
			
			for child in children: #Adds children of a ul tag to an array
				this_ul.append(str(child.text.strip().replace('<li>', '')))
			degree_requirements = DegreeRequirements(titles[k], this_ul) #instance of class
			degrees.append(degree_requirements)	#add degree_requirements object to list

		if minorkeyword in str(titles[k]):
			#print("Appended: ", titles[k])
			this_ul = []
			children = uls.findChildren("li", recursive=False)
			
			for child in children:
				this_ul.append(str(child.text.strip().replace('<li>', '')))
			degree_requirements = DegreeRequirements(titles[k], this_ul)
			degrees.append(degree_requirements)


def main():
	#Normal degrees hold the part of the URL for degrees that have similar HTML set up. The URL for all of these is www.augsburg.edu/{INSERT_COURSE}/degree-requirements
	#Psychology doesn't account for any concentrations
	normal_degrees = ["ais", "art", "biology/degrees/ba-biology/", "biology/degrees/bs-biology/", "biology/degrees/ba-life-sciences/", "biology/degrees/biopsychology/", "chemistry", "cs", "economics", "economics", "english", "environmental", "womensstudies", "hpe", "languages", "mathematics", "philosophy", "physics",  "politicalscience", "psychology", "religion", "socialwork/academics", "sociology", "theater", "urban"]

	other_degrees = ["business", "communication", "music"]
	degrees = []

	#Education major is suuuuuuper wacky and not at all uniform.
	#History is also wonky.
	#Medieval Studies ends in /program-details/
	for i in range(len(normal_degrees)):
		url = create_url(normal_degrees[i])

		majorkeyword = "Major"
		minorkeyword = "Minor"

		if "biology" in normal_degrees[i]:
			majorkeyword = "Biology"
			minorkeyword = "Biology"

		#properly appends the URL for a major
		majors = get_site(url)
		#finds the proper div

		if "biology" in normal_degrees[i]:
			page_response = requests.get(url, timeout=5)
			page_content = BeautifulSoup(page_response.content, "html.parser")
			x = page_content.find(class_='entry-title')
		else:
			x = majors.find_all('h2')

		y = [] #temporary list to hold all h2 in the entry-content div
		y.append(x)

		titles = []
		uls = majors.ul #grabs all of the ul tags on the page
		uls.text

		for a in x: #This loop strips the list of all h2 tags
			if "biology" in normal_degrees[i]:
			 	titles.append(str(a.strip().replace('<h1 class="entry-title">', '').replace('</h1>', '')))
			else:
				titles.append(str(a.text.strip().replace('<h2>', '').replace('</h2>', '')))

		#print(titles)
		create_major(majors, titles, degrees, uls, majorkeyword, minorkeyword)		

	print_arr(degrees)

if __name__ == '__main__':
	main()  