import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


class PythonPredictor:
    def __init__(self, config):
        self.device = "cpu"
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2").to(self.device)

    def predict(self, payload):
        input_length = len(payload["text"].split())
        tokens = self.tokenizer.encode(payload["text"], return_tensors="pt").to(self.device)
        prediction = self.model.generate(tokens, max_length=input_length + payload["predictor_length"], do_sample=True)
        return self.tokenizer.decode(prediction[0])


'''predictor = PythonPredictor(True)

sample = """When then, someone was knocking on the door. Who is it? """

print(predictor.predict({"text":sample,"predictor_length":20}))'''
