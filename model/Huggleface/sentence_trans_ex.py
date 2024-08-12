# SBERT이용한 것
# step1
from sentence_transformers import SentenceTransformer

# step2: 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# step3: The sentences to encode
# sentences1 = "집에 가고싶다!"
# sentences2 = "맛있는 음식이 집에 있다."
# # sentences = [
#     "The weather is lovely today.",
#     "It's so sunny outside!",
#     "He drove to the stadium.",
# ]
query_embedding = model.encode("How big is London")
passage_embeddings = model.encode(
    [
        "London is known for its finacial district",
        "London has 9,787,426 inhabitants at the 2011 census",
        "The United Kingdom is the fourth largest exporter of goods in the world",
    ]
)

# step4: 추론: 2. Calculate embeddings by calling model.encode()
# embeddings1 = model.encode(sentences1)
# embeddings2 = model.encode(sentences2)
# print(embeddings1.shape)
# print(embeddings2.shape)
# [3, 384]

# 유사한 값 출력: 3. Calculate the embedding similarities
similarities = model.similarity(query_embedding, passage_embeddings)
print(similarities)
# tensor([[1.0000, 0.6660, 0.1046],
#         [0.6660, 1.0000, 0.1411],
#         [0.1046, 0.1411, 1.0000]])
