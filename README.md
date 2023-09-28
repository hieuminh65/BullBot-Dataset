# BullBot-Dataset
The repository contains dataset of Bull Bot from 5000+ websites and links of the University of South Florida

### Checkout Bull Bot in action at **[BullBot.tech](https://www.bullbot.tech)**

## About the main files in the repository: main.ipynb and data_webScrap.ipynb
1. The program in [main.ipynb](main.ipynb) file scrapes the links from the websites stored them in the form of a pickle file [urls.pkl](urls.pkl).
2. After that, the program in [data_webScrap.ipynb](data_webScrap.ipynb) file scrapes the page contents from the links stored in the pickle file and stores them in the form of a json file [data.json](dataset.json).

## About the dataset
The dataset is a json file [data.json](dataset.json). In another words, it is a list of python dictionary with the following structure:
```python
[{
  "page_content": {
    "page_content of the pages.....",
    "metadata": {
      "source": "url of the page",
      "title": "title of the page"
        }
    },
  {
    "page_content": {
        "About USF. See .... "
        }
    "metadata": {
        "source": "https://www.usf.edu/about-usf/index.aspx",
        "title": "About USF | University of South Florida"
        }
    },  
  ...
}
]
```

## Data Analyst Notes
- Data Analyst only need to look at the [data.json](data.json) file.
- Data Analyst can use the example.ipynb file to get started with the dataset. However, it is just an example to start. 

**Tasks:**
- [ ] Remove and filter unrelevant data from the dataset. The data which is considered unrelevant when it is not related to the USF and contains unnecessary information.
- [ ] Clean the data. The current data contain a lo of new line characters (\n). They should be removed or cut off.
- [ ] Develop a python program to clean data, and filter out the unrelevant data. The program should be able to automatically clean the data and filter out the unrelevant data when the new data is added to the dataset. 
