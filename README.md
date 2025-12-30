# My-PromptWizard 🧙

> **这是一个基于 PromptWizard 的 Fork 项目，适配了自定义 LLM API（如 apinexus.net）的使用场景**

## 📖 项目简介

本项目是 [PromptWizard](https://github.com/microsoft/PromptWizard) 的一个 Fork，主要目的是：

- ✅ **适配自定义 LLM API**：支持使用 OpenAI 兼容的 API 端点（如 `apinexus.net`）
- ✅ **提供中文教学示例**：包含完整的中文文档和 Hello World 示例
- ✅ **快速上手**：提供最简单的使用场景，帮助初学者快速了解 PromptWizard

### 主要特性

- 🔧 **自定义 Base URL 支持**：修改了 `llm_mgr.py` 以支持自定义 `base_url`
- 📚 **My-Helloworld 示例**：提供最简单的使用示例（场景1：无训练数据，无示例）
- 🧪 **测试用例**：包含 pytest 测试用例，验证 API 连接和基本功能
- 📖 **中文文档**：完整的中文 README 和使用指南

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/thiswind/My-PromptWizard.git
cd My-PromptWizard
```

### 2. 环境准备

#### 2.1 激活 Conda 环境

```bash
# 激活 conda 环境（根据你的环境名称修改）
conda activate base
```

#### 2.2 安装项目依赖

```bash
# 在项目根目录执行
pip install -e .
```

这将安装 PromptWizard 及其所有依赖，包括：
- `llama-index==0.11.10`
- `llama-index-core==0.11.10`
- `openai`, `datasets`, `tiktoken`, `nltk`, `pyyaml`, `python-dotenv` 等

### 3. 运行 Hello World 示例

#### 3.1 配置环境变量

```bash
cd demos/my-helloworld
cp .env.example .env
```

编辑 `.env` 文件，配置以下变量：

```bash
# 是否使用 OpenAI API Key
USE_OPENAI_API_KEY="True"

# 你的 API Key（请替换为真实值）
OPENAI_API_KEY="your-api-key-here"

# 模型名称（根据你的 API 提供商修改）
OPENAI_MODEL_NAME="gpt-5.2"

# API Base URL（根据你的 API 提供商修改）
OPENAI_API_BASE_URL="https://apinexus.net/v1"
```

**重要提示**：
- ⚠️ 不要将包含真实 API key 的 `.env` 文件提交到 Git
- ✅ `.env.example` 文件是安全的，可以提交到 Git

#### 3.2 运行示例

```bash
# 确保在 my-helloworld 目录中
cd demos/my-helloworld

# 运行示例
python hello_world.py
```

### 4. 查看详细文档

更多详细信息，请查看：
- 📖 [My-Helloworld 示例完整文档](demos/my-helloworld/README.md)
- 🧪 [测试用例](tests/test_scenarios.py)

## 🔧 适配自定义 LLM API

### 适配 apinexus.net

如果你使用的是基于 `apinexus.net` 的 LLM API，需要做以下配置：

#### 1. 设置 Base URL

在 `.env` 文件中设置：

```bash
OPENAI_API_BASE_URL="https://apinexus.net/v1"
```

#### 2. 设置模型名称

根据 `apinexus.net` 提供的模型名称设置：

```bash
# 示例：如果 apinexus.net 提供的模型名称是 gpt-5.2
OPENAI_MODEL_NAME="gpt-5.2"
```

#### 3. 设置 API Key

```bash
# 使用你在 apinexus.net 获取的 API key
OPENAI_API_KEY="your-apinexus-api-key"
```

#### 4. 代码修改说明

本项目修改了 `promptwizard/glue/common/llm/llm_mgr.py`，添加了对自定义 `base_url` 的支持：

```python
if os.environ['USE_OPENAI_API_KEY'] == "True":
    base_url = os.environ.get("OPENAI_API_BASE_URL", None)
    if base_url:
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], base_url=base_url)
    else:
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
```

### 适配其他 OpenAI 兼容的 API

如果你使用的是其他 OpenAI 兼容的 API，只需要：

1. 在 `.env` 文件中设置 `OPENAI_API_BASE_URL` 为你的 API 端点
2. 设置 `OPENAI_MODEL_NAME` 为你的 API 支持的模型名称
3. 设置 `OPENAI_API_KEY` 为你的 API key

## 📚 项目结构

```
My-PromptWizard/
├── README.md                    # 本文件（项目主 README）
├── demos/
│   ├── my-helloworld/          # Hello World 示例（推荐从这里开始）
│   │   ├── README.md           # 详细的使用文档
│   │   ├── hello_world.py      # 示例脚本
│   │   ├── .env.example        # 环境变量示例
│   │   └── configs/            # 配置文件
│   └── scenarios/              # 其他场景示例
├── tests/                      # 测试用例
│   ├── test_scenarios.py      # 场景测试
│   └── conftest.py            # pytest 配置
├── promptwizard/               # PromptWizard 核心代码
│   └── glue/
│       └── common/
│           └── llm/
│               └── llm_mgr.py  # 已修改：支持自定义 base_url
└── ...
```

## 🧪 运行测试

```bash
# 激活 conda 环境
conda activate base

