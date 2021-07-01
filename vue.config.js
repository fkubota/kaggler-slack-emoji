module.exports = {
  "outputDir": "docs",
  "assetsDir": "./",
  "publicPath": "./",
  "transpileDependencies": [
    "vuetify"
  ],
  
  pages: {
    index: {
      entry: 'src/main.js', // 必須パラメータ
      title: 'kaggler-slack-emoji',
      template: 'public/index.html'
    }
  },
}
