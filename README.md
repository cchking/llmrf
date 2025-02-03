好的，这是一个更详细的 `README.md`：

````markdown
# LLMRF (LLM Response Formatter)

一个简单的 LLM 响应格式化工具，可以将文本内容格式化为类似 OpenAI API 的响应格式。

## 功能特点

- 支持普通响应和流式响应格式
- 类 OpenAI API 的响应结构
- 简单易用的接口
- 支持自定义模型名称和其他参数

## 安装

```bash
pip install llmrf
```
````

## 基础使用

```python
from llmrf import RF

# 创建格式化器实例
rf = RF()

# 普通响应
response = rf.f_r("你好世界")
# 返回格式示例：
{
    "id": "chatcmpl-xxx",
    "object": "chat.completion",
    "created": 1709544000,
    "model": "gpt-3.5-turbo",
    "choices": [{
        "index": 0,
        "message": {
            "role": "assistant",
            "content": "你好世界"
        },
        "finish_reason": "stop"
    }],
    "usage": {
        "prompt_tokens": 3,
        "completion_tokens": 3,
        "total_tokens": 6
    }
}

# 流式响应
stream = rf.f_r("你好世界", stream=True)
# 返回格式示例：
data: {"id": null, "object": "chat.completion.chunk", ...}
data: [DONE]
```

## 高级用法

可以自定义模型名称和其他参数：

```python
response = rf.f_r(
    content="你好世界",
    stream=False,
    model="custom-model",
    id="custom-id"
)
```

## 参数说明

`rf.f_r()` 方法支持以下参数：

- `content`: (必需) 要格式化的文本内容
- `stream`: (可选) 布尔值，是否使用流式响应格式，默认 False
- `model`: (可选) 模型名称，默认 "gpt-3.5-turbo"
- `id`: (可选) 响应 ID，默认自动生成
- `created`: (可选) 创建时间戳，默认当前时间

## 开源协议

MIT License

## 问题反馈

如果您发现任何问题或有改进建议，欢迎在 GitHub 上提交 issue。

```

这个版本的 README：
1. 增加了功能特点说明
2. 添加了更详细的使用示例
3. 包含了完整的参数说明
4. 添加了响应格式示例
5. 说明了开源协议和问题反馈方式

需要补充或修改什么吗？
```
