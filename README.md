# 🤖 GPT-Powered Web Scraper

A smart web scraper that combines the power of OpenAI's GPT with Selenium to extract structured data from websites and save it to CSV files.

## ✨ Features

- 🧠 Uses GPT to intelligently extract data from web pages
- 🌐 Handles JavaScript-rendered content with Selenium
- 📊 Exports data to CSV format
- 🛠 Automatic Chrome WebDriver management
- 🧹 Clean HTML content processing
- 🔄 Supports multiple URLs

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Chrome browser installed
- OpenAI API key

### Installation

1. Clone this repository:

bash 
git clone https://github.com/yourusername/gpt-web-scraper.git
cd gpt-web-scraper


2. Install required packages:

bash
pip install -r requirements.txt

3. Create a `.env` file in the project root and add your OpenAI API key:

env
OPENAI_API_KEY=your_openai_api_key_here

## 🎯 Usage

1. Open `web_scraper.py` and modify the `urls` list with the websites you want to scrape:

python
urls = [
    "https://example.com/page1",
    "https://example.com/page2"
]

2. Customize the `elements_to_extract` list with the data points you want to extract:
ython
elements_to_extract = [
    "title",
    "price",
    "description",
    "rating"
]

3. Run the script:

bash
python web_scraper.py


The script will:
- Visit each URL
- Extract the content
- Use GPT to analyze and structure the data
- Save all extracted data to `scraped_data.csv`

## 📝 Example Output

The script will create a CSV file with columns matching your `elements_to_extract` list. For example:

| title | price | description | rating |
|-------|-------|-------------|--------|
| Product A | $19.99 | Amazing product... | 4.5 |
| Product B | $29.99 | Great features... | 4.8 |

## ⚙️ Customization

You can modify the GPT prompt in the `scrape_website` method to improve extraction accuracy:

python
messages=[
    {"role": "system", "content": "You are a data extraction assistant..."},
    {"role": "user", "content": f"Extract the following elements..."}
]

## ⚠️ Important Notes

- Respect websites' `robots.txt` files and terms of service
- Be mindful of rate limiting and website policies
- The free OpenAI API has usage limits
- Some websites may block automated access

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for the GPT API
- Selenium for web automation
- Beautiful Soup for HTML parsing

## 💡 Tips

- Test the scraper on a small number of URLs first
- Adjust the wait times if pages load slowly
- Consider adding error retry logic for production use
- Use proxy rotation for large-scale scraping