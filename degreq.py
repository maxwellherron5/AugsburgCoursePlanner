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
	if "business" in str:
		return("http://www.augsburg.edu/" + str)
	if "communication" in str:
		return("http://www.augsburg.edu/" + str)
	if "music" in str:
		return("http://www.augsburg.edu/" + str)
	if "medievalstudies" in str:
		return("http://www.augsburg.edu/" + str)
	else:
		return("http://www.augsburg.edu/" + str + "/degree-requirements")

def create_major(majors, titles, degrees, uls, majorkeyword, minorkeyword):
	for k in titles: #Only adds item to the major list if it has the word major or minor in it
		if majorkeyword in str(k):
			#print(str(k))
			#print("Appended: ", titles[k])
			this_ul = []
			children = uls.findChildren("li", recursive=False)
			
			for child in children: #Adds children of a ul tag to an array
				this_ul.append(str(child.text.strip().replace('<li>', '')))
			degree_requirements = DegreeRequirements(k, this_ul) #instance of class
			degrees.append(degree_requirements)	#add degree_requirements object to list

		if minorkeyword in str(k):
			#print("Appended: ", titles[k])
			this_ul = []
			children = uls.findChildren("li", recursive=False)
			
			for child in children:
				this_ul.append(str(child.text.strip().replace('<li>', '')))
			degree_requirements = DegreeRequirements(k, this_ul)
			degrees.append(degree_requirements)


def main():
	#Normal degrees hold the part of the URL for degrees that have similar HTML set up. The URL for all of these is www.augsburg.edu/{INSERT_COURSE}/degree-requirements
	#Psychology doesn't account for any concentrations
	normal_degrees = ["ais", "art", 
					  "biology/degrees/ba-biology/", "biology/degrees/bs-biology/", "biology/degrees/ba-life-sciences/", "biology/degrees/biopsychology/", 
					  "business/degree-requirements/business-administration/", "business/degree-requirements/accounting/", "business/degree-requirements/finance/", "business/degree-requirements/international-business/", "business/degree-requirements/management/", "business/degree-requirements/management-information-systems/", "business/degree-requirements/marketing/", 
					  "communication/degrees/communication-studies/", "communication/degrees/film/", "communication/degrees/new-media/",
					  "chemistry", "cs", 
					  "education/programs/sped/degree-requirements/", 
					  "economics", "english", "environmental", "womensstudies", "hpe", "languages", "mathematics",
					  "medievalstudies/program-details/", 
					  "music/programs/requirements/", 
					  "philosophy", "physics",  "politicalscience", "psychology", "religion", "socialwork/academics", "sociology", "theater", "urban"]
	degrees = []
	#Film does not account for tracks. See: http://www.augsburg.edu/communication/degrees/film/
	#Education major is suuuuuuper wacky and not at all uniform. Special education has been accounted for, but I'm not at all sure how to do the rest.
	#History is also wonky.
	for i in range(len(normal_degrees)):
		url = create_url(normal_degrees[i])

		majorkeyword = "Major"
		minorkeyword = "Minor"

		if "biology" in normal_degrees[i]:
			majorkeyword = "Bachelor"
			minorkeyword = "Bachelor"

		if "music" in normal_degrees[i]:
			majorkeyword = "Music"
			minorkeyword = "Music"	

		#properly appends the URL for a major
		majors = get_site(url)
		#finds the proper div
		x = [];

		if "/" in normal_degrees[i]:
			if "business" in normal_degrees[i]:
				x = majors.find_all('h3')

			if "communication" in normal_degrees[i]:
				x = majors.find_all('h3')

			if "education" in normal_degrees[i]:
				x = majors.find_all('h3')

			if "biology" in normal_degrees[i]:
				page_response = requests.get(url, timeout=5)
				page_content = BeautifulSoup(page_response.content, "html.parser")
				x = page_content.find(class_='entry-title')
			if "music" in normal_degrees[i]:
				x = majors.find_all('h2')
			if "medievalstudies" in normal_degrees[i]:
				x = majors.find_all('h2')

		else:
			x = majors.find_all('h2')

		titles = []
		uls = majors.ul #grabs all of the ul tags on the page
		uls.text

		for a in x: #This loop strips the list of all h2 tags
			if "/" in normal_degrees[i]:
				if "business" in normal_degrees[i]:
					titles.append(str(a.text.strip().replace('<h3>', '').replace('</h3>', '')))
			#		print(a.text)
				if "communication" in normal_degrees[i]:
					titles.append(str(a.text.strip().replace('<h3>', '').replace('</h3>', '')))
				if "education" in normal_degrees[i]:
					titles.append(str(a.text.strip().replace('<h3>', '').replace('</h3>', '')))
				if "biology" in normal_degrees[i]:
				 	titles.append(str(a.strip().replace('<h1 class="entry-title">', '').replace('</h1>', '')))
				 	#print(str(titles[0]))
				if "music" in normal_degrees[i]:
					titles.append(str(a.text.strip().replace('<h2>', '').replace('</h2>', '')))
				if "medievalstudies" in normal_degrees[i]:
					titles.append(str(a.text.strip().replace('<h2>', '').replace('</h2>', '')))
			else:
				titles.append(str(a.text.strip().replace('<h2>', '').replace('</h2>', '')))
		#print(titles)
		create_major(majors, titles, degrees, uls, majorkeyword, minorkeyword)		

	print_arr(degrees)

if __name__ == '__main__':
	main()  