# Experimental Results and Analysis (RESULTS)

## 1. Model Performance Data
- **Model parameters**: 1.88 Billion (Q4_K_M quantization)
- **Average inference speed**: ~19–20 tokens/sec (local CPU environment)
- **Memory usage**: ~1.2 GB (after loading)
- **Context length**: 2048 tokens (adjustable based on hardware)

## 2. Qualitative Analysis
- **Strengths**: The model answers Chinese common-sense questions accurately (e.g., "the capital of China", "the location of Macao Polytechnic University") and demonstrates basic logical reasoning ability.
- **Weaknesses**: Under English prompts, it enables "thinking mode" by default (outputting `<think>` tags), which requires post-processing cleanup; generation speed drops noticeably for very long contexts (e.g., 16384 tokens).

## 3. Challenges Encountered and Solutions
### Challenge 1: Asynchronous Conflict Between LangChain and Streamlit
- **Problem**: When using `langchain_community.llms.LlamaCpp`, Streamlit threw a `ConnectionResetError`, and the model's response was interrupted.
- **Solution**: Abandoned the LangChain wrapper and switched to the native `llama_cpp.Llama` library for direct calls, avoiding event-loop blocking and improving stability.

### Challenge 2: Compilation Failure in Python 3.13 Environment
- **Problem**: Installing `llama-cpp-python` on Windows failed during source compilation due to the missing C++ compiler.
- **Solution**: Installed using a precompiled wheel: `pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu`.

### Challenge 3: Model Outputting Thinking Tags During Testing
- **Problem**: In the accuracy test, the model failed to provide an answer within the token limit because it output a `<think>` reasoning process.
- **Solution**: Increased `max_tokens` to 200 and wrote a `clean_response` post-processing function to strip the tags, ensuring clean output.

## 4. Unit Test Coverage
- **Post-processing test**: Verifies that `clean_response` correctly removes `<think>` tags and leading/trailing whitespace.
- **Pre-processing test**: Verifies that `preprocess_prompt` correctly truncates overly long input (over 500 characters).
- **Model tests**: Covers accuracy (Beijing/capital), response latency (< 30 seconds), and memory usage (< 3 GB).

## 5. Conclusion
This project successfully deployed a 2B-parameter quantized large language model on an ordinary Windows laptop, validating its usability in real-world question-answering scenarios. By bypassing the LangChain wrapper and optimizing the testing strategy, the stability bottleneck in local inference was resolved.