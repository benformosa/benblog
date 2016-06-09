#!/usr/bin/python2
from bottle import abort, route, run, template, static_file
import yaml, os, misaka

settings = {'blog_title': "Blog",
        'blog_author': "Blogger"}
try:
    with open('settings.yml', 'r') as stream:
        settings = yaml.load(stream)
except:
    print 'settings.yml not found, using defaults.'

@route('/')
@route('/article/<title>')
def article(title):
    article_path = os.path.join('./article', (title + '.md'))
    meta_path = os.path.join('./article_meta', (title + '.yml'))


    # if markdown file doesn't exist, return 404
    if(not os.path.isfile(article_path)):
        abort(404, "No such article.")

    # if yml file exists, parse it. otherwise use defaults
    if(os.path.isfile(meta_path)):
        with open(meta_path, 'r') as stream:
            try:
                meta = yaml.load(stream)
                article_title = meta['title']
            except yaml.YAMLError as e:
                abort(500, e)
    else:
        article_title = title

    with open(article_path, 'r') as stream:
        article = stream.read()
        return template('article', 
                blog_title=settings['blog_title'],
                blog_author=settings['blog_author'],
                article_title=article_title,
                article_markdown=misaka.html(article))

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./static')

run(host='localhost', port=8080, debug=True)
