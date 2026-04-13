from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from omegaconf import OmegaConf
from transformers import AutoTokenizer, AutoModelForCausalLM

class ModernVietnameseAI:
    def __init__(self, config_path):
        self.config = OmegaConf.load(config_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(self.config.model_path)

    def __call__(self, prompt_text):
        messages = [
            {"role": "system", "content": "Bạn là một chuyên gia IT thông minh. Hãy trả lời câu hỏi của người dùng một cách ngắn gọn, súc tích và logic bằng tiếng Việt."},
            {"role": "user", "content": prompt_text}
        ]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer([text], return_tensors="pt")

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=150,
                temperature=0.7
            )
        
        generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, outputs)]
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return response

chatbot = ModernVietnameseAI("./config.yaml")

app = FastAPI()

class TextRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "Hệ thống API Trợ lý ảo AI. Sinh viên thực hiện: Trịnh Văn Hợp."}

@app.get("/health")
async def health():
    return {"status": "ok", "model": "Qwen2.5-0.5B-Instruct"}

@app.post("/generate")
async def generate(data: TextRequest):
    if not data.prompt or data.prompt.strip() == "":
        raise HTTPException(status_code=400, detail="Vui lòng đặt câu hỏi.")
    try:
        answer = chatbot(data.prompt)
        return {
            "question": data.prompt,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))