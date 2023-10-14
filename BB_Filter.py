import re

class BB_Filter():
    def __init__(self, data: list[dict]):
        self.data = data
        if data is None:
            raise ValueError("Data must be provided")
        if not isinstance(self.data, list):
            raise TypeError("Data must be a list")
        if not all(isinstance(item, dict) for item in self.data):
            raise TypeError("Data must be a list of dictionaries")

        self.patterns = [
        (r'\n+', '\n'),     # Replace more than one consecutive newlines with a single newline
        (r'\t+', '\t'),     # Replace consecutive tabs with a single tab
        (r' +', ' '),       # Replace consecutive spaces with a single space
        ]
        self.invalid_keywords = ['youtube', 'instagram', 'facebook', 'twitter', 'fyp365', 'title2', 'sacscoc', 'google', 'secure', 'nam04']
        self.invalid_contents = ['Page Not Found']

    def clean_page_content(self) -> list[dict]:
        """
        Cleans the 'page_content' text in the provided data if contains too many \n, \t, or spaces.
        """
        for item in self.data[:]:
            for pattern, replacement in self.patterns:
                item['page_content'] = (re.sub(pattern, replacement, item['page_content'])).strip()

        return self.data
    
    def delete_data_if_not_contain_usf(self) -> list[dict]:
        """
        Delete data if the source does not contain usf before the third slash
        """
        for item in self.data[:]:
            if 'usf' not in item['metadata']['source'].split('/')[2]:
                self.data.remove(item)

        return self.data
    
    def delete_data_if_page_not_found(self) -> list[dict]:
        """
        Delete data if the page content contains invalid words
        """
        self.invalid_contents = [invalid_content.strip().lower() for invalid_content in self.invalid_contents]
        for item in self.data[:]:
            if any(keyword in item['page_content'].strip().lower() for keyword in self.invalid_contents):
                self.data.remove(item)

        return self.data
    
    def filter_sources_on_keywords(self) -> list[dict]:
        """
        Delete data if the source contains any of the invalid keywords
        """
        for item in self.data[:]:
            if any(keyword in item['metadata']['source'] for keyword in self.invalid_keywords):
                self.data.remove(item)

        return self.data
    
    def format_title(self) -> list[dict]:
        """
        Format the title of of some items in the data
        """
        for item in self.data:
            if "title" in item['metadata'] and "::" in item['metadata']['title']:
                item['metadata']['title'] = item['metadata']['title'].replace("::", "|")

        return self.data
    
    def filter(self) -> list[dict]:
        self.clean_page_content()
        self.delete_data_if_not_contain_usf()
        self.delete_data_if_page_not_found()
        self.filter_sources_on_keywords()
        self.format_title()
        return self.data