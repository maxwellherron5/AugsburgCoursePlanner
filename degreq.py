from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys

class DegreeRequirements:

	def __init__(self, major, classes):
		self.name = major
		self.courses = classes.copy()

	def print_arr(self, list):
		"""
		Prints out the list
		"""
		for i in range(len(list)-1):
			print("----------", list[i].name, "----------")
			print()
			for j in range(len(list[i].courses)):
				print(list[i].courses[j])
			print()

def get_site(url):
	page_response = requests.get(url, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#gets the page

	content = page_content.find(class_='entry-content')
	return(content)

def create_url(str):

	return("http://www.augsburg.edu/" + str + "/degree-requirements")

def main():
	#Normal degrees hold the part of the URL for degrees that have similar HTML set up. The URL for all of these is www.augsburg.edu/{INSERT_COURSE}/degree-requirements
	#Psychology doesn't account for any concentrations
	normal_degrees = ["ais", "art", "chemistry", "cs", "economics", "economics", "english", "environmental", "womensstudies", "hpe", "languages", "mathematics", "philosophy", "physics",  "politicalscience", "psychology", "religion", "socialwork/academics", "sociology", "theater", "urban"]

	other_degrees = ["biology", "business", "communication", "music"]
	degrees = []

	#Education major is suuuuuuper wacky and not at all uniform.
	#History is also wonky.
	#Medieval Studies ends in /program-details/

	for i in range(len(normal_degrees)-1): #loops for all degrees
		url = create_url(normal_degrees[i])
		
		#properly appends the URL for a major
		majors = get_site(url)
		#finds the proper div

		x = majors.find_all('h2')
		y = [] #temporary list to hold all h2 in the entry-content div
		y.append(x)

		titles = []
		uls = majors.ul #grabs all of the ul tags on the page
		uls.text
		#print(uls.text)
		
		for a in x: #This loop strips the list of all h2 tags
			titles.append(str(a.text.strip().replace('<h2>', '').replace('</h2>', '')))


		for k in range(len(titles)-1): #Only adds item to the major list if it has the word major or minor in it
			if "Major" in str(titles[k]):
				#print("Appended: ", titles[k])
				this_ul = []
				children = uls.findChildren("li", recursive=False)
				
				for child in children: #Adds children of a ul tag to an array
					this_ul.append(str(child.text.strip().replace('<li>', '')))
				degree_requirements = DegreeRequirements(titles[k], this_ul) #instance of class
				degrees.append(degree_requirements)	#add degree_requirements object to list

			if "Minor" in str(titles[k]):
				#print("Appended: ", titles[k])
				this_ul = []
				children = uls.findChildren("li", recursive=False)
				
				for child in children:
					this_ul.append(str(child.text.strip().replace('<li>', '')))
				degree_requirements = DegreeRequirements(titles[k], this_ul)
				degrees.append(degree_requirements)				

	degree_requirements.print_arr(degrees)

if __name__ == '__main__':
	main()  