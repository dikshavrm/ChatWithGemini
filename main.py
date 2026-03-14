
from fastapi import FastAPI
from google import genai

app = FastAPI()  # <-- must exist at module top level with this exact name

client = genai.Client(api_key="AIzaSyBLAJQjUdII3lCu8rVayPPq7K7F-FkihIk")

@app.get("/")
def read_root():
    return {"hello": "world"}

text_posts= {}

@app.get("/posts")
def get_all_posts():
    return text_posts

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Name 5 pet animals",
)

@app.get("/chat")
def chat():
    return response.text

# print(response.text)
