# from flask import Flask, request, send_file, jsonify
# import pandas as pd
# import json
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import io

# app = Flask(__name__)

# # Root endpoint
# @app.route('/')
# def home():
#     return "Flask backend is running!"

# # Process endpoint
# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json
#     input_text = data['input']
#     file_format = data['format']

#     # Process data with LLM (pseudo-code)
#     processed_data = {"summary": "This is a sample summary."}

#     # Format data
#     if file_format == 'csv':
#         df = pd.DataFrame(processed_data)
#         output = df.to_csv(index=False)
#         filename = 'output.csv'
#     elif file_format == 'json':
#         output = json.dumps(processed_data, indent=4)
#         filename = 'output.json'
#     elif file_format == 'pdf':
#         buffer = io.BytesIO()
#         p = canvas.Canvas(buffer, pagesize=letter)
#         p.drawString(100, 750, str(processed_data))
#         p.save()
#         buffer.seek(0)
#         return send_file(buffer, as_attachment=True, download_name='output.pdf')
#     elif file_format == 'txt':
#         output = str(processed_data)
#         filename = 'output.txt'

#     return send_file(io.BytesIO(output.encode()), as_attachment=True, download_name=filename)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



# --------------------------------  Updated


# from flask import Flask, request, send_file, jsonify
# import pandas as pd
# import json
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import io

# app = Flask(__name__)

# # Root endpoint
# @app.route('/')
# def home():
#     return "Flask backend is running!"

# # Process endpoint
# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json
#     input_text = data['input']
#     file_format = data['format']

#     # Process data with LLM (pseudo-code)
#     processed_data = {"summary": "This is a sample summary."}

#     # Format data
#     if file_format == 'csv':
#         df = pd.DataFrame(processed_data, index=[0])  # Add an index
#         output = df.to_csv(index=False)
#         filename = 'output.csv'
#     elif file_format == 'json':
#         output = json.dumps(processed_data, indent=4)
#         filename = 'output.json'
#     elif file_format == 'pdf':
#         buffer = io.BytesIO()
#         p = canvas.Canvas(buffer, pagesize=letter)
#         p.drawString(100, 750, str(processed_data))
#         p.save()
#         buffer.seek(0)
#         return send_file(buffer, as_attachment=True, download_name='output.pdf')
#     elif file_format == 'txt':
#         output = str(processed_data)
#         filename = 'output.txt'

#     return send_file(io.BytesIO(output.encode()), as_attachment=True, download_name=filename)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


# ------------------------------------------------------------------------------------------------------------



# from flask import Flask, request, send_file, jsonify
# import pandas as pd
# import json
# import requests
# from bs4 import BeautifulSoup
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import io
# import openai  # For LLM processing

# from api_key import openai_api_key


# app = Flask(__name__)

# # Set your OpenAI API key
# openai.api_key = openai_api_key

# # Root endpoint
# @app.route('/')
# def home():
#     return "Flask backend is running!"

# # Function to scrape data from a website
# def scrape_website(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     paragraphs = soup.find_all("p")
#     text = " ".join([p.get_text() for p in paragraphs])  # Extract text from paragraphs
#     return text

# # Function to fetch relevant data using a keyword (Pseudo search function)
# def search_keyword(keyword):
#     search_url = f"https://en.wikipedia.org/wiki/{keyword}"  # Example: Wikipedia search
#     return scrape_website(search_url)

# # Function to process text with LLM (GPT)
# def process_text_with_llm(text):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "system", "content": "Summarize the following content:"},
#                   {"role": "user", "content": text}]
#     )
#     return response["choices"][0]["message"]["content"]

# # Process endpoint
# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json
#     input_value = data['input']
#     file_format = data['format']
    
#     # Determine if input is a website URL or keyword
#     if input_value.startswith("http"):
#         raw_text = scrape_website(input_value)
#     else:
#         raw_text = search_keyword(input_value)

#     # Process the extracted text with LLM
#     processed_data = {"summary": process_text_with_llm(raw_text)}

#     # Format and return the data
#     if file_format == 'csv':
#         df = pd.DataFrame([processed_data])  # Convert to DataFrame
#         output = df.to_csv(index=False)
#         filename = 'output.csv'
#     elif file_format == 'json':
#         output = json.dumps(processed_data, indent=4)
#         filename = 'output.json'
#     elif file_format == 'pdf':
#         buffer = io.BytesIO()
#         p = canvas.Canvas(buffer, pagesize=letter)
#         p.drawString(100, 750, str(processed_data))
#         p.save()
#         buffer.seek(0)
#         return send_file(buffer, as_attachment=True, download_name='output.pdf')
#     elif file_format == 'txt':
#         output = str(processed_data)
#         filename = 'output.txt'
    
#     return send_file(io.BytesIO(output.encode()), as_attachment=True, download_name=filename)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


# ------------------------------------------------------------------------------------------------------------------------------------------------


from flask import Flask, request, send_file, jsonify
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import openai  # For LLM processing

# Import the OpenAI API key from api_key.py
from api_key import gemini_api_key

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = gemini_api_key  # Use the imported variable

# Root endpoint
@app.route('/')
def home():
    return "Flask backend is running!"

# Function to scrape data from a website
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])  # Extract text from paragraphs
        return text
    except requests.exceptions.RequestException as e:
        return f"Error scraping website: {str(e)}"

# Function to fetch relevant data using a keyword (Pseudo search function)
def search_keyword(keyword):
    search_url = f"https://en.wikipedia.org/wiki/{keyword}"  # Example: Wikipedia search
    return scrape_website(search_url)

# Function to process text with LLM (GPT)
def process_text_with_llm(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Summarize the following content:"},
                {"role": "user", "content": text}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.AuthenticationError:
        return "Error: Invalid OpenAI API key. Please check your API key."
    except openai.error.RateLimitError:
        return "Error: Rate limit exceeded. Please try again later."
    except Exception as e:
        return f"Error processing text with LLM: {str(e)}"

# Process endpoint
@app.route('/process', methods=['POST'])
def process():
    data = request.json
    input_value = data['input']
    file_format = data['format']
    
    # Determine if input is a website URL or keyword
    if input_value.startswith("http"):
        raw_text = scrape_website(input_value)
    else:
        raw_text = search_keyword(input_value)

    # Process the extracted text with LLM
    processed_data = {"summary": process_text_with_llm(raw_text)}

    # Format and return the data
    if file_format == 'csv':
        df = pd.DataFrame([processed_data])  # Convert to DataFrame
        output = df.to_csv(index=False)
        filename = 'output.csv'
    elif file_format == 'json':
        output = json.dumps(processed_data, indent=4)
        filename = 'output.json'
    elif file_format == 'pdf':
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, str(processed_data))
        p.save()
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name='output.pdf')
    elif file_format == 'txt':
        output = str(processed_data)
        filename = 'output.txt'
    
    return send_file(io.BytesIO(output.encode()), as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)