#!/usr/bin/python2
from bottle import abort, route, request, run, template, static_file
import yaml, os, misaka

SETTINGS = {
        'blog_title': "Blog",
        'blog_author': "Blogger"
        }
try:
    with open('settings.yml', 'r') as stream:
        SETTINGS = yaml.load(stream)
except:
    print 'settings.yml not found, using defaults.'

@route('/')
def home():
    """Display links to recent articles.

    If specified, only show articles with all specified tags."""
    tags = request.query.tags
    return template('home', tags=tags)

@route('/article/<title>')
def article(title):
    """Display an article."""

    article_path = os.path.join('./article', (title + '.md'))
    meta_path = os.path.join('./article_meta', (title + '.yml'))

    # if markdown file doesn't exist, return 404
    if not os.path.isfile(article_path):
        abort(404, "No such article.")

    meta = {'title': title}
    # if yml file exists, parse it. otherwise use defaults
    # ideally, defaults should be used on a per-value basis
    if os.path.isfile(meta_path):
        with open(meta_path, 'r') as stream:
            try:
                meta = yaml.load(stream)
            except yaml.YAMLError as ex:
                abort(500, ex)

    with open(article_path, 'r') as stream:
        article_body = stream.read()

        # merge the meta, SETTINGS and content together into one dict
        article_content = meta.copy()
        article_content.update(SETTINGS)
        article_content['markdown'] = misaka.html(article_body)
        return template('article', article_content)

@route('/static/<filepath:path>')
def server_static(filepath):
    """Serve a static file from the ./static directory"""
    return static_file(filepath, root='./static')

@route('/favicon.ico')
def favicon():
    """Serve the favicon"""
    return static_file('favicon.ico', root='./static')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
