# step1 : inference 다운
from transformers import pipeline

# from transformers import AutoTokenizer
# from transformers import AutoModelForSequenceClassification


# step 2
# model = 유저계정/어떤 모델이냐
# 한국어 모델 language에서 korea 선택 (예시: https://huggingface.co/snunlp/KR-FinBert-SC)
classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")

# 토큰이 없을 때
# tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_model")
# model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model")

# step3
text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might watch it again."
"""
현대바이오, '폴리탁셀' 코로나19 치료 가능성에 19% 급등
"""

# step 4
result = classifier(text)
# inputs = tokenizer(text, return_tensors="pt")
# with torch.no_grad():
#     logits = model(**inputs).logits

# 결과 뽑기
# predicted_class_id = logits.argmax().item()
# result = model.config.id2label[predicted_class_id]
# step 5
print(result)
