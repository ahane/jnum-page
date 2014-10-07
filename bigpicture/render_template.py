# coding: utf-8

import jinja2 as ji
strings = {'portfolio': 'Portfolio'}
t = ji.Template("{{ portfolio }} hello)
t = ji.Template("{{ portfolio }} hello")
t.render(strings)
with open('index-temp.html' as f):
    template = ji.Template(f.read())
with open('index-temp.html', 'r') as f:
    template = ji.Template(f.read())
with open('index.html', 'r') as f:
    template = ji.Template(f.read())
english_strings = {'portfolio': 'Portfolio'}
with open('index-en.html', 'w') as f:
    f.write(template.render(english_strings))
with open('index-de.html', 'w') as f:
    f.write(template.render(german_strings))
german_strings = {'portfolio': 'werke'}
english_strings = {'portfolio': 'Portfolio'}
with open('index-en.html', 'w') as f:
    f.write(template.render(english_strings))
with open('index-de.html', 'w') as f:
    f.write(template.render(german_strings))
with open('index-template.html', 'r') as f:
    template = ji.Template(f.read())
german_strings = {'portfolio': 'werke'}
english_strings = {'portfolio': 'Portfolio'}
with open('index-en.html', 'w') as f:
    f.write(template.render(english_strings))
with open('index-de.html', 'w') as f:
    f.write(template.render(german_strings))
get_ipython().magic(u'save render_template')
get_ipython().magic(u'save render_template')
get_ipython().magic(u'save render_template *')
