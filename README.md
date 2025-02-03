
# LLMRF
[![PyPI version](https://badge.fury.io/py/llmrf.svg)](https://badge.fury.io/py/llmrf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

LLMRF (LLM Response Formatter) 是一个轻量级的 Python 库，用于将 LLM 输出格式化为标准的 OpenAI API 响应格式。

## ✨ 特性
- 🚀 简单易用的 API
- 📦 支持标准和流式响应格式
- 🔧 完全可自定义的参数
- 🎯 兼容 OpenAI API 格式

## 🛠️ 安装
```bash
pip install llmrf
```

## 📖 使用示例
### 基础用法
```python
from llmrf import RF
import json

rf = RF()
# 普通响应
response = rf.f_r("Hello, World!")
print(json.dumps(response, indent=2))  # 格式化输出

# 流式响应
stream = rf.f_r("Hello, World!", stream=True)
print(stream)
```

### 输出示例
普通响应输出：
```json
{
  "id": "chatcmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "chat.completion",
  "created": 1707139200,
  "model": "gpt-3.5-turbo",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello, World!"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 12,
    "total_tokens": 24
  }
}
```

流式响应输出：
```
data: {"id": null, "object": "chat.completion.chunk", "created": null, "model": "gpt-3.5-turbo", "choices": [{"index": 0, "delta": {"content": "Hello, World!", "role": null}, "finish_reason": null}], "usage": null}
```

### 自定义参数
```python
response = rf.f_r(
    content="Hello, World!",
    model="custom-model",
    id="custom-id"
)
```

### 格式化输出提示
为了获得更好的可读性，建议使用 `json.dumps()` 格式化输出：
```python
import json

response = rf.f_r("Hello, World!")
# 使用 indent 参数美化输出
print(json.dumps(response, indent=2, ensure_ascii=False))
```

## 📚 API 文档
### RF.f_r()
主要格式化方法，支持以下参数：
| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| content | str | 是 | - | 要格式化的文本内容 |
| stream | bool | 否 | False | 是否使用流式响应 |
| model | str | 否 | "gpt-3.5-turbo" | 模型名称 |
| id | str | 否 | 自动生成 | 响应 ID |
| created | int | 否 | 当前时间戳 | 创建时间 |

## 🎯 使用场景
- 自定义 LLM 服务接口标准化
- API 响应格式转换
- 流式输出格式化
- LLM 响应模拟测试

## 🤝 贡献
欢迎提交 Pull Requests！对于重大更改，请先开 issue 讨论您想要改变的内容。

## 🔗 相关链接
- [PyPI 项目页面](https://pypi.org/project/llmrf/)
- [问题反馈](https://github.com/cchking/llmrf/issues)
- [更新日志](CHANGELOG.md)
