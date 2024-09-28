# w3_school_scraper

This tool is used to scrape courses from [w3schools](https://www.w3schools.com/) and save each page as a pdf file.

## Installation

Use the `setup.sh` script to install the required packages.
```bash
git clone https://github.com/Moineau54/w3_school_scraper.git
cd w3_school_scraper
./setup.sh
```

## Usage

```bash
python3 w3_school_scraper.py <url>
```

or use the `run.sh` script
 ```bash
./run.sh
```

## Example

```bash
python3 w3_school_scraper.py https://www.w3schools.com/python/default.asp
```

## Requirements

- Python (3.11+)
- wkhtmltopdf
- requests
- beautifulsoup4
- pdfkit
- lxml

