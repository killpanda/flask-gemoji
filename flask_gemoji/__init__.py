import os
import pkg_resources

from flask import Blueprint, url_for, current_app

names = None

def gemoji_filter(s, height='auto'):
    if names is None:
        raise Exception("Must first call init_gemoji")
    splits = s.split(':')
    splits_len = len(splits)
    out = ''
    for i, w in enumerate(splits):
        if w in names:
            out = out[:-1]
            out += '<img src="%s" alt="%s" class="%s" height="%s">' % (
                url_for('gemoji.static',
                        filename='images/emoji/%s.png' % w),
                w,
                current_app.config['GEMOJI_CLASS'],
                height,
            )
        elif i + 1 < splits_len:
            out += w + ':'
        else:
            out += w
    return out

def init_gemoji(app):
    app.config.setdefault('GEMOJI_CLASS', 'gemoji')
    gemoji_images_path = (pkg_resources
        .resource_filename(__package__, 'static/images/emoji'))
    names = map(lambda s: os.path.splitext(s)[0],
                filter(lambda s: s.endswith('.png'),
                       os.listdir(gemoji_images_path)))
    gemoji = Blueprint('gemoji', __name__, static_folder='static')
    app.register_blueprint(gemoji, url_prefix='/gemoji')
    app.jinja_env.filters['gemoji'] = gemoji_filter

