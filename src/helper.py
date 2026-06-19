import fitz # PyMuPDF
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)

def extract_text_from_pdf(uploaded_file):

    """
    Extract text from pdf file.

    Args:
       uploaded_file(str) : the path to the pdf file.

    Return:
       str: the extracted text.
    """

    text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        text+= page.get_text()
    return text;

def ask_openai(prompt, max_token=500):
    """
    send a prompt to the openAI API and returns the response.

    Args:
        prompt(str) : the prompt to send to the openAI api.
    
    Returns : 
        str: the response from openAI API.
    """

    response = client.chat.completions.create(
        model= "gpt-4o",
        messages=[
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_token
    )

    return response.choices[0].message.content
 



