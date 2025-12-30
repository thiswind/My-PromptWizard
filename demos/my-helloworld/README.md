# PromptWizard Hello World 示例

这是一个最简单的 PromptWizard 使用示例，演示如何使用 PromptWizard 优化提示词。

## 📖 简介

这个示例展示了 **场景1：无训练数据，无示例** 的使用方式，这是 PromptWizard 最简单的使用场景。

### 适用对象

- 想快速了解 PromptWizard 的初学者
- 想测试自己的 LLM API 连接的用户
- 想学习如何配置 PromptWizard 的用户

### 这个示例会做什么？

1. 加载配置文件和环境变量
2. 创建 PromptWizard 优化器
3. 调用 LLM API 生成优化的提示词
4. 显示优化结果

### 场景说明

**场景1：无训练数据，无示例**
- ✅ 不需要准备训练数据
- ✅ 不需要提供示例
- ✅ 只需要任务描述和基础指令
- ✅ 适合快速测试和学习

## 🚀 快速开始

### 1. 环境准备

#### 1.1 激活 Conda 环境

```bash
# 激活 conda 环境（根据你的环境名称修改）
conda activate base
```

#### 1.2 安装项目依赖

```bash
# 在项目根目录执行
cd /path/to/PromptWizard
pip install -e .
```

这将安装 PromptWizard 及其所有依赖，包括：
- `llama-index==0.11.10`
- `llama-index-core==0.11.10`
- `openai`, `datasets`, `tiktoken`, `nltk`, `pyyaml`, `python-dotenv` 等

### 2. 配置环境变量

#### 2.1 复制环境变量示例文件

```bash
cd demos/my-helloworld
cp .env.example .env
```

#### 2.2 编辑 .env 文件

使用文本编辑器打开 `.env` 文件，配置以下变量：

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
- ✅ 使用占位符 `your-api-key-here` 作为示例

### 3. 运行示例

```bash
# 确保在 my-helloworld 目录中
cd demos/my-helloworld

# 运行示例
python hello_world.py
```

或者直接使用可执行权限：

```bash
./hello_world.py
```

## ⚙️ 配置说明

### 环境变量配置

#### 必需的环境变量

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `USE_OPENAI_API_KEY` | 是否使用 OpenAI API Key | `"True"` |
| `OPENAI_API_KEY` | 你的 API Key | `"sk-..."` |
| `OPENAI_MODEL_NAME` | 模型名称 | `"gpt-5.2"` |
| `OPENAI_API_BASE_URL` | API Base URL | `"https://apinexus.net/v1"` |

#### 环境变量加载顺序

`hello_world.py` 会按以下顺序尝试加载环境变量：

1. 项目根目录的 `my.env` 文件
2. 当前目录的 `.env` 文件
3. 系统环境变量

### 配置文件说明

#### promptopt_config.yaml

这是提示词优化的配置文件，主要参数：

- `task_description`: 任务描述
- `base_instruction`: 基础指令
- `mutation_rounds`: 变异轮数（已优化为 1，加快运行）
- `mutate_refine_iterations`: 优化迭代次数（已优化为 1，加快运行）

#### setup_config.yaml

这是 PromptWizard 的设置配置文件：

- `assistant_llm.prompt_opt`: 使用的模型 ID
- `mode`: 运行模式（`offline` 或 `online`）
- `experiment_name`: 实验名称

## 🔧 适配 apinexus.net

如果你使用的是基于 apinexus.net 的 LLM API，需要做以下配置：

### 1. 设置 Base URL

在 `.env` 文件中设置：

```bash
OPENAI_API_BASE_URL="https://apinexus.net/v1"
```

### 2. 设置模型名称

根据 apinexus.net 提供的模型名称设置：

```bash
# 示例：如果 apinexus.net 提供的模型名称是 gpt-5.2
OPENAI_MODEL_NAME="gpt-5.2"
```

### 3. 设置 API Key

```bash
# 使用你在 apinexus.net 获取的 API key
OPENAI_API_KEY="your-apinexus-api-key"
```

### 4. 验证配置

运行示例，如果看到以下输出，说明配置成功：

```
[步骤 1] 加载环境变量...
  ✓ 从 /path/to/my.env 加载环境变量
  ✓ 环境变量检查通过

[步骤 5] 调用优化函数生成提示词...
  （这可能需要 30-120 秒，取决于 API 响应速度）
  
Mutating Task Description....
Optimization Finished...
  
  ✓ 优化过程完成！
```

### 5. 常见问题

#### Q: 如何确认使用的是 apinexus.net？

A: 检查 `.env` 文件中的 `OPENAI_API_BASE_URL` 是否为 `https://apinexus.net/v1`

