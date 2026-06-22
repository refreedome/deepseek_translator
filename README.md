

```markdown
# DeepSeek 智能翻译官

一个基于 DeepSeek 大模型的命令行翻译工具，输入中文即可获得英文翻译和优化建议。

## 功能特点

- 调用 DeepSeek-chat 模型进行高质量翻译
- 自动给出词汇和语法优化建议
- 交互式命令行界面，支持多轮翻译
- 使用环境变量管理 API Key，安全可靠
- 代码结构清晰，适合入门学习 API 调用

## 技术栈

- Python 3.8+
- OpenAI SDK (兼容 DeepSeek API)
- DeepSeek 大模型 API
- python-dotenv（环境变量管理）

## 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/refreedome/deepseek_translator.git
cd deepseek_translator
```

### 2. 创建虚拟环境（推荐）
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 配置 API Key
在项目根目录创建 `.env` 文件，写入你的 DeepSeek API Key：
```
DEEPSEEK_API_KEY=你的真实Key
```
> 注册并获取 Key：https://platform.deepseek.com/

⚠️ `.env` 文件已被 `.gitignore` 忽略，不会被上传到 GitHub，确保你的 Key 安全。

### 5. 运行
```bash
python translator.py
```

## 效果演示

```
===== DeepSeek 智能翻译官 =====
输入 'exit' 退出程序

请输入要翻译的中文: 我喜欢在周末去公园散步，感受大自然的气息。

思考中...

翻译结果：
I like taking a walk in the park on weekends to enjoy the atmosphere of nature.

优化建议：
- "感受大自然的气息" 译为 "enjoy the atmosphere of nature" 很自然，也可以用 "embrace the essence of nature" 增加文艺感。
```

## 项目结构
```
deepseek_translator/
├── translator.py      # 主程序
├── requirements.txt   # 依赖包列表
├── .gitignore         # Git 忽略规则
└── README.md          # 项目说明文档
```

## 学习笔记
这是我学习 Python 调用大模型 API 的第一个实战项目，通过它理解了：
- RESTful API 的调用模式
- 如何设计 Prompt 来控制模型输出
- 使用环境变量保护敏感信息
- Git 和 GitHub 的基本使用

后续计划：增加图形界面（GUI）、支持多语种互译。

## 联系方式
- GitHub: [@refreedome](https://github.com/refreedome)

欢迎 issue 和 star！
```
