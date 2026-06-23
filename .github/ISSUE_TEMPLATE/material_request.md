---
name: Material request
description: Suggest a course, paper, system, benchmark, or project to add
title: "[Material] "
labels: [material]
body:
  - type: input
    id: name
    attributes:
      label: Material name
      description: Name of the course, paper, system, benchmark, or project.
    validations:
      required: true
  - type: textarea
    id: why
    attributes:
      label: Why is it important?
      description: Explain the problem it solves, why it is classic/frontier, and who should read it.
    validations:
      required: true
  - type: input
    id: link
    attributes:
      label: Official link
      description: Prefer arXiv, official repo, official blog, or course homepage.
  - type: dropdown
    id: area
    attributes:
      label: Area
      options:
        - Foundation Models
        - RAG / Retrieval
        - Multimodal
        - AI Infra
        - Agent Engineering
        - Reinforcement Learning
        - Generative Models
        - Computer Science
        - Evaluation
        - Other
    validations:
      required: true
  - type: textarea
    id: placement
    attributes:
      label: Suggested placement
      description: Which document should be the main source of truth?
