from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return """ 
            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>NOC Status Dashboard</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            text-align: center;
                            margin-top: 100px;
                            background-color: #f4f4f4;
                        }
                        h1 {
                            color: #333;
                            font-size: 2.5rem;
                        }
                    </style>
                </head>
                <body>
                    <h1>NOC Status Dashboard - Coming Soon</h1>
                    <p>This dashboard is under development.</p>
                </body>
                </html>
            """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
