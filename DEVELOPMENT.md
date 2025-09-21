# Development Guide

This guide is for developers who want to contribute to or modify the Simple Weather Card.

## Prerequisites

- Node.js 16+ (see `.nvmrc`)
- npm

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

## Development

### Build the card
```bash
npm run build
```

### Watch for changes
```bash
npm run watch
```

## Project Structure

```
simple-weather-card/
├── src/
│   ├── main.js          # Main card component
│   ├── weather.js       # Weather entity logic
│   ├── style.js         # CSS styles
│   └── handleClick.js   # Click handling
├── icons/               # Weather icons
├── simple-weather-card-bundle.js  # Built card (for HACS)
├── hacs.json           # HACS configuration
├── info.md             # HACS display info
└── README.md           # User documentation
```

## Building for Release

1. Update version in `package.json`
2. Run `npm run build`
3. The built file will be `simple-weather-card-bundle.js` in the root directory
4. Commit and tag the release

## HACS Compatibility

The repository is configured for HACS with:
- `hacs.json` - HACS metadata
- `info.md` - Card description and installation instructions
- Built bundle in root directory
- Proper file structure for HACS detection

## Testing

The card can be tested by:
1. Building the card (`npm run build`)
2. Placing `simple-weather-card-bundle.js` in Home Assistant's `config/www/` directory
3. Adding the resource to Lovelace configuration
4. Adding the card to a dashboard
