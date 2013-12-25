from filters import datefilter
import jinja2, os

jj2 = jinja2.Environment(
    loader=jinja2.FileSystemLoader('%s/../../views' % os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
jj2.filters['date'] =  datefilter
