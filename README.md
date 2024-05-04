
# Question and Answer System based on Google's Gemini LLM and Langchain

This project presents a complete end-to-end Question Answering system powered by Large Language Models. Used Google's Gemini language model (LLM) and Langchain. 

To ensure a user-friendly experience, a web interface was built using Streamlit. This interface allows users to interact with the system by posing questions and receiving relevant answers.

![gemini-qa](https://github.com/notayush000/QA-using-LLM/assets/58353326/c12f80a0-26f2-4b3f-b4cc-07a5b9e7fce6)


## Features

- The system intelligently searches for answers within a pre-defined FAQ database (faq.csv) and provides relevant responses.
- Can be used by users to obtain answers quickly.

## Acknowledgements

 - [Codebasics LLM Tutorial](https://youtu.be/AjQPRomyd-k?si=u0R2m0pYe4Z53xY_)


## Installation

1. Clone this repository 
```bash
  https://github.com/notayush000/QA-using-LLM.git
```

2. Generate an API_KEY [[Google AI Studio]](https://aistudio.google.com/app/apikey)
    - Click on Get API Key then click Create API Key 
    - Select any existing project or else create new
    - Finally click Create API Key

3. Put the api key in `langchain_helper.py`
```python
API_KEY = "YOUR_API_KEY"
```
## Usage

1. Rum the Streamlit app
```python
streamlit run main.py
```