# 运行测试
pytest tests/test_scenarios.py -v
```

## 📖 PromptWizard 背景介绍

以下内容来自 [PromptWizard 官方项目](https://github.com/microsoft/PromptWizard)，作为项目背景介绍：

---

### PromptWizard: Task-Aware Prompt Optimization Framework

> **PromptWizard: Task-Aware Prompt Optimization Framework**  
> Eshaan Agarwal, Joykirat Singh, Vivek Dani, Raghav Magazine, Tanuja Ganu, Akshay Nambi

### Overview 🌟

PromptWizard is a discrete prompt optimization framework that employs a self-evolving mechanism where the LLM generates, critiques, and refines its own prompts and examples, continuously improving through iterative feedback and synthesis. This self-adaptive approach ensures holistic optimization by evolving both the instructions and in-context learning examples for better task performance.

Three key components of PromptWizard are the following:

- **Feedback-driven Refinement**: LLM generates, critiques, and refines its own prompts and examples, continuously improving through iterative feedback and synthesis
- **Critique and Synthesize diverse examples**: Generates synthetic examples that are robust, diverse and task-aware. Also it optimizes both prompt and examples in tandem
- **Self generated Chain of Thought (CoT) steps** with combination of positive, negative and synthetic examples

### How PromptWizard Works 🔍

- Using the problem description and initial prompt instruction, PW generates variations of the instruction by prompting LLMs to mutate it. Based on performance, the best prompt is selected. PW incorporates a critique component that provides feedback, thus guiding and refining the prompt over multiple iterations.
- PW also optimizes in-context examples. PW selects a diverse set of examples from the training data, identifying positive and negative examples based on their performance with the modified prompt. Negative examples help inform further prompt refinements.
- Examples and instructions are sequentially optimized, using the critique to generate synthetic examples that address the current prompt's weaknesses. These examples are integrated to further refine the prompt.
- PW generates detailed reasoning chains via Chain-of-Thought (CoT), enriching the prompt's capacity for problem-solving.
- PW aligns prompts with human reasoning by integrating task intent and expert personas, enhancing both model performance and interpretability.

### Three Main Scenarios

PromptWizard supports three main usage scenarios:

1. **Scenario 1**: Optimizing prompts without examples
2. **Scenario 2**: Generating synthetic examples and using them to optimize prompts
3. **Scenario 3**: Optimizing prompts with training data

### Citation 📝

If you make use of PromptWizard, please cite the original paper:

```
@misc{agarwal2024promptwizardtaskawarepromptoptimization,
      title={PromptWizard: Task-Aware Prompt Optimization Framework}, 
      author={Eshaan Agarwal and Joykirat Singh and Vivek Dani and Raghav Magazine and Tanuja Ganu and Akshay Nambi},
      year={2024},
      eprint={2405.18369},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2405.18369}, 
}
```

### 官方资源

- 📄 [论文](https://arxiv.org/abs/2405.18369)
- 🌐 [项目网站](https://microsoft.github.io/PromptWizard/)
- 📝 [官方博客](https://www.microsoft.com/en-us/research/blog/promptwizard-the-future-of-prompt-optimization-through-feedback-driven-self-evolving-prompts/)
- 🔗 [官方 GitHub 仓库](https://github.com/microsoft/PromptWizard)

---

## 🔄 与官方版本的差异

### 主要修改

1. **支持自定义 Base URL**
   - 修改了 `promptwizard/glue/common/llm/llm_mgr.py`
   - 添加了 `OPENAI_API_BASE_URL` 环境变量支持

2. **添加中文文档和示例**
   - 创建了 `demos/my-helloworld/` 示例
   - 提供了完整的中文 README 和使用指南

3. **添加测试用例**
   - 创建了 `tests/` 目录
   - 添加了 pytest 测试用例

### 兼容性

- ✅ 与官方版本完全兼容
- ✅ 支持所有官方功能
- ✅ 可以无缝切换到官方版本

## ❓ 常见问题

### Q: 如何确认使用的是自定义 API？

A: 检查 `.env` 文件中的 `OPENAI_API_BASE_URL` 是否设置为你的 API 端点。

### Q: 模型名称在哪里查看？

A: 模型名称通常在你的 API 提供商的文档或控制台中查看。

### Q: API 调用失败怎么办？

A: 检查以下几点：
1. `OPENAI_API_BASE_URL` 是否正确
2. `OPENAI_API_KEY` 是否有效
3. `OPENAI_MODEL_NAME` 是否与 API 提供商支持的模型名称一致
4. 网络连接是否正常

### Q: 如何学习更多？

A: 
- 查看 [My-Helloworld 示例文档](demos/my-helloworld/README.md)
- 查看 [官方 PromptWizard 文档](https://github.com/microsoft/PromptWizard)
- 查看 `demos/scenarios/dataset_scenarios_demo.ipynb` 了解其他场景

## 📄 许可证

本项目遵循 [MIT License](LICENSE)。

## 🙏 致谢

- 感谢 [PromptWizard 团队](https://github.com/microsoft/PromptWizard) 提供优秀的框架
- 感谢所有贡献者的支持

---

**最后更新**: 2025-12-30
