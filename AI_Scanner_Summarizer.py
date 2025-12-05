# Import the Azure AI Document Intelligence SDK
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from groq import Groq
import os
from dotenv import load_dotenv
import time

folder_path = r"C:\Users\PC\Documents\Coding Projects\AI-ML\AI Scanner + Summarizer Project\Examples"
folder_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith (".pdf")]

# Set up the endpoint and API key for the Azure Document Intelligence service
load_dotenv()
endpoint =  "https://josiadocai.cognitiveservices.azure.com/"
api_key = os.getenv("AZURE_KEY")
# Create a client to interact with the Document Intelligence service
client = DocumentAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)

groq_client = Groq(api_key=os.getenv("GROQ_KEY"))


# Store and print the extracted text
for file_path in folder_files:
    time.sleep(1) #Adds a delay between requests

    extracted_text = ""
    with open(file_path, "rb") as f: 
        poller = client.begin_analyze_document(
            model_id="prebuilt-layout",
            document=f
    )
    result = poller.result()

    for page in result.pages:
        for line in page.lines:
            extracted_text += line.content + " "

    print (f"\n---- Extracted text for {os.path.basename(file_path)} ----")
    print(extracted_text)

    #Summarization
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Summarize the document clearly, simply and concisely."},
            {"role": "user", "content": f"Summarize this:\n\n{extracted_text}"}
        ]
    )

    summary = response.choices[0].message.content

    print(f"\n---- Summary for {os.path.basename(file_path)} ----")
    print(summary)
