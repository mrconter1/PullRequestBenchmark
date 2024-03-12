# PullRequestBenchmark

## Introduction

Welcome to PullRequestBenchmark, a groundbreaking dataset and evaluation framework crafted to scrutinize the ability of Large Language Models (LLMs) in accurately approving or rejecting pull requests (PRs) in a manner consistent with human developers. Developed by Rasmus Lindahl, this benchmark aims to bridge the gap between artificial intelligence and software development practices, offering a unique tool to measure the contextual understanding and decision-making prowess of LLMs in real-world coding environments.

## Project Objective

PullRequestBenchmark seeks to evaluate LLMs' proficiency in considering the entire codebase context, proposed code changes, and PR information (title, description) to make approval or rejection decisions on par with human reviewers. This involves not just technical accuracy but also the comprehension of nuanced aspects like backward compatibility, code quality, and alignment with project goals.

## Dataset Description

The dataset comprises several key attributes for each PR, including:

- **Repository Size**: A measure of the code repository's overall size.
- **Change Size**: The scope of the proposed changes.
- **PR Title & Description**: Contextual information outlining the intent and details of the changes.
- **PR Result**: Indication of whether the PR was approved or rejected.
- **Rejection Reason**: Detailed feedback on the rationale behind the rejection (if applicable).

## Exclusion Policy

It is crucial that any foundation models trained with this dataset explicitly exclude the repository and its code to prevent any bias or overfitting. This ensures the integrity and the generalizability of the model's decision-making capabilities.

## Getting Started

To utilize the PullRequestBenchmark for training or evaluating your LLM, follow these steps:

1. **Clone the Repository**: Access the latest version of the dataset and evaluation tools.
2. **Dataset Preparation**: Familiarize yourself with the dataset structure and prepare your model's training environment accordingly.
3. **Model Training**: Integrate the dataset into your model's training regime, ensuring to adhere to the exclusion policy.
4. **Evaluation**: Use the provided evaluation framework to assess your model's performance against the benchmark.

## Contribution Guidelines

We welcome contributions from the community, including improvements to the dataset, evaluation methods, or any other resources that could enhance the PullRequestBenchmark. Please follow these steps to contribute:

1. **Fork the Repository**: Make a copy of the project to your GitHub account.
2. **Make Your Changes**: Implement the improvements or additions.
3. **Submit a Pull Request**: Open a PR to the main project with a detailed description of your changes.

For detailed contribution guidelines, please refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## Contact

For any inquiries or suggestions regarding the PullRequestBenchmark, please reach out to Rasmus Lindahl at rasmus.lindahl1996@gmail.com.

## License

PullRequestBenchmark is open-sourced under the [MIT License](LICENSE). We encourage the use and distribution of this dataset for academic and research purposes, ensuring that advancements in AI and software development are shared and accessible.
