# PullRequestBenchmark

## Description

### What Software Developers Do That LLMs Can't (Yet)
Traditionally, LLMs have focused on generating code, often without fully understanding the collaborative and complex nature of real-world software development. Developers navigate vast codebases, integrating changes that respect both past work and team dynamics—areas where LLMs have room to grow.

### Shifting Perspective from Producing Perfect Code to Identifying It Perfectly
The PullRequestBenchmark shifts focus towards equipping LLMs with the judgment to accurately approve or reject pull requests. This approach aligns with the evolving needs of software development, emphasizing discernment in code quality over mere creation, and marking a step into an era of long-context intelligence.

### Using PR Review Ability for Self-supervising
Imagine an LLM that not only critiques but also learns from every piece of code it reviews, evolving into a system capable of generating flawless pull requests. This vision for self-supervised learning in LLMs promises a future where AI contributes deeply to software development, offering a blend of creativity and precision once thought exclusive to human developers.

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
