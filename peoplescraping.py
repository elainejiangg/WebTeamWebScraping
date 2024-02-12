import requests
from bs4 import BeautifulSoup
import csv

def search_linkedin(first_name, last_name):
    # Create a search query URL
    query = f"https://www.linkedin.com/pub/dir/?first={first_name}&last={last_name}"
    
    # Send a GET request to LinkedIn
    response = requests.get(query)
    
    # Parse the HTML content of the search results page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first search result
    result = soup.find("li", class_="search-result")
    
    # If there's a search result, extract basic information
    if result:
        name = result.find("span", class_="name").text.strip()
        occupation = result.find("p", class_="subline-level-1").text.strip()
        location = result.find("p", class_="subline-level-2").text.strip()
        return name, occupation, location
    else:
        return None, None, None

def main():
    # Read the names from a CSV file
    with open('names.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            first_name, last_name = row[0], row[1]
            
            # Search LinkedIn for the person
            name, occupation, location = search_linkedin(first_name, last_name)
            
            # Write the information to a new CSV file
            with open('linkedin_info.csv', mode='a', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([first_name, last_name, name, occupation, location])

if __name__ == "__main__":
    main()
