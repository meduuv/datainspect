# DataInspect

> Understand structured data quickly from the command line.

DataInspect is a dependency-free CLI for exploring structured tabular data without modifying the source files.

## Highlights

- CSV and delimited-text inspection
- Column and row summaries
- Basic type inference
- Missing-value counts
- Human-readable diagnostics
- JSON output for automation

## Usage

```bash
datainspect data.csv
datainspect data.csv --json
datainspect data.csv --columns
```

## Workflow

```text
data file
   ↓
parse structure
   ↓
profile columns
   ↓
summary / JSON
```

## Use Cases

- Dataset exploration
- Quick CSV diagnostics
- Data-cleaning preparation
- Developer tooling
- Lightweight automation

DataInspect does not modify the source dataset during inspection.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
