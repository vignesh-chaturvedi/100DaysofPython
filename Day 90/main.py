import os
import pytesseract
from pdf2image import convert_from_path
from gtts import gTTS

# Path to the PDF file to convert
pdf_path = "example.pdf"

# Convert the PDF file to a list of PIL images
pages = convert_from_path(pdf_path, dpi=200)

# Initialize an empty string to store the extracted text
text = ""

# Loop over each page and extract the text using OCR
for page in pages:
    text += pytesseract.image_to_string(page)

# Use the gTTS library to convert the text to speech using Google's TTS API
tts = gTTS(text=text, lang='en')

# Save the audio file as an MP3 file
tts.save("audio.mp3")

# Play the audio file using the default media player
os.system("start audio.mp3")
