import sys
if sys.platform == "win32":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import streamlit as st
from llama_cpp import Llama

st.set_page_config(page_title="Qwen3.5 智能助手", page_icon="🤖")
st.title("🤖 Qwen3.5 本地聊天机器人")
st.caption("基于 Qwen3.5-2B 量化模型 (GGUF)")

@st.cache_resource
def load_model():
    return Llama(
        model_path="./Qwen3.5-2B-Q4_K_M.gguf",
        n_ctx=2048,
        n_threads=8,            # 使用多线程加速
        verbose=False
    )

llm = load_model()
st.success("✅ 模型加载成功！")

user_input = st.text_input("💬 请输入你的问题：", placeholder="例如：请解释一下什么是人工智能？")

if st.button("🚀 发送", type="primary"):
    if user_input:
        with st.spinner("🧠 模型思考中..."):
            try:
                # 直接调用底层库的生成函数
                output = llm(
                    user_input,
                    max_tokens=2048,
                    temperature=0.7,
                    stop=["<|im_end|>", "<|endoftext|>"],  # 设置结束标记，防止无限生成
                    echo=False
                )
                response = output["choices"][0]["text"]
                st.success("📝 回答如下：")
                st.write(response)
            except Exception as e:
                st.error(f"生成出错：{e}")
    else:
        st.warning("⚠️ 请先输入问题。")

st.divider()
st.caption("💡 提示：首次回复可能需要几秒加载，之后会更快。")