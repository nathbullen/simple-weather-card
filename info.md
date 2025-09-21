# Simple Weather Card

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/kalkih/simple-weather-card.svg)](https://github.com/kalkih/simple-weather-card/releases/latest)
[![GitHub stars](https://img.shields.io/github/stars/kalkih/simple-weather-card.svg)](https://github.com/kalkih/simple-weather-card/stargazers)

A minimalistic weather card for [Home Assistant](https://github.com/home-assistant/home-assistant) Lovelace UI, inspired by Google Material Design.

![Preview](https://user-images.githubusercontent.com/457678/53588519-61dfdf80-3b8d-11e9-9f0d-f5995ba794ce.png)

## Features

- **Minimalistic & compact design** - Clean, uncluttered interface
- **Custom day/night backgrounds** - Automatic theme switching based on sun position
- **Clean weather icons** - Material Design inspired weather icons
- **Customizable information** - Wind speed, precipitation, humidity, pressure, and more
- **Responsive design** - Works on all screen sizes
- **Easy configuration** - Simple YAML configuration
- **HACS compatible** - Easy installation and updates

## Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to Frontend
3. Click the three dots in the top right
4. Select "Custom repositories"
5. Add this repository URL: `https://github.com/kalkih/simple-weather-card`
6. Select "Lovelace" as the category
7. Click "Add"
8. Find "Simple Weather Card" in the list and click "Install"

### Manual Installation

1. Download `simple-weather-card-bundle.js` from the [latest release](https://github.com/kalkih/simple-weather-card/releases/latest)
2. Place the file in your `config/www/` directory
3. Add the resource to your Lovelace configuration:

```yaml
resources:
  - url: /local/simple-weather-card-bundle.js?v=0.9.0
    type: module
```

## Configuration

Add the card to your Lovelace dashboard:

```yaml
type: custom:simple-weather-card
entity: weather.home
name: "Home Weather"
primary_info: ["extrema"]
secondary_info: ["precipitation", "humidity"]
backdrop:
  day: "#45aaf2"
  night: "#a55eea"
  text: "#ffffff"
```

## Requirements

- Home Assistant 2023.1.0 or later
- Lovelace UI

## Support

- [GitHub Issues](https://github.com/kalkih/simple-weather-card/issues)
- [Home Assistant Community](https://community.home-assistant.io/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.