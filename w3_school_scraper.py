from bs4 import BeautifulSoup
import requests
import sys
import pdf_maker


    
                
if __name__ == '__main__':
    """
    Debugging
    """
    try:
        url = sys.argv[1]
    except IndexError:
        print('Please provide a URL')
        print('Usage: python w3_school_scraper.py <URL>')
        sys.exit(1)
        #url = 'https://www.w3schools.com/python/default.asp' # test with single url

    print(url)
    base_url_origin = ''
    count = 0
    lenght = url.split('/').__len__()
    print(lenght)
    for part in url.split('/'):
        #print(part)
        if count == url.split('/').__len__()-1:
            break
        base_url_origin = base_url_origin + part + '/'
        count += 1
    print(base_url_origin)
    #base_url_origin = url.split('/')[0]+'//'+url.split('/')[2]+'/' + url.split('/')[3] + '/'
    time_base_first = 10
    time_base_second = time_base_first + 30
    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    middle = soup.find('div', class_='w3-sidebar w3-collapse')
    if middle != None:
        row = middle.find('div', id='leftmenuinner')
        if row != None:
            next_url = row.find_all('a', target='_top')
            if next_url == None:
                exit()
            else:
                urls = []
                for links in next_url:
                    link = links['href']
                    if link.startswith('/'):
                        url = base_url_origin.split('/')[0]+'//'+base_url_origin.split('/')[2]+link
                    else:
                        url = base_url_origin + link
                    print(url)
                    
                    urls.append(url)
print("\n")

pdf_maker.scrape_course_from_array(urls)