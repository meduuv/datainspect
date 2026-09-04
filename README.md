# DataInspect

A dependency-free CLI for exploring structured tabular data without modifying the source files.

## Features

- CSV inspection
- Column and row summaries
- Type inference
- Missing-value counts
- Delimited text statistics
- JSON output for automation

## Usage

```bash
datainspect data.csv
datainspect data.csv --json
datainspect data.csv --columns
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

Built by Medu: https://guns.lol/meduu
