# options-decoding-api
Since options naming is weird...

## Usage
Basic usage notes, for more in-depth version check out [api.json](./api.json).

### /health-check
Verifies API is active and functioning. Should always response `alive`.

### /decode-option
Decode option from standard naming convention to JSON data. For example:

POST:
```json
{
  "option": "AAPL150416C00031420"
}
```

Response:
```json
{
  "symbol": "AAPL",
  "company_name": "Apple",
  "year": 2015,
  "month": 4,
  "day": 16,
  "option_type": "call",
  "price": 31.42
}
```