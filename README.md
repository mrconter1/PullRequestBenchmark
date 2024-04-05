# PullRequestBenchmark

Fellow software engineers, we are **genuinely** at the cusp of making ourselves obsolete through the power of automation! Can't wait to get there.

This effort might seem similar to [SWE-bench](https://www.swebench.com/) at first glance, but there are [key differences](#PullRequestBenchmark-vs-SWE-bench).

## Expert PR reviewers are likely expert PR creators

The journey towards automating the programming profession as we know it today is both fascinating and crucial. Here lies the core of our motivation for using LLMs to review PRs as a proxy for this significant transition.

1. **Complex PR Review Capabilities Imply Complex PR Creation Capability**: If LLMs can expertly review and make decisions on complex PRs—covering major refactoring, architecture redesigns, large feature additions, intricate bug fixes, or advanced security measures—it implies that they are also capable of creating complex high-quality PRs.

2. **PR Review Skill Evaluation is Easier Than PR Creation Skill Assessment**: Assessing LLMs' PR review skills simplifies the evaluation process by allowing direct comparisons to human expert responses, focusing on the nuanced decision-making involved in software development.

3. **Autonomous Complex PR Generation Could Eliminate Traditional Programmer Roles**: The ability of LLMs to autonomously generate complex PRs for projects as intricate as the Linux kernel may redefine or even phase out the traditional concept of a "programmer," shifting the landscape of software development.

4. **Code Review Benchmarks Tracks Progress Toward Programming Automation**: Creating a benchmark for LLMs' code review abilities offers a clear method to track progress towards fully automating programming, providing tangible milestones on this transformative journey.

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

## Prompt Size and Distribution

The PullRequestBenchmark encompasses a wide range of prompt sizes, reflecting the diversity of real-world software development scenarios. Prompt sizes, measured in tokens, vary significantly, with the smallest being around 125,506 tokens and the largest exceeding 49,015,233 tokens. This variation underscores the benchmark's comprehensive approach to evaluating LLMs across simple to complex pull request reviews. The distribution of prompt sizes illustrates the challenges in software development tasks, ranging from minor code tweaks to substantial feature additions or optimizations.

## Contact

For inquiries or suggestions, contact us via email at rasmus.lindahl1996@gmail.com.

## License

Licensed under the [MIT License](LICENSE), PullRequestBenchmark encourages academic and research use, promoting advancements in AI for software development.

-------------------------------------

## PullRequestBenchmark vs. SWE-bench

- **Focus**: PullRequestBenchmark evaluates LMs on reviewing pull requests to ensure they align with project standards. SWE-bench tests LMs' ability to solve real-world GitHub issues by generating fixes that pass unit tests.
  
- **Objective**: PullRequestBenchmark aims at decision-making in PR reviews, emphasizing quality assurance. SWE-bench focuses on problem-solving, specifically generating solutions for issues.

- **Evaluation**: PullRequestBenchmark assesses binary decision-making (approve or reject) on PRs. SWE-bench measures success by whether generated solutions resolve issues, validated through unit tests.

- **Inputs**: PullRequestBenchmark evaluates the reviewing of PRs, incorporating the full Git history and PR details to support these assessments. SWE-bench, focusing on code creation, considers only the current state of the repository through Issue-PR pairs.