#### Q: 模型名称在哪里查看？

A: 模型名称通常在你的 API 提供商（apinexus.net）的文档或控制台中查看

#### Q: API 调用失败怎么办？

A: 检查以下几点：
1. `OPENAI_API_BASE_URL` 是否正确
2. `OPENAI_API_KEY` 是否有效
3. `OPENAI_MODEL_NAME` 是否与 API 提供商支持的模型名称一致
4. 网络连接是否正常

## 💻 代码说明

### hello_world.py 主要步骤

#### 步骤 1: 加载环境变量

```python
from dotenv import load_dotenv

# 从 .env 文件加载环境变量
load_dotenv(env_file, override=True)
```

#### 步骤 2: 设置配置文件路径

```python
promptopt_config_path = config_dir / "promptopt_config.yaml"
setup_config_path = config_dir / "setup_config.yaml"
```

#### 步骤 3: 创建 GluePromptOpt 对象

```python
gp = GluePromptOpt(
    str(promptopt_config_path),
    str(setup_config_path),
    dataset_jsonl=None,  # 场景1：无训练数据
    data_processor=None  # 场景1：无数据处理器
)
```

#### 步骤 4: 调用优化函数

```python
best_prompt, expert_profile = gp.get_best_prompt(
    use_examples=False,
    run_without_train_examples=True,
    generate_synthetic_examples=False
)
```

### 关键参数说明

- `use_examples=False`: 不使用示例
- `run_without_train_examples=True`: 在没有训练示例的情况下运行
- `generate_synthetic_examples=False`: 不生成合成示例

## 📊 输出说明

### 简化输出示例

运行成功后，你会看到以下关键输出：

```
======================================================================
PromptWizard Hello World 示例
======================================================================

这个示例演示如何使用 PromptWizard 优化提示词（场景1：无训练数据）
任务：中文文本摘要

[步骤 1] 加载环境变量...
  ✓ 从 /path/to/my.env 加载环境变量
  ✓ 环境变量检查通过

[步骤 2] 设置配置文件路径...
  ✓ 提示词优化配置: .../promptopt_config.yaml
  ✓ 设置配置: .../setup_config.yaml

[步骤 3] 加载配置文件...
  ✓ 配置文件加载成功
  - 任务描述: 你是一个文本摘要专家。你需要将给定的文本总结成简洁的摘要。
  - 基础指令: 请仔细阅读文本，提取关键信息，生成简洁准确的摘要。
  - 变异轮数: 2
  - 优化迭代次数: 2

[步骤 4] 创建 GluePromptOpt 对象...
  （这可能需要几秒钟）
  ✓ GluePromptOpt 对象创建成功

[步骤 5] 调用优化函数生成提示词...
  （这可能需要 30-120 秒，取决于 API 响应速度）
  （优化过程会生成变异的提示词并调用 LLM API）

Mutating Task Description....
Optimization Finished...

  ✓ 优化过程完成！

======================================================================
优化结果
======================================================================

【专家身份描述】
----------------------------------------------------------------------
你是一名文本摘要专家，兼具计算语言学与信息检索背景，长期为新闻编辑、学术研究、法律与技术写作提供高质量摘要。你精通抽取式与生成式方法，能够在不失真、不臆造的前提下，将长篇、多源或噪声文本压缩为简洁、准确、可读的内容。你擅长识别并保留关键信息与脉络，包括人物/实体、时间线、数据与指标、因果链、对比关系与核心结论，同时有效去冗余、消除重复与歧义，确保事实一致性与术语准确。

你能根据需求灵活控制摘要的长度、结构与语气：支持要点式或段落式、导语+要点、标题+摘要等多种形式；可面向不同受众（专家/大众/管理者）调整细节密度与可读性；支持多语言与跨领域文本处理。你具备强大的对齐与评估能力，熟悉ROUGE、BERTScore等指标与金字塔法、RST等语篇框架，结合主题建模、语义相似度与冗余抑制技术提升覆盖率与连贯性；同时具备事实核查与数值校对能力，可在需要时标注来源句或保留关键原文短语。开始前你会澄清用途、受众与长度限制，并据此输出结构化、信息密度高、易于二次利用的简洁摘要，必要时附上关键词与后续阅读建议。

【优化后的提示词】
----------------------------------------------------------------------
你是一个文本摘要专家。你需要将给定的文本总结成简洁的摘要。
请仔细阅读文本，提取关键信息，生成简洁准确的摘要。

请先说明你的摘要思路，然后提供最终的摘要。
Keywords: 深度阅读理解, 关键信息提取, 准确简洁表达, 中文摘要生成, 长文本处理

======================================================================
执行总结
======================================================================

✅ 示例执行成功！

关键验证点：
  1. ✓ 环境变量配置正确
  2. ✓ 配置文件加载成功
  3. ✓ GluePromptOpt 对象创建成功
  4. ✓ API 连接成功（优化过程完成，无异常）
  5. ✓ 优化过程完成（生成了变异的提示词）
```

