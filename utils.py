import re

def clean_response(text: str) -> str:
    """
    后处理函数：移除模型输出中的 思考标签 和多余空白。
    """
    # 1. 移除 <think>...</think> 标签（包括换行）
    cleaned = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    # 2. 移除首尾空白
    cleaned = cleaned.strip()
    return cleaned

def preprocess_prompt(user_input: str) -> str:
    """
    预处理函数：简单限制输入长度（防止恶意超长输入）。
    """
    max_len = 500
    if len(user_input) > max_len:
        return user_input[:max_len] + "...(已截断)"
    return user_input