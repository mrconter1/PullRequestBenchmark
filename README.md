# PullRequestBenchmark

Fellow software engineers, we are **genuinely** at the cusp of making ourselves obsolete through the power of automation! Can't wait to get there.

This effort might seem similar to [SWE-bench](https://www.swebench.com/) at first glance, but there are [key differences](#PullRequestBenchmark-vs-SWE-bench).

## Expert PR reviewers are likely expert PR creators

The journey towards automating the programming profession as we know it today is both fascinating and crucial. Here lies the core of our motivation for using LLMs to review PRs as a proxy for this significant transition.

1. **Assertion: Expertise in PR Review Capabilities Equates to Expertise in PR Creation Capability**

    a. *Intuitive Argument (Competence Argument)*: If LLMs can expertly review and make decisions on complex PRs—covering major refactoring, architecture redesigns, large feature additions, intricate bug fixes, or advanced security measures—it intuitively implies that they are also capable of creating complex high-quality PRs. The understanding, analysis, and judgment required to review such PRs would necessarily entail the ability to create them.

    b. *Logical Argument (Bootstrap Argument)*: Leveraging LLMs' expert review skills, even initially basic PRs could be iteratively generated and refined. This process of self-evaluation and improvement, akin to bootstrapping, could potentially lead to the creation of high-quality, human-level PRs over time.

2. **Assertion: PR Review Skill Evaluation is Easier Than PR Creation Skill Assessment**

    Assessing LLMs' PR review skills simplifies the evaluation process by allowing direct comparisons to human expert responses, focusing on the nuanced decision-making involved in software development.

3. **Assertion: Code Review Benchmarks Tracks Progress Toward Traditional Programming Role Obsolescence**

    By measuring the code review capabilities of LLMs using benchmarks, we can track advancements towards automating traditional programming roles in a tangible way. The ability of LLMs to generate complex pull requests autonomously implies a potential obsolescence of traditional programmer roles, signaling a transformation in the software development industry.

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