### 详细输出说明

#### 步骤 4 的额外输出（可选查看）

在创建 `GluePromptOpt` 对象时，你可能会看到配置参数信息：

```
Setup configurations parameters: [...]
Prompt Optimization parameters: [...]
```

这些是调试信息，显示了 PromptWizard 使用的配置参数。**这些信息不影响使用，可以忽略**。

#### 步骤 5 的详细优化过程

在步骤 5 中，优化过程会显示详细的日志信息：

1. **迭代进度条**：
   ```
   Iterations completed:   0%|          | 0/2 [00:00<?, ?it/s]
   ```

2. **变异过程日志**：
   ```
   + Starting iteration: 1
   current_base_instruction: 请仔细阅读文本，提取关键信息，生成简洁准确的摘要。
   mutation_round=0 mutated_sample_prompt=...
   mutation_round=1 mutated_sample_prompt=...
   ```

3. **生成的提示词变体**：
   优化过程会生成多个提示词变体，每个变体都用 `<START>` 和 `<END>` 标记：
   ```
   mutated_prompt_generation=
   <START>
   请仔细阅读文本，提取关键信息并生成简洁准确的摘要。在输出前，先在内部思考如何简化问题（先列出核心实体、事件与结论再压缩），并设计一个小对比实验（主题-要点式 vs 因果-过程式）以选择更清晰的表达。以准确性、覆盖率与简洁性为衡量标准优化结果；仅输出最终摘要。
   <END>
   <START>
   请阅读文本并识别核心信息，生成2-3句精准摘要。请在内部设定关键假设（面向一般读者、无新增信息、语句通顺），并做快速实验比较约30%与50%压缩两种版本，选择更易懂者。以是否遗漏关键信息与是否言简意赅作为进度衡量，仅输出最终摘要。
   <END>
   ...
   ```

4. **专家身份描述和最终提示词**：
   ```
   Possible prompt variations:
   _______________________________________________________________________
   Variations 1:
   Expert Profile:
   你是一名文本摘要专家，兼具计算语言学与信息检索背景，长期为新闻编辑、学术研究、法律与技术写作提供高质量摘要。你精通抽取式与生成式方法，能够在不失真、不臆造的前提下，将长篇、多源或噪声文本压缩为简洁、准确、可读的内容。你擅长识别并保留关键信息与脉络，包括人物/实体、时间线、数据与指标、因果链、对比关系与核心结论，同时有效去冗余、消除重复与歧义，确保事实一致性与术语准确。
   
   你能根据需求灵活控制摘要的长度、结构与语气：支持要点式或段落式、导语+要点、标题+摘要等多种形式；可面向不同受众（专家/大众/管理者）调整细节密度与可读性；支持多语言与跨领域文本处理。你具备强大的对齐与评估能力，熟悉ROUGE、BERTScore等指标与金字塔法、RST等语篇框架，结合主题建模、语义相似度与冗余抑制技术提升覆盖率与连贯性；同时具备事实核查与数值校对能力，可在需要时标注来源句或保留关键原文短语。开始前你会澄清用途、受众与长度限制，并据此输出结构化、信息密度高、易于二次利用的简洁摘要，必要时附上关键词与后续阅读建议。
   Prompt:
   你是一个文本摘要专家。你需要将给定的文本总结成简洁的摘要。
   请仔细阅读文本，提取关键信息，生成简洁准确的摘要。

   请先说明你的摘要思路，然后提供最终的摘要。
   Keywords: 深度阅读理解, 关键信息提取, 准确简洁表达, 中文摘要生成, 长文本处理
   ```

5. **时间统计**：
   ```
   Time taken to find best prompt: 298.48221731185913 sec
   ```

**说明**：这些详细输出是 PromptWizard 优化过程的正常日志，有助于理解优化过程。如果你只是想快速验证功能，可以只关注关键步骤的输出。

### 场景1的特殊说明

在场景1（无训练数据，无示例）中：

- ✅ 优化过程会正常完成
- ✅ API 调用会成功
- ✅ 会生成变异的提示词（在日志中可见）
- ✅ 返回值（`best_prompt` 和 `expert_profile`）包含优化后的提示词和专家身份描述
- ✅ 这是正常的，主要验证点是：优化过程完成，没有异常

