# 自动化测试项目（基于 Selenium + Pytest）

## 项目简介

本项目是一个基于 **Selenium** 和 **Pytest** 的自动化测试框架，采用了**页面对象模型（POM）**设计模式，旨在提升测试代码的可维护性和扩展性。项目结构清晰，易于管理和开发，适合 Web 应用的自动化功能测试。

---

## 目录结构

- `config/`：存放项目配置文件，如浏览器配置、环境变量等。
- `pages/`：页面对象层，每个页面对应一个类，封装页面元素和操作。
- `tests/`：测试用例目录，使用 Pytest 编写，调用页面对象执行测试。
- `utils/`：工具模块，包含日志记录、截图、断言等辅助功能。
- `conftest.py`：Pytest 配置文件，定义fixture，实现测试初始化和清理。
- `pytest.ini`：Pytest 配置文件，用于配置测试参数和报告格式。
- `requirements.txt`：项目依赖包列表，方便环境搭建。

---

## 环境搭建

1. 克隆仓库到本地：

   ```bash
   git clone <your-repo-url>
   cd selenium_project
````

2. 创建并激活 Python 虚拟环境（推荐）：

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. 安装依赖包：

   ```bash
   pip install -r requirements.txt
   ```

4. 下载对应浏览器驱动（如 ChromeDriver），并配置环境变量。

---

## 使用说明

* **运行全部测试**

  ```bash
  pytest
  ```

* **生成测试报告（HTML格式）**

  ```bash
  pytest --html=report.html
  ```

* **运行指定测试用例**

  ```bash
  pytest tests/test_main_flow.py
  ```

---

## 功能特点

* **页面对象模型（POM）**：解耦页面元素和测试逻辑，便于维护。
* **灵活的测试配置**：通过 `config/settings.py` 可定制浏览器类型、测试环境等。
* **日志记录与截图**：自动生成测试日志和失败时截图，方便问题排查。
* **多用例支持**：支持多测试用例和测试套件的组织和执行。
* **支持测试夹具（fixture）**：统一管理测试前置和后置条件。

---

## 未来规划

* 集成 **CI/CD** 流水线，实现自动化测试的持续执行。
* 增加多浏览器支持，覆盖更广泛的测试场景。
* 丰富测试报告，集成 Allure 或其他测试报告工具。
* 优化测试用例覆盖，提升测试质量。

---

## 联系方式

如有问题或建议，欢迎通过 GitHub Issues 或邮件联系我。

```

