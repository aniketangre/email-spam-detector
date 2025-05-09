#!/usr/bin/env python
# coding: utf-8

# In[9]:


import joblib
import sys


# In[10]:


def load_model():
    model = joblib.load('spam_detector_model.pkl')
    vectorizor = joblib.load('spam_detector_vectorizor.pkl')
    return model, vectorizor


# In[11]:


def predict(text):
    model, vectorizor = load_model()
    text_transformed = vectorizor.transform([text])
    prediction = model.predict(text_transformed)
    return "spam" if prediction[0] == 1 else "Not Spam"


# In[13]:


if __name__ == "__main__":
    text = sys.argv[1] #"Hello world!"
    prediction = predict(text)
    print(f"The message is: {prediction}")


# In[ ]:




