import sae
from house import app

application = sae.create_wsgi_app(app)