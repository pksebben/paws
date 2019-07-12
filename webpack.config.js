const path = require("path");
const HtmlWebPackPlugin = require("html-webpack-plugin");
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const TodoWebpackPlugin = require("todo-webpack-plugin");

//plugins
const htmlPlugin =  new HtmlWebPackPlugin({
    hash: true,
    filename: "index.html",  //target html
    template: "./frontend/public/index.html" //source html
});

const etPlugin =  new ExtractTextPlugin({ filename: 'css/style.css' });

const todoWebpackPlugin = new TodoWebpackPlugin({
    console:true,
    tags:['TODO','BUSTED','KIRBY','IAN','BEN','WTF','GOOGLE']
});

module.exports = {
    context: path.resolve(__dirname,''),
    devtool: 'eval-source-map',
    devServer: {
	open: true,
	// contentBase: './dist'
    },
    entry: ["./frontend/index.jsx"],
    output: {
        path: path.resolve(__dirname, "./dist"),
        filename: "[name].bundle.js",
	chunkFilename: "[name].bundle.js",
	publicPath: "/"
    },
    module: {
        rules: [{
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/preset-react']
                }
            }
        }, {
            test: /\.css$/,
            use: ExtractTextPlugin.extract(
                {
                    fallback: 'style-loader',
                    use: ['css-loader']
                }
            )
        },
        {
            test: /\.(png|jpg|gif)$/,
            use: [
                {
                    loader: 'file-loader'
                }
            ]
        }
        ]
    },

    plugins: [ htmlPlugin, etPlugin, todoWebpackPlugin ]

}


