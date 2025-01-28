from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import openai
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

class GPTWebScraper:
    def __init__(self):
        # Initialize Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def scrape_website(self, url, elements_to_extract):
        """
        Scrape website and extract specified elements using GPT
        """
        try:
            # Navigate to URL
            self.driver.get(url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Get page content
            page_content = self.driver.page_source
            soup = BeautifulSoup(page_content, 'html.parser')
            
            # Extract main content and remove script/style tags
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get clean text
            text = soup.get_text()
            
            # Use GPT to extract structured data
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a data extraction assistant. Extract the requested information from the provided text and return it as JSON."},
                    {"role": "user", "content": f"Extract the following elements: {elements_to_extract} from this text: {text[:4000]}"}  # Limit text length
                ]
            )
            
            # Parse the response
            extracted_data = json.loads(response.choices[0].message.content)
            return extracted_data
            
        except Exception as e:
            print(f"Error scraping website: {str(e)}")
            return None
        
    def save_to_csv(self, data, output_file):
        """
        Save extracted data to CSV
        """
        df = pd.DataFrame([data])
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
        
    def close(self):
        """
        Close the browser
        """
        self.driver.quit()

def main():
    # Example usage
    urls = [
        "https://example.com/page1",
        "https://example.com/page2"
    ]
    
    elements_to_extract = [
        "title",
        "price",
        "description",
        "rating"
    ]
    
    scraper = GPTWebScraper()
    all_data = []
    
    for url in urls:
        data = scraper.scrape_website(url, elements_to_extract)
        if data:
            all_data.append(data)
    
    # Save all data to CSV
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv('scraped_data.csv', index=False)
        print("All data saved to scraped_data.csv")
    
    scraper.close()

if __name__ == "__main__":
    main() 