# Contributing to EVORAO

Thank you for your interest in contributing to the **EVORA Ontology (EVORAO)**! Contributions are welcome from both **scientific** and **development** perspectives. Please follow the guidelines below to ensure a smooth contribution process.

---

## How to Contribute

### 1. Scientific Contributions

Experts in virology and metadata management can propose:

- New terms, relationships, and refinements to the ontology.
- Restructuring of parent classes or metadata concepts for better domain representation.

#### Contribution Process:

1. **Review** the current EVORAO terms from the [Google Sheet](https://docs.google.com/spreadsheets/d/1zcyNKuhkpH-0FqEGSt6UwHAiSYzsUUSkHYcDOYz67zI) or the [generated documentation](https://github.com/EVORA-project/evora-ontology/blob/main/models/docs/index.md).  
2. **[Open a GitHub Issue](https://github.com/EVORA-project/evora-ontology/issues)**, providing the following details for new terms:
   - Purpose and justification.
   - Term name (following [EVORAO naming conventions](#evorao-naming-conventions-and-best-practices)).
   - Human-readable label/title.
   - Precise definition of the term.  
3. **Discuss** your proposal with the community and ontology maintainers.
4. Upon agreement, maintainers will incorporate the approved suggestions into the Google Sheet and trigger the CI pipeline.

---

### 2. Development Contributions

Developers can contribute by improving:
#### On this repository
- The code used for the Ontology generation pipelines ([/.Github](https://github.com/EVORA-project/evora-ontology/tree/main/.github/workflows) and [/Gscript](https://github.com/EVORA-project/evora-ontology/tree/main/Gscript)).
- Documentation in the README.md and this CONTRIBUTING.md

 #### On the repository of used tools
 More precisely the metadata processing programs used are Schemasheets, LinkML.
 Contribution to those tools will impact this repository on inclusion of the updated version in our process and triggering of our CI pipeline
 Fork the corresponding repository and make a pull request:
 - [Schemasheets Github repo](https://github.com/linkml/schemasheets)
 - [LinkML Github repo](https://github.com/linkml/linkml)

 
#### Contribution Process on this repository:

1. **[Create an issue](https://github.com/EVORA-project/evora-ontology/issues)** in the repository detailing the observed issue or enhancement.  
2. **Assign the issue** to yourself.  
3. **Fork the repository** and create a feature branch.  
4. **Implement the changes** and submit a pull request (PR).  

All PRs must include the following header:

```markdown
| Q             | A
| ------------- | ---
| Bug fix?      | yes/no
| New feature?  | yes/no
| Deprecations? | no
| Fixed tickets | #1234, #5678
```

#### Squashing Your Commits

Before submitting, squash your commits to maintain a clean history.

```bash
git rebase -i HEAD~3
```

In the interactive editor, replace pick with fixup (or f) for all commits except the first.

To amend the commit message, use:

```bash
git commit --amend
```

Finally, force push your branch to update the PR:

```bash
git push --force
```

## EVORAO Naming Conventions and best practices

Following these conventions ensures consistency, readability, and adherence to FAIR principles:

- 1. **Classes**:

  - Follow `CamelCase` with an **uppercase initial letter** (e.g., VirusStrain).
  - Each class should include a descriptive label and definition.
  - Check existing vocabularies and standards to provide exact or close mapping with existing terms

- 2 **Properties**:

  - Use `camelCase` with a **lowercase initial letter** (e.g., collectionDate).
  - Check existing vocabularies and standards to provide exact or close mapping with existing terms
  - Ensure clear descriptions and specify expected data types (e.g., string, integer, boolean).
  - Determine whether the property should reference another class or use a standard datatype.
  - Discuss potential restrictions such as default values and cardinality.


# License and copyright attribution

By submitting a pull request, you agree to license your contributions under the **Creative Commons Universal (CC0 1.0)** license, which governs the entire EVORAO repository.
