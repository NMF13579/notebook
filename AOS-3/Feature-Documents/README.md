# AOS Feature Documents — delivery bundle

This directory contains a deterministic, compressed delivery of the DRAFT feature documentation package.

## Materialize documents

```bash
python3 extract_feature_documents.py
```

The command verifies SHA-256, rejects unsafe archive paths and writes the separate Markdown documents into `documents/`.

## Package contents

- 34 feature-family documents (`FTR-001..034`)
- 100 atomic-function documents (`IDEA-001..100`)
- indexes, manifest, checksums and validation report
- all artifacts remain `DRAFT`, `authority: NONE`

## Boundaries

This package does not modify canonical `docs/`, does not authorize implementation and does not imply human acceptance.

Archive SHA-256: `0d85639e458366cd4290c3fa545a7573fc726c5e05b51fee30bc4a0f83ba2373`
