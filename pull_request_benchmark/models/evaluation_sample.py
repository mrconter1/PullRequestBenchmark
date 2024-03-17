import requests
from bs4 import BeautifulSoup

class EvaluationSample:
    def __init__(self, pr_url):
        self.pr_url = pr_url
        self.pr_title = self.extract_pr_title(pr_url)
        print(self.pr_title)
        
    def extract_pr_title(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('bdi', class_='js-issue-title markdown-title')
        return title_tag.text.strip() if title_tag else 'Title not found'
        
    def get_pr_type():
        return "lol"
    
    def get_pr_title():
        return "lol"    
    
    def get_pr_description():
        return "lol"  
    
    def get_pr_diff():
        return "lol"    
        
    def get_pr_outcome():
        return "rejected"