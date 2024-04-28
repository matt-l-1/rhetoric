from bs4 import BeautifulSoup
import requests
import csv

base_url = "http://www.britishpoliticalspeech.org/speech-archive.htm"

def scrape_speeches(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize a list to store speech data
    speeches = []
    
    # Send an HTTP GET request to the speech URL
    speech_response = requests.get(url)
    speech_soup = BeautifulSoup(speech_response.text, 'html.parser')
    
    # Extract speech text
    speech_text = ""
    speech_content = speech_soup.find('div', class_='speech-content')
    if speech_content:
        speech_text = speech_content.get_text()
    speaker = ""
    speech_speaker = speech_soup.find('p', class_='speech-speaker')
    if speech_speaker:
        speaker = speech_speaker.get_text()

    year = ""
    speech = speech_soup.find('div', class_='speech')
    if speech:
        year = speech.find('h3')
        year = str(year)[-9:-5]
    
    # Add speech data to the list
    speeches.append({
        'url': url,
        'text': speech_text,
        'speaker': speaker,
        'year': year
    })
    
    return speeches

def scrape_multiple_pages(base_url):
    # Initialize a list to store all speeches
    all_speeches = []
    
    # Start with the first page
    current_page = 1
    while current_page < 400:
        # Construct the URL of the current page
        page_url = base_url + f"?speech={current_page}"
        
        # Scrape speeches from the current page
        speeches = scrape_speeches(page_url)
        
        # Check if there are no more speeches on the page
        if not speeches:
            break
        
        # Add speeches to the list of all speeches
        all_speeches.extend(speeches)
        
        # Move to the next page
        current_page += 1
    
    return all_speeches

def main():
    # Scrape speeches from all pages
    all_speeches = scrape_multiple_pages(base_url)
    
    # Save speeches to a CSV file
    with open('speeches.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'text', 'speaker', 'year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for speech in all_speeches:
            writer.writerow(speech)

if __name__ == "__main__":
    main()


