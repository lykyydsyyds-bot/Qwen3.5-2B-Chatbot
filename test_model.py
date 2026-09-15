"""
Test suite for Qwen3.5-2B local model.
Tests: accuracy, performance, and memory usage.
"""

import pytest
import time
import psutil
import os
from llama_cpp import Llama

# -------------------- Fixture: load model once --------------------
@pytest.fixture(scope="session")
def llm():
    """Load the Qwen model once for all tests."""
    print("\n🚀 [Setup] Loading Qwen model for testing...")
    model = Llama(
        model_path="./Qwen3.5-2B-Q4_K_M.gguf",
        n_ctx=512,          # Smaller context for faster testing
        n_threads=4,
        verbose=False
    )
    yield model
    print("\n🧹 [Teardown] Tests finished, model unloaded.")

# -------------------- Test 1: Accuracy (capital of China) --------------------
def test_accuracy_capital(llm):
    """
    Verify the model knows the capital of China.
    Expected answer can be either 'Beijing' or '北京'.
    """
    prompt = (
        "What is the capital of China? Please answer only the city name. "
        "Do not show any reasoning or extra text."
    )
    output = llm(prompt, max_tokens=200, temperature=0)  # 增加到 200，确保输出完整
    response = output["choices"][0]["text"].strip()

    # Assertion: response must contain "Beijing" or "北京"
    assert "Beijing" in response or "北京" in response, (
        f"❌ Accuracy test failed! Expected 'Beijing' or '北京', got: {response[:100]}..."
    )
    print(f"✅ Accuracy test passed! Model answered: {response}")
# -------------------- Test 2: Performance (latency) --------------------
def test_performance_simple(llm):
    """Test the response speed for a simple greeting."""
    prompt = "Please simply say 'hello'."
    start_time = time.time()

    output = llm(prompt, max_tokens=10, temperature=0)
    duration = time.time() - start_time
    response = output["choices"][0]["text"].strip()

    # Assertion: response time must be under 30 seconds (reasonable for local CPU)
    assert duration < 30, (
        f"❌ Performance test failed! Took {duration:.2f} seconds, exceeded threshold."
    )
    print(f"✅ Performance test passed! Time taken: {duration:.2f} seconds")
    print(f"   Model reply: {response}")

# -------------------- Test 3: Memory usage (bonus) --------------------
def test_memory_usage():
    """Check the memory usage of the current Python process."""
    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / 1024 / 1024  # Convert to MB

    print(f"💾 Current memory usage: {memory_mb:.2f} MB")

    # Warning if memory exceeds 3 GB (unexpected for a 2B quantized model)
    if memory_mb > 3000:
        pytest.fail(f"⚠️ Memory usage abnormally high: {memory_mb:.2f} MB")
    else:
        print("✅ Memory usage is within a reasonable range.")