---
name: Content improvement
description: Suggest improvements to an existing document
title: "[Improve] "
labels: [improvement]
body:
  - type: input
    id: file
    attributes:
      label: Document path
      description: e.g. docs/study-materials/ai-infra/04-llm-inference.md
    validations:
      required: true
  - type: textarea
    id: issue
    attributes:
      label: What should be improved?
      description: Is it outdated, missing context, lacking project, duplicated, or unclear?
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed change
      description: Provide concrete additions, removals, or restructuring suggestions.
