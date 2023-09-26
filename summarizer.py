from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ The Amazon rainforest , also known as the Amazon jungle , is the world 's largest tropical rainforest .
It spans over nine countries in South America and covers approximately 5.5 million square kilometers .
The Amazon is home to a staggering variety of wildlife , including jaguars , sloths , and colorful macaw parrots .
The rainforest plays a crucial role in regulating the Earth 's climate by absorbing carbon dioxide and releasing oxygen .      
It is often referred to as the `` lungs of the Earth . ''
However , the Amazon faces significant threats from deforestation , primarily driven by agriculture and logging .
Efforts are underway to protect and preserve the Amazon rainforest through conservation initiatives and sustainable practices .These efforts are essential to maintain the biodiversity of this remarkable ecosystem and mitigate the impacts of climate change .
TextRazor 's summarization capabilities can help extract key information from articles and documents related to the Amazon rainforest and its conservation .
"""
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))