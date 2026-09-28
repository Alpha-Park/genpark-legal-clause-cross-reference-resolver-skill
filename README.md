# genpark-clause-references

Extract English defined terms and explicit numbered references from supplied contract text; inspect dependency cycles. Regex heuristics, not legal analysis.

Python 3.9+; standard library runtime; MIT license.

## Install and run

Download `genpark-clause-references.mcpb` from [GitHub Releases](https://github.com/Alpha-Park/genpark-legal-clause-cross-reference-resolver-skill/releases/tag/v1.0.1) and install with an MCPB-compatible client. Python must be installed and available as `python`.

Alternatively clone this repository and configure an MCP stdio server with command `python` and arguments containing the absolute path to `mcp_server.py`.

[Smithery listing](https://smithery.ai/servers/krispang1020/genpark-clause-references)

## Tools

- `extract_defined_terms`
- `map_clause_dependencies`
- `detect_circular_references`
- `resolve_and_expand_clause`
- `run_benchmark_legal_resolution`

Run `python -m unittest discover -s tests` for regression checks. The official MCP SDK integration check uses the development dependency `mcp`: `python tests/check_mcp.py`.

## Limitations

These are deterministic helpers operating on supplied structured data, not machine-learning models. Input and output remain in the local process. No hosted endpoint, automatic file access or network access is required. State lasts only for the current process. Benchmark tools run synthetic examples in isolated state; their status is not a production-quality certification.

Use canonical `Section N` clause keys. References named Clause, Article or Paragraph are normalized to Section. The graph reports DFS back-edge cycles, not an exhaustive enumeration; defined terms use quoted English phrases.
