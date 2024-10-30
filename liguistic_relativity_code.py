# The objective of this code is to ask prompt and get responses in the same langue for esperimenting "Language Relativity" hypothesis with ChatGPT
#
# This code asks "gpt-4o-mini" 10 prompts in various languages as shown below:
# Hindi 
# Gujarati 
# Marathi 
# Urdu 
# English 
# French 
# Spanish 
# Portuguese 
# German 
# Russian 
# Chinese (Mandarin) 
# Japanese 
# Arabic 

# Partha Pratim Ray
# 20 October, 2024

#!/usr/bin/env python
# coding: utf-8

from openai import OpenAI
import pandas as pd
import time

# Initialize OpenAI client
client = OpenAI(api_key='enter you chatgpt api here')

# Define 10 English prompts for testing (aligned with linguistic relativity)
prompts_english = [
    "Describe what 'home' means to you.",
    "What is your perspective on 'freedom'?",
    "Explain the concept of 'love.'",
    "How would you define 'success' in life?",
    "Describe what 'respect' means to you, especially towards elders.",
    "What does 'happiness' mean to you?",
    "How do you perceive 'nature' and humanity’s relationship with it?",
    "What are your views on 'luck' or 'fate'?",
    "How do you describe the feeling of 'sadness'?",
    "What is your interpretation of 'beauty'?"
]

# Define the languages to translate and get responses in
languages = {
    "English": "English",
    "Hindi": "हिंदी में अनुवाद करें",
    "Gujarati": "ગુજરાતીમાં અનુવાદ કરો",
    "Marathi": "मराठीत भाषांतर करा",
    "Urdu": "اردو میں ترجمہ کریں",
    "French": "Traduisez en français",
    "Spanish": "Traduce al español",
    "Portuguese": "Traduza para o português",
    "German": "Übersetze ins Deutsche",
    "Russian": "Переведите на русский",
    "Chinese": "翻译成中文",
    "Japanese": "日本語に翻訳してください",
    "Arabic": "ترجم إلى العربية"
}

# Function to get a translated prompt and response in the target language
def get_translation_and_response(prompt, target_language):
    try:
        # Translate the prompt into the target language
        translation_prompt = f"Translate the following prompt into {target_language}: '{prompt}'"
        translation_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": translation_prompt}]
        )
        translated_prompt = translation_response.choices[0].message.content

        # Get the response for the translated prompt in the target language
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": translated_prompt}]
        )
        response_text = response.choices[0].message.content

        return translated_prompt, response_text

    except Exception as e:
        print(f"Error with prompt '{prompt}' in {target_language}: {e}")
        return None, None

# Initialize DataFrame with columns for each language's prompt and response
columns = ["Prompt"] + [f"{lang}_Prompt" for lang in languages.keys()] + [f"{lang}_Response" for lang in languages.keys()]
df = pd.DataFrame(columns=columns)

# Loop through each prompt, first getting the English response, then translating and getting responses for each language
for i, prompt in enumerate(prompts_english, start=1):
    row_data = {"Prompt": prompt}

    # Process each language: translate and get response in target language
    for lang in languages.keys():
        translated_prompt, response_text = get_translation_and_response(prompt, languages[lang])
        row_data[f"{lang}_Prompt"] = translated_prompt
        row_data[f"{lang}_Response"] = response_text
        print(f"[Prompt {i}/10] Processed {lang} prompt and response.")

        # Optional: delay to avoid rate limiting
        time.sleep(1)

    # Append row data to the DataFrame
    row_df = pd.DataFrame([row_data])
    df = pd.concat([df, row_df], ignore_index=True)

# Save responses to an Excel file
df.to_excel("chatgpt_multilingual_responses_linguistic_relativity.xlsx", index=False)
print("Responses saved to 'chatgpt_multilingual_responses_linguistic_relativity.xlsx'")


# In[ ]:




