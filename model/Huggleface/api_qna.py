# step1 : inference 다운
from transformers import pipeline
from fastapi import FastAPI, Form

# step 2
question_answerer = pipeline("question-answering", model="stevhliu/my_awesome_qa_model")
app = FastAPI()


# text를 주고 받을 수 있는 껍데기
@app.post("/question_answerer/")
async def login(question: str = Form(), context: str = Form()):
    # STEP 3: text 서버에서 입력
    # step 4:
    result = question_answerer(question=question, context=context)
    return {"result": result}
