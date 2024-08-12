# step1 : inference 다운
from transformers import pipeline
from fastapi import FastAPI, Form

# step 2
summarizer = pipeline("summarization", model="stevhliu/my_awesome_billsum_model")
app = FastAPI()


# text를 주고 받을 수 있는 껍데기
@app.post("/summarizer/")
async def login(text: str = Form()):
    # STEP 3: text 서버에서 입력
    # step 4:
    result = summarizer(text)
    return {"result": result}
