var path = require("path")
var webpack = require("webpack")
module.exports = {
	context: __dirname,
	mode: "development",
	entry: {
		index: "./files/logic/js/index.js"
	},
	output: {
		path: path.resolve("./bundles"),
		filename: "[name].js",
	},
	plugins: [],
	module: {
		rules: [			{
				test: /\.jsx?$/,
				exclude: /(node_modules|bower_components)/,
				use: {
					loader: "babel-loader",
					options: {
						presets: ["@babel/preset-env", "@babel/preset-react"]
					}
				}
			},
			{
				test: /\.css$/,
				loader: "style-loader!css-loader"
			},
			{
				test: /\.png$/,
				loader: "url-loader?limit=100000"
			},
			{
				test: /\.jpg$/,
				loader: "url-loader?limit=100000"
			},
			{
				test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
				loader: "url-loader?limit=100000"
			},
			{
				test: /\.tff(\?v=\d+\.\d+\.\d+)?$/,
				loader: "url?limit=10000&mimetype=application/octet-stream"
			},
			{
				test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
				loader: "file"
			},
			{
				test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
				loader: "url?limit=10000&mimetype=image/svg+xml"
			},
		]
	},
	resolve: {
		modules: ["node_modules"],
		extensions: [".js", ".jsx"]
	}
}
