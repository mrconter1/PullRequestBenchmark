# PullRequestBenchmark

## Introduction

PullRequestBenchmark serves as a comprehensive benchmark designed to evaluate Large Language Models' (LLMs) capability to approve or reject pull requests (PRs) with the same discernment as human reviewers. It is structured around a collection of PRs, each accompanied by all necessary contextual information, challenging LLMs to deliver decisions on approval or rejection. This task mirrors a critical aspect of software development, demanding a deep understanding of code context, quality, and project alignment. Achieving proficiency in this area represents a significant milestone for LLMs, potentially enabling models to not only assess PRs but also generate and select the most appropriate ones based on a given change description. This breakthrough would mark a pivotal step toward leveraging LLMs in enhancing software development and maintenance workflows.

## Benchmark Format

### Input to the Model

Models are furnished with inputs akin to those a developer would consider, including:

- **Entire Git History**: Offering a lens into the project's evolution and coding standards.
- **Pull Request Title and Description**: Providing context and specifics of the proposed changes.
- **Changeset**: Detailing the exact additions, deletions, and modifications proposed.

### Expected Output from the Model

The output is a binary decision, with the model delivering a verdict akin to a human reviewer's judgment:

- **Approved**: Signifies the PR aligns with project standards.
- **Rejected**: Indicates the PR falls short, with reasons for rejection articulated through specific feedback.

## How to Contribute

Extending the size of PullRequestBenchmark is greatly appreciated. Your contributions play a vital role in this effort. Here's how you can help:

1. **Identify Suitable Repositories**: Start by locating repositories that align with the scope of our benchmark.
2. **Find PRs**: Within these repositories, search for either approved or rejected Pull Requests (PRs) that capture the essence of reviewing.
3. **Format and Add Evaluation**: Follow our guidelines to document the evaluation data point correctly and add them to our benchmark suite.

For detailed contribution guidelines, please refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## Contact

For inquiries or suggestions, contact us via email at rasmus.lindahl1996@gmail.com.

## License

Licensed under the [MIT License](LICENSE), PullRequestBenchmark encourages academic and research use, promoting advancements in AI for software development.
