from setuptools import setup, find_packages
import os

# 读取 README.md 的内容
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llmrf",
    version="0.1.1",
    description="轻量级的 LLM 响应格式化工具，支持标准响应和流式响应",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="满天翔",
    author_email="2722843861@qq.com",
    url="https://github.com/cchking/llmrf",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
