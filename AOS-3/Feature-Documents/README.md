# AOS Feature Documents — delivery bundle

This directory contains a deterministic delivery bundle of **DRAFT** AOS feature documentation.

## Contents

After materialization, the bundle contains:

- 34 feature-family documents (`FTR-001..034`);
- 100 atomic-function documents (`IDEA-001..100`);
- indexes, manifest, checksums and validation report;
- 141 files in total.

All materials remain:

```yaml
status: DRAFT
authority: NONE
canonical_status: NOT_ASSIGNED
implementation_authorization: NONE
human_review_required: true
```

They do not modify or override canonical `docs/`.

## Why the archive is split

The deterministic `tar.xz` archive is base64-encoded and stored as 23 ordered parts under `archive-parts/` because the connected GitHub delivery interface has a bounded file-write payload.

The repository never treats archive presence as validation. The extractor verifies:

1. the exact part names `archive.part-00.b64..archive.part-22.b64`;
2. SHA-256 of their byte-exact concatenation;
3. SHA-256 of the decoded `tar.xz` archive;
4. absence of path traversal and archive links;
5. the expected extracted file count.

## Materialize the separate documents

From the repository root:

```bash
python3 AOS-3/Feature-Documents/extract_feature_documents.py
```

The command writes the separate Markdown files to:

```text
AOS-3/Feature-Documents/documents/
```

The extractor refuses to overwrite a non-empty `documents/` directory. Removal or replacement must be explicit.

## Digests

```text
concatenated base64 SHA-256:
d0315fd273e953e5043ec74b41ad499e5861ad875460e28df1f54c625ec9e73b

decoded tar.xz SHA-256:
0d85639e458366cd4290c3fa545a7573fc726c5e05b51fee30bc4a0f83ba2373
```

## Boundaries

This delivery:

- does not change `docs/`;
- does not approve any feature;
- does not authorize implementation;
- does not authorize merge, release or runtime execution;
- does not convert DRAFT material into Evidence or canonical knowledge.
