from flask import Flask, render_template

app = Flask(__name__)

posts = [
  {
      'title': 'Go beats Rust',
      'author': 'Todd McLeod',
      'content': "Google's own languge or Golang beats Rust",
      'image_url': "static/images/gopher.png",
      'posted_at': "02 February, 2020 08:00",
  },
  {
      'title': 'Will Google Stadia take over the gaming world?',
      'author': 'Tyler McGregor',
      'content': "Google's cloud gaming platform 'Stadia' set to take over the world of gaming",
      'image_url': "static/images/stadia.jpg",
      'posted_at': '02 February, 2020 11:00',
  },
]

@app.route('/')
def index():
  return render_template('home.html', posts=posts)


@app.route('/about')
def about():
  return render_template('about.html', title='About')


if __name__ == '__main__':
  app.run(debug=True)

