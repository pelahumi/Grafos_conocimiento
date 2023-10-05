import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]

question = "What team won the 2022 champions league?"
completion = openai.ChatCompletion.create(model="gpt-3.5", 
                                          temperature=0, 
                                          messages=[{"role":"user",
                                                    "content":question,}])

print(completion["choices"][0]["message"]["content"])

