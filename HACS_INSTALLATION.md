# HACS Installation Guide

This guide will help you install the Simple Weather Card through HACS (Home Assistant Community Store).

## Prerequisites

- Home Assistant 2023.1.0 or later
- HACS installed and configured
- Lovelace UI enabled

## Installation Steps

### 1. Open HACS

1. In your Home Assistant instance, go to **HACS** in the sidebar
2. Click on **Frontend** in the HACS interface

### 2. Add Custom Repository

1. Click the **three dots** (⋮) in the top right corner
2. Select **Custom repositories**
3. In the **Repository** field, enter: `https://github.com/kalkih/simple-weather-card`
4. In the **Category** dropdown, select **Lovelace**
5. Click **Add**

### 3. Install the Card

1. Find **Simple Weather Card** in the list of available cards
2. Click on **Simple Weather Card**
3. Click the **Install** button
4. Wait for the installation to complete

### 4. Restart Home Assistant

1. Go to **Settings** → **System** → **Restart**
2. Click **Restart** to restart Home Assistant

### 5. Add the Card to Your Dashboard

1. Go to your **Dashboard**
2. Click the **three dots** (⋮) in the top right
3. Select **Edit Dashboard**
4. Click the **+** button to add a card
5. Search for **Simple Weather Card** or select it from the list
6. Configure the card with your weather entity

## Configuration Example

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

## Updating the Card

HACS will automatically notify you when updates are available:

1. Go to **HACS** → **Frontend**
2. Find **Simple Weather Card** in the list
3. If an update is available, you'll see an **Update** button
4. Click **Update** to install the latest version
5. Restart Home Assistant

## Troubleshooting

### Card Not Appearing

- Make sure you've restarted Home Assistant after installation
- Check that you have a weather entity configured in Home Assistant
- Verify the card is properly added to your Lovelace configuration

### Card Not Loading

- Check the browser console for errors
- Ensure your Home Assistant version is 2023.1.0 or later
- Try clearing your browser cache

### Configuration Issues

- Verify your weather entity exists: `weather.home` (replace with your actual entity)
- Check the YAML syntax in your card configuration
- Ensure all required fields are present

## Support

If you encounter any issues:

1. Check the [GitHub Issues](https://github.com/kalkih/simple-weather-card/issues)
2. Ask for help in the [Home Assistant Community](https://community.home-assistant.io/)
3. Make sure you're using the latest version of the card

## Manual Installation (Alternative)

If you prefer not to use HACS, you can install the card manually:

1. Download `simple-weather-card-bundle.js` from the [latest release](https://github.com/kalkih/simple-weather-card/releases/latest)
2. Place it in your `config/www/` directory
3. Add the resource to your Lovelace configuration:

```yaml
resources:
  - url: /local/simple-weather-card-bundle.js?v=0.9.0
    type: module
```
