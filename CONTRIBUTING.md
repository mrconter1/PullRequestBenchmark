# Contributing to PullRequestBenchmark

We appreciate your interest in contributing to the PullRequestBenchmark dataset. This guide is designed to help contributors identify and document pull requests (PRs) effectively, enhancing the dataset's diversity and richness.

## Locating Suitable PRs

The goal is to populate the dataset with both approved and rejected PRs that offer a wide range of decision-making scenarios. Here's how you can locate suitable PRs on GitHub:

### For Rejected PRs

To find rejected PRs, use the GitHub search feature with the following query parameters:

```
is:pr is:closed is:merge
```

Adjust the search by adding specific keywords related to the project or technology you're interested in.

### For Approved PRs

Finding approved PRs that provide valuable learning data points is crucial. As of now, the specific search query for approved PRs is under development. However, a general approach would include:

```
is:pr is:closed is:merged 
```

Note: The search query might be refined in the future to better target PRs that meet our criteria.

## Documenting PRs

Once you have identified a suitable PR, the next step is to document it for inclusion in the PullRequestBenchmark dataset. Please collect the following information:

- **GitHub PR URL**: Provide the direct link to the PR. Example: `https://github.com/httpie/cli/pull/1178`
- **Type**: Categorize the PR. Common types include Bugfix, Feature, Improvement, Documentation, etc.
- **Rejection Reason (if applicable)**: Briefly describe the primary reason for rejection. Example: "Non-equivalent functionality"

Please ensure that the PR documentation is clear, concise, and free of any personal opinions or subjective interpretations.

## Submitting Your Contribution

To submit your documented PR to the PullRequestBenchmark dataset:

1. Fork the repository.
2. Create a new branch for your contribution.
3. Add your documented PRs to the dataset, following the existing format and guidelines.
4. Create a pull request against the main repository, providing a detailed description of your contribution.

Ensure to review your submission for accuracy and completeness before submitting.

## PR Types and Rejection Reasons

To help standardize the contributions and ensure consistency across the dataset, we have defined specific categories for PR types and reasons for PR rejection. Please use these categories to classify your submissions.

### PR Types

When documenting a PR, select the type that best describes the nature of the contribution:

- **Bugfix**: Addresses and resolves a specific issue or bug in the code.
- **Feature**: Introduces new functionality or features to the project.
- **Improvement**: Enhancements or optimizations to existing code or features without adding new functionality.
- **Documentation**: Updates, additions, or improvements to documentation.

### Rejection Reasons

For rejected PRs, please specify the primary reason for rejection, choosing from the following categories:

- **Non-equivalent functionality**: The proposed changes modify the existing functionality too significantly.
- **Lack of tests**: The PR fails to include necessary tests or sufficient test coverage.
- **Coding standards violation**: The changes do not adhere to the project's established coding standards.
- **Out of project scope**: The PR introduces changes or features that are beyond the current scope or goals of the project.

## Questions or Suggestions

If you have any questions or suggestions about contributing to PullRequestBenchmark, please feel free to reach out. We're always looking to improve the process and make it easier for contributors to participate.

Thank you for contributing to the advancement of AI in software development practices!
