const path = require('path');

module.exports = {
  entry: './src/main.js',
  output: {
    filename: 'simple-weather-card-bundle.js',
    path: path.resolve(__dirname),
    clean: false,
  },
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.(png|svg)$/i,
        type: 'asset/inline',
        generator: {
          dataUrl: {
            encoding: 'base64',
            mimetype: 'image/png'
          }
        }
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.mjs'],
  },
  optimization: {
    minimize: true,
  },
};
