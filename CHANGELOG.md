# Changelog

## [0.9.0] - 2024-12-19

### Fixed
- **BREAKING**: Simplified to use Lit 2.8.0 directly for maximum compatibility
- Fixed "TypeError: e is not a function" error in newer Home Assistant versions
- Fixed "e.constructor.createProperty is not a function" decorator compatibility issue
- Fixed "custom element does not exist" error by removing complex detection logic
- Fixed "customElements.entries is not a function" error for older browser compatibility
- Removed all complex LitElement detection and fallback logic
- Updated build system to Webpack 5 and Babel 7.23+
- Simplified to standard Lit 2 patterns without decorators

### Changed
- Uses Lit 2.8.0 directly for stable web component support
- Updated Webpack from 4.x to 5.x
- Updated Babel configuration for better compatibility
- Simplified build process by removing decorator dependencies
- Improved build output with modern asset handling
- Removed all test files and unnecessary documentation

### Technical Details
- Uses Lit 2.8.0 directly for maximum compatibility
- Removed all decorator usage to prevent transpilation issues
- Fixed webpack configuration for better tree shaking and optimization
- Updated all dependencies to latest compatible versions
- Simplified architecture to standard Lit 2 patterns

### Migration Notes
- This version requires Home Assistant 2023.1.0 or later
- The card should now work without the "TypeError: e is not a function" error
- No configuration changes required - existing configurations will continue to work
