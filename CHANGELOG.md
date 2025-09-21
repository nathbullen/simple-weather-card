# Changelog

## [0.9.0] - 2024-12-19

### Fixed
- **BREAKING**: Reverted to Home Assistant's native LitElement detection for maximum compatibility
- Fixed "TypeError: e is not a function" error in newer Home Assistant versions
- Fixed "e.constructor.createProperty is not a function" decorator compatibility issue
- Fixed "custom element does not exist" error by using Home Assistant's LitElement
- Fixed "customElements.entries is not a function" error for older browser compatibility
- Removed external Lit dependency to prevent version conflicts
- Updated build system to Webpack 5 and Babel 7.23+
- Simplified property definitions for better compatibility

### Changed
- Removed external Lit dependency - now uses Home Assistant's native LitElement
- Updated Webpack from 4.x to 5.x
- Updated Babel configuration for better compatibility
- Simplified build process by removing decorator dependencies
- Improved build output with modern asset handling

### Technical Details
- Uses Home Assistant's native LitElement detection for maximum compatibility
- Removed all decorator usage to prevent transpilation issues
- Fixed webpack configuration for better tree shaking and optimization
- Updated all dependencies to latest compatible versions
- Eliminated external Lit dependency to prevent version conflicts

### Migration Notes
- This version requires Home Assistant 2023.1.0 or later
- The card should now work without the "TypeError: e is not a function" error
- No configuration changes required - existing configurations will continue to work
