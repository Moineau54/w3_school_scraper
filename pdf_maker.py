import os
import requests
from bs4 import BeautifulSoup
from weasyprint import HTML



def scrape_to_pdf(page_url, output_dir, number):
    """
    page_url: URL of the page to scrape
    output_dir: Directory to save the PDF files
    number: Index of the PDF file
    Fetches the page content, extracts the main content, and converts it to a PDF.
    """
    # Get page content
    response = requests.get(page_url)
    if response.status_code != 200:
        print(f"Failed to retrieve {page_url}")
        return

    # Parse the content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the main content within the div#main
    main_content = soup.find("div", {"id": "main", "class": "w3-col l10 m12"})
    if not main_content:
        print(f"Main content not found on {page_url}")
        return

    # Extract title for the PDF file name
    title = soup.find("h1").get_text().strip().replace(" ", "_")
    title = title.replace("/", "_")
    if number < 10:
        filename = f"{output_dir}/0{number}.{title}.pdf"
    else:
        filename = f"{output_dir}/{number}.{title}.pdf"

    # Convert the extracted HTML to a PDF
    HTML(string=str(main_content)).write_pdf(filename)
    print(f"Saved {filename}")



def scrape_course_from_array(urls):
    """
    urls: list of URLs to scrape
    Makes the output directory and scrapes each URL using scrape_to_pdf.
    """
    # Create output directory if it doesn't exist
    list_of_contents = os.listdir('output')
    length = urls[0].split('/').__len__()
    if length >= 6:
        count = 0
        output_dir = "output/"
        for part in urls[0].split('/'):
            if count == 2:
                output_dir = output_dir + part.split('.')[1]
            elif count == 3:
                output_dir = output_dir + '_' + part
            elif count == 4:
                output_dir = output_dir + '_' + part
            
            count += 1
        output_dir = output_dir + '_pdf'
    else:
        output_dir = f"output/{urls[0].split('/')[2].split('.')[1]}_{urls[0].split('/')[3]}_pdf"
    
    
    try:
        for content in list_of_contents:
            if content == output_dir.split('/')[1]:
                print('Directory already exists')
                exist = True
            else:
                exist = False
        
        if exist == False:
            os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory: {e}")
        return
    # Loop through each URL and scrape it
    i = 0
    for url in urls:
        page_url = url.strip()  # Remove any leading/trailing whitespaces
        if page_url:  # Ensure the line is not empty
            i += 1
            scrape_to_pdf(page_url, output_dir, i)
    
    print(f"\nScraped {i} pages to {output_dir}")



if __name__ == "__main__":
    # Replace 'urls.txt' with the path to your file containing the URLs
    scrape_course_from_array(['https://www.w3schools.com/css/default.asp', 'https://www.w3schools.com/css/default.asp']) # test with array