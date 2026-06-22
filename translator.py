import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
# 初始化客户端
client = OpenAI(
    api_key="DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com"
)


def translate(text, source_lang="中文", target_lang="英文"):
    """
    调用DeepSeek大模型进行翻译，并给出优化建议
    """
    # 系统提示词：定义模型角色
    system_prompt = "你是一个专业的翻译助手，请将用户输入的文本翻译成目标语言，并简要给出翻译中词汇或语法的优化建议。"

    # 用户消息
    user_message = f"请将以下{source_lang}翻译成{target_lang}，并给出优化建议：\n{text}"

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # 使用 deepseek-chat 模型
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,  # 降低随机性，让翻译更稳定
            max_tokens=1024,
            stream=False
        )

        # 获取回复内容
        result = response.choices[0].message.content
        return result

    except Exception as e:
        return f"调用出错: {e}"


if __name__ == "__main__":
    print("===== DeepSeek 智能翻译官 =====")
    print("输入 'exit' 退出程序\n")

    while True:
        user_input = input("请输入要翻译的中文: ")
        if user_input.lower() == 'exit':
            print("再见！")
            break

        if not user_input.strip():
            print("输入为空，请重新输入。")
            continue

        print("\n思考中...\n")
        translation = translate(user_input)
        print(f"翻译结果：\n{translation}\n")
        print("-" * 40)