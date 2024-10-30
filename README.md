# Liguistic_Relativity_Chatgpt
This repo contains codes for experiementing linguistic relativity of various language specific prompts asked to and responded back from ChatGPT 4 mini

# Objective
To experiment "Linguistic Relativity" with ChatGPT

# Code
Run python code 'liguistic_relativity_code.py'

# Output
An excel sheet named 'chatgpt_multilingual_responses_linguistic_relativity.xlsx'

# Modification of 'chatgpt_multilingual_responses_linguistic_relativity.xlsx'
Then, do modification on the 'chatgpt_multilingual_responses_linguistic_relativity.xlsx' file.

During the modifications, we remove colom (') symbol from the prompt and responses as saved by the python code in the above excel sheet. It is done to minimze special symbol specific biasness by the analysis code.

Finally we rename the file as 'modified_results'

# Analysis

We perform two major types of analysis as below.

1. Semantic Similarity among responses accross the languages by using 'paraphrase-multilingual-MiniLM-L12-v2' senstence transformer
   
2. Perform Polarity comparison accorss the responses of the languaes by using 'polyglot' package. This analysis generates a new excel sheet called 'polyglot_sentiment_analysis_results.xlsx' that has three sheets namly 'Average_Polarity_Scores', 'Positivity_Ratios', and 'Negativity_Ratios'. Screen shots are given below for each sheet.

![image](https://github.com/user-attachments/assets/8b9ca32e-7c37-4b75-b4ee-9a52afd36b7a)


![image](https://github.com/user-attachments/assets/e813ab24-8459-4ba8-be32-7b227695bb7d)

![image](https://github.com/user-attachments/assets/dce823e8-2b14-46c1-b448-c9104e4985d8)

