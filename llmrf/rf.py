import time
import json
import uuid

class RF:
    def __init__(self):
        self.default_id = f"chatcmpl-{str(uuid.uuid4())}"
        self.default_model = "gpt-3.5-turbo"
        
    def f_r(self, content, stream=False, **kwargs):
        id = kwargs.get('id', self.default_id)
        model = kwargs.get('model', self.default_model)
        created = kwargs.get('created', int(time.time()))
        
        return self._stream(content, model) if stream else self._normal(content, id, model, created)
    
    def _normal(self, content, id, model, created):
        return {
            "id": id,
            "object": "chat.completion",
            "created": created,
            "model": model,
            "choices": [{
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": content
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "prompt_tokens": len(content),
                "completion_tokens": len(content),
                "total_tokens": len(content) * 2
            }
        }
    
    def _stream(self, content, model):
        chunk = {
            "id": None,
            "object": "chat.completion.chunk",
            "created": None,
            "model": model,
            "choices": [{
                "index": 0,
                "delta": {
                    "content": content,
                    "role": None
                },
                "finish_reason": None
            }],
            "usage": None
        }
        return f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n"
