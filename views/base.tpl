<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="/static/benblog.css" type="text/css">
  <title>{{blog_title}}</title>
</head>
<body>
  <header>
    <h1>{{blog_title}}</h1>
    <p><em>A cool blog by {{blog_author}}</em></p>
  </header>
  <nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
  </nav>
  {{!base}}
  <footer>
    <p>© {{current_year}} {{blog_author}}</p>
    <p>Powered by BenBlog</p>
  </footer>
</body>
</html>
