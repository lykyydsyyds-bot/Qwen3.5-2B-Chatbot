import pytest
from utils import clean_response, preprocess_prompt

def test_clean_response_removes_think():
    """测试后处理：必须移除 <think> 标签"""
    raw = "<think>\nThinking Process...\n</think>\nBeijing"
    assert clean_response(raw) == "Beijing"

def test_clean_response_removes_extra_whitespace():
    """测试后处理：必须移除首尾空格和换行"""
    raw = "\n   Hello World   \n"
    assert clean_response(raw) == "Hello World"

def test_clean_response_keeps_normal_text():
    """测试后处理：正常文本不受影响"""
    raw = "Paris is the capital."
    assert clean_response(raw) == "Paris is the capital."

def test_preprocess_prompt_truncates_long_input():
    long_text = "a" * 600
    result = preprocess_prompt(long_text)
    suffix = "...(已截断)"
    expected_len = 500 + len(suffix)  # 500 + 8 = 508
    assert len(result) == expected_len, f"Expected length {expected_len}, got {len(result)}"
    assert result.endswith(suffix), f"Result should end with '{suffix}'"

def test_preprocess_prompt_keeps_short_input():
    """测试预处理：正常输入保持不变"""
    short_text = "Hello"
    assert preprocess_prompt(short_text) == "Hello"