import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBarZkGOiou8V7uXPkZtRuTd0tXwIEKJFU")

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")  # Make sure the model name is correct

# Generate content 
response = model.generate_content("hi how are you")

# Print the response text
print(response.text)
