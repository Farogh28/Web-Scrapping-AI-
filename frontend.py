# import streamlit as st
# import requests

# st.title("AI Data Formatter")

# input_type = st.radio("Input Type", ["Website URL", "Keyword"])
# input_data = st.text_input("Enter your input:")
# file_format = st.selectbox("Select output format:", ["CSV", "JSON", "PDF", "TXT"])

# if st.button("Process"):
#     payload = {
#         "input": input_data,
#         "format": file_format.lower()
#     }
#     try:
#         response = requests.post("http://192.168.29.152:5000/process", json=payload)
#         if response.status_code == 200:
#             st.download_button("Download File", response.content, file_name=f"output.{file_format.lower()}")
#         else:
#             st.error(f"Error: {response.status_code} - {response.text}")
#     except requests.exceptions.ConnectionError:
#         st.error("Failed to connect to the backend. Ensure the Flask server is running.")



# -----------------------------------------------------------------------------------------------------------------------------



import streamlit as st
import requests

st.title("AI Data Formatter")

# User Input Section
input_type = st.radio("Input Type", ["Website URL", "Keyword"])
input_data = st.text_input("Enter your input:")
file_format = st.selectbox("Select output format:", ["CSV", "JSON", "PDF", "TXT"])

# Process Button Logic
if st.button("Process"):
    if input_data.strip() == "":  # Validate input
        st.error("Please enter a valid URL or keyword.")
    else:
        payload = {
            "input": input_data,
            "format": file_format.lower()
        }

        with st.spinner("Processing your request..."):
            try:
                # Send the request to Flask backend
                response = requests.post("http://192.168.29.152:5000/process", json=payload)
                if response.status_code == 200:
                    # Provide download option
                    st.download_button("Download File", response.content, file_name=f"output.{file_format.lower()}")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Failed to connect to the backend. Ensure the Flask server is running.")
