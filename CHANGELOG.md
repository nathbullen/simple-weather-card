# Changelog

## [0.9.0] - 2024-12-19

### Fixed
- **BREAKING**: Updated to Lit 3.x for compatibility with modern Home Assistant frontend
- Fixed "TypeError: e is not a function" error in newer Home Assistant versions
- Fixed "e.constructor.createProperty is not a function" decorator compatibility issue
- Fixed "custom element does not exist" error by removing problematic decorators
- Updated build system to Webpack 5 and Babel 7.23+
- Modernized ES6 module imports and property definitions

### Changed
- Upgraded from Lit 2.2.3 to Lit 3.1.0
- Updated Webpack from 4.x to 5.x
- Updated Babel configuration for better compatibility
- Improved build output with modern asset handling

### Technical Details
- Replaced dynamic LitElement detection with direct imports
- Updated property decorators to use modern Lit 3 syntax
- Fixed webpack configuration for better tree shaking and optimization
- Updated all dependencies to latest compatible versions

### Migration Notes
- This version requires Home Assistant 2023.1.0 or later
- The card should now work without the "TypeError: e is not a function" error
- No configuration changes required - existing configurations will continue to work
