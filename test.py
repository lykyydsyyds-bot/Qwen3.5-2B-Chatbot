from langchain_community.llms import LlamaCpp

llm = LlamaCpp(
    model_path="./Qwen3.5-2B-Q4_K_M.gguf",
    verbose=True,
    n_ctx=2048,
    temperature=0.7,
    n_gpu_layers=0
)

response = llm.invoke("Explain e-commerce in simple terms.")
print(response)