**关键日志标识**：
- `Mutating Task Description....` - 说明正在生成变异的提示词
- `Optimization Finished...` - 说明优化过程完成
- `Time taken to find best prompt: X sec` - 显示优化耗时

**返回值说明**

在场景1中，PromptWizard 会生成多个提示词变体（在日志中可见），并返回第一个生成的变体作为 `best_prompt` 和 `expert_profile`。这确保了：

1. 优化过程完成（没有异常）
2. 日志中显示了变异提示词的生成
3. API 调用成功
4. 返回值包含实际生成的优化结果

**返回值内容**：
- **expert_profile**：详细的中文专家身份描述，说明专家应具备的能力和背景
- **best_prompt**：优化后的完整提示词，包括任务描述、基础指令、答案格式和关键词

## ❓ 常见问题

### Q1: 提示 "ModuleNotFoundError: No module named 'llama_index'"

**原因**: 项目依赖未安装

**解决方法**:
```bash
# 激活 conda 环境
conda activate base

# 安装项目依赖
pip install -e .
```

### Q2: 提示 "Missing required environment variables"

**原因**: 环境变量未配置

**解决方法**:
1. 复制 `.env.example` 为 `.env`
2. 编辑 `.env` 文件，填入真实的 API key 和配置
3. 确保 `.env` 文件在正确的位置（项目根目录或当前目录）

### Q3: API 调用失败

**原因**: API 配置不正确

**解决方法**:
1. 检查 `OPENAI_API_KEY` 是否正确
2. 检查 `OPENAI_API_BASE_URL` 是否正确（如果使用自定义 API）
3. 检查 `OPENAI_MODEL_NAME` 是否与 API 提供商支持的模型名称一致
4. 检查网络连接

### Q4: 运行时间很长

**原因**: 这是正常的，因为需要调用 LLM API

**说明**:
- 优化过程需要调用多次 LLM API
- 每次 API 调用可能需要几秒到几十秒
- 总时间通常在 30-120 秒之间
- 可以通过减少 `mutation_rounds` 和 `mutate_refine_iterations` 来加快速度（但会影响优化质量）

### Q5: 优化结果包含什么内容？

**说明**: 在场景1中，优化结果包含：

- **expert_profile**：详细的中文专家身份描述，说明专家应具备的能力和背景。例如，对于文本摘要任务，会描述专家在计算语言学、信息检索、文本压缩等方面的专业能力。

- **best_prompt**：优化后的完整提示词，包括：
  - 任务描述（例如："你是一个文本摘要专家。你需要将给定的文本总结成简洁的摘要。"）
  - 基础指令（可能已被优化，例如："请仔细阅读文本，提取关键信息，生成简洁准确的摘要。"）
  - 答案格式（例如："请先说明你的摘要思路，然后提供最终的摘要。"）
  - 关键词（例如："深度阅读理解, 关键信息提取, 准确简洁表达, 中文摘要生成, 长文本处理"）

这些内容都是中文的，与配置的任务类型（文本摘要）相关。优化过程会生成多个提示词变体，并返回第一个生成的变体作为最终结果。

## 🔄 下一步

### 扩展这个示例

1. **修改任务描述**: 编辑 `configs/promptopt_config.yaml` 中的 `task_description`
2. **修改基础指令**: 编辑 `configs/promptopt_config.yaml` 中的 `base_instruction`
3. **增加迭代次数**: 修改 `mutation_rounds` 和 `mutate_refine_iterations`（会增加运行时间）
4. **尝试其他场景**: 参考 `demos/scenarios/` 中的其他示例

### 学习更多

- 查看 `demos/scenarios/dataset_scenarios_demo.ipynb` 了解其他场景
- 查看项目根目录的 `README.md` 了解 PromptWizard 的完整功能
- 查看 `tests/test_scenarios.py` 了解测试用例

## 📝 文件结构

```
demos/my-helloworld/
├── README.md                    # 本文件
├── hello_world.py              # 示例脚本
├── .env.example                # 环境变量示例（不含 API key）
└── configs/
    ├── promptopt_config.yaml   # 提示词优化配置
    └── setup_config.yaml       # 设置配置
```

## 🔒 安全提示

- ⚠️ **不要**将包含真实 API key 的 `.env` 文件提交到 Git
- ✅ **可以**将 `.env.example` 文件提交到 Git（使用占位符）
- ✅ 使用 `.gitignore` 忽略 `.env` 文件

## 📄 许可证

本示例遵循 PromptWizard 项目的许可证（MIT License）。

## 🙏 致谢

本示例基于 PromptWizard 项目的测试用例创建，感谢 PromptWizard 团队。

---

**最后更新**: 2025-12-30

