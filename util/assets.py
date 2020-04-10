from flask_assets import Bundle, Environment
from flask import Flask
from main import app

bundles = {
    'all_css': Bundle(
        'scss/vendor/reset.scss',
        'scss/styles.scss',
        filters='pyscss, cssmin',        
        output='minified/styles.min.css'),

    'all_js': Bundle(
        'js/vendor/jquery-3.4.1.js',
        'js/vendor/anime.min.js',
        'js/game-frontend.js',
        filters='jsmin',
        output='minified/script.min.js')
}

assets = Environment(app)
assets.register(bundles)