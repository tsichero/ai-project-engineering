# ADR-001 — RAG versus Fine-Tuning

## Status

Accepted for the initial architecture.

## Decision

Use retrieval-augmented generation as the first architecture for knowledge-grounded use cases.

## Rationale

RAG keeps external knowledge in a retrievable data layer, making updates and inspection easier without retraining the model.

Fine-tuning may be evaluated later when the requirement is behavior or style adaptation rather than knowledge injection.

## Consequence

The system must evaluate retrieval quality separately from generation quality.
