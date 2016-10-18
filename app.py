import memcache
import json
import requests

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.contrib.cache import SimpleCache, MemcachedCache
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key = 'h!t$v)bv5o7&p)7@vzyb)*w^w1&i#51qjtmrs2kormgvj&dnbe'
Bootstrap(app)
#cache = SimpleCache()
cache = MemcachedCache(['memcache:11211'], 60*60)

class DiceSearchForm(FlaskForm):
    '''Search Form'''
    search_text = StringField('Find a Job', validators=[DataRequired()])


def get_count(text, city):
    url = 'http://service.dice.com/api/rest/jobsearch/v1/simple.json?text={}&city={}'
    city = city.replace(',', '').replace(' ', '+').lower()
    text = text.replace(',', '').replace(' ', '+').lower()

    count = cache.get('count'+city+text)
    if count:
        print('cache for {}'.format(city))
        jobs = cache.get('jobs'+city+text)
        return (count, json.loads(jobs))
    resp = requests.get(url.format(text, city)).json()
    cache.set('count'+city+text, resp['count'])
    jobs = resp['resultItemList'][:3]
    cache.set('jobs'+city+text, json.dumps(jobs))
    print(url.format(text, city))
    return (resp['count'], jobs)


@app.route('/', methods=('GET', 'POST'))
def index():
    cities = ['Los Angeles, CA',
              'Denver, CO',
              'San Jose, CA',
              'New York, NY',
              'Austin, TX',
              'Minneapolis, MN',
              'Portland, OR',
              'Atlanta, GA'
             ]
    text = 'linux'

    form = DiceSearchForm()
    if form.validate_on_submit():
        text = form.search_text.data
        if request.form.get('city0'):
            cities = [city for key, city in request.form.items() if key.startswith('city')]
            print(cities)
        print(text)
    city_count = [(city, get_count(text, city)) for city in cities]
    city_count = sorted(city_count, key=lambda x: x[1][0], reverse=True)
#    print(city_count)
    return render_template('index.html', city_count=city_count, form=form, text=text)

if __name__ == '__main__':
    app.run()
