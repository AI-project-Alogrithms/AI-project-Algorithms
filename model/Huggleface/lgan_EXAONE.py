import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct")

# Choose your prompt
prompt = "Explain who you are"  # English example
prompt = "너의 소원을 말해봐"  # Korean example

messages = [
    {
        "role": "system",
        "content": "You are EXAONE model from LG AI Research, a helpful assistant.",
    },
    {"role": "user", "content": prompt},
]
input_ids = tokenizer.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
)

output = model.generate(
    input_ids.to("cuda"), eos_token_id=tokenizer.eos_token_id, max_new_tokens=128
)
print("output: ", tokenizer.decode(output[0]))
