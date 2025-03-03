from openai import OpenAI


client = OpenAI(
    api_key="sk-21d0c971972c4822a28217ba67947000",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁'}],
    stream=True,
    stream_options={"include_usage": True}
    )

full_content = ""
for chunk in completion:
    if chunk.choices == []:
        continue
    full_content += chunk.choices[0].delta.content
    print(chunk.choices[0].delta.content, end='', flush=True)



