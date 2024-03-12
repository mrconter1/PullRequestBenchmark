# Contributing to PullRequestBenchmark

We appreciate your interest in contributing to the PullRequestBenchmark dataset. This guide is designed to help contributors identify and document pull requests (PRs) effectively, enhancing the dataset's diversity and richness.

## Locating Suitable PRs

The goal is to populate the dataset with both approved and rejected PRs that offer a wide range of decision-making scenarios. Here's how you can locate suitable PRs on GitHub:

### For Rejected PRs

To find rejected PRs, use the GitHub search feature with the following query parameters:

```
is:pr is:closed is:unmerged
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

- `GitHub_PR_URL`: The direct URL to the GitHub Pull Request.
- `Type`: The category of the Pull Request, such as Bugfix, Feature, Improvement, Documentation, Refactoring, etc.
- `Outcome`: The status of the Pull Request, Approved or Rejected.
- `RejectionReason`: If applicable, the primary caegory for the rejection of the Pull Request.
- `Comment`: Additional remarks or context regarding the Pull Request, such as the significance of the contribution or specific aspects of the Pull Request that were notable.

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

1. `Bugfix`: Addresses and resolves an issue or error in the existing code.
2. `Feature`: Adds new functionality or features to the project.
3. `Documentation`: Improves or adds to the project's documentation.
4. `Improvement`: Enhances existing features or the project's performance without adding new functionality.
5. `Refactoring`: Code changes that neither fix a bug nor add a feature but improve the structure or readability.
6. `Testing`: Adds or improves existing tests, including unit tests, integration tests, and end-to-end tests.
7. `Dependency Update`: Updates or modifies project dependencies, libraries, or frameworks.
8. `Configuration Change`: Adjustments to project configuration files or settings.
9. `UI/UX`: Changes or enhancements to the user interface or user experience design.
10. `Localization`: Adds or improves support for additional languages or regional settings.

### Rejection Reasons

For rejected PRs, please specify the primary reason for rejection, choosing from the following categories:

1. `Inadequate Testing`: The PR lacks necessary tests or has insufficient test coverage.
2. `Quality Concerns`: The changes raise concerns regarding code quality.
3. `Functionality Issues`: The PR introduces bugs or breaks existing functionality.
4. `Design Incompatibility`: The proposed changes do not align with the project's design principles.
5. `Performance Regression`: The changes result in a degradation of performance.
6. `Security Vulnerabilities`: The PR introduces or does not adequately address security vulnerabilities.
7. `Lack of Documentation`: Necessary documentation updates are missing or incomplete.
8. `Conflict with Project Scope`: The changes are beyond the current project scope or goals.
9. `Coding Standards Violation`: The PR does not comply with the project's coding standards.
10. `Dependency Concerns`: The PR introduces compatibility issues, licensing conflicts, or security risks with dependencies.

## Questions or Suggestions

If you have any questions or suggestions about contributing to PullRequestBenchmark, please feel free to reach out. We're always looking to improve the process and make it easier for contributors to participate.

Thank you for contributing to the advancement of AI in software development practices!
