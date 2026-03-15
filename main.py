
from fastapi import FastAPI, HTTPException
from google import genai
from app.schemas import PostCreate

app = FastAPI()  # <-- must exist at module top level with this exact name

client = genai.Client(api_key="YOUR_API_KEY")

@app.get("/")
def read_root():
    return {"hello": "world"}

text_posts= {
    1:  {"title":"Artificial", "content":"Intelligence"}
}

@app.get("/posts")
def get_all_posts():
    return text_posts

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="High protein rich vegeterian foods",
)

@app.get("/chat")
def chat():
    return response.text

# print(response.text)

@app.get("/chat/{id}")
def chat_with_id():
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Chat not found")
    return text_posts.get(id)

@app.post("/chat")
def post_chat(post: PostCreate):
    new_chat = {"title":"hello", "content":"World"}
    text_posts[max(text_posts.keys()) + 1] = new_chat
    return new_chat


# GEMINI POST METHOD
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Badminton rules",
)

@app.post("/chat-with-gemini")
def post_chat(post: PostCreate):
    new_chat = {"title":"hello", "content":"World"}
    return response.text
