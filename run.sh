source venv/bin/activate
# gets input from the user
echo "Enter the URL of the w3school course you want to scrape"
read url

echo "running main.py"
python w3_school_scraper.py $url