#!/usr/bin/env python

from flask import Flask
from flask import render_template
from jinja2.exceptions import TemplateNotFound
app = Flask(__name__)

@app.route('/')
@app.route('/<page>/')
def any_page(page='index'):
    try:
        return render_template(page + '.html')
    except TemplateNotFound:
        return render_template('404.html')

@app.route('/fablab/')
def fablabindex():
    return render_template('fablab/index.html')
@app.route('/fablab/charter/')
def fablabcharter():
    return render_template('fablab/charter.html')
@app.route('/fablab/network/')
def fablabnetwork():
    return render_template('fablab/network.html')
@app.route('/fablab/partners/')
def fablabpartners():
    return render_template('fablab/partners.html')
@app.route('/fablab/partnership/')
def fablabpartnership():
    return render_template('fablab/partnership.html')
@app.route('/fablab/wherefrom/')
def fablabwherefrom():
    return render_template('fablab/wherefrom.html')

@app.route('/equipment/')
def equipmentwherefrom():
    return render_template('equipment/index.html')
@app.route('/equipment/dimension-elite/')
def equipmentdimensionelite():
    return render_template('equipment/dimension-elite.html')
@app.route('/equipment/flexicam-stealth/')
def equipmentflexicamstealth():
    return render_template('equipment/flexicam-stealth.html')
@app.route('/equipment/laser-pro-spirit/')
def equipmentlaserprospirit():
    return render_template('equipment/laser-pro-spirit.html')
@app.route('/equipment/replicator/')
def equipmentreplicator():
    return render_template('equipment/replicator.html')
@app.route('/equipment/roland-gx300-gx24/')
def equipmentrolandgx300gx24():
    return render_template('equipment/roland-gx300-gx24.html')
@app.route('/equipment/roland-modella-mdx/')
def equipmentrolandmodellamdx():
    return render_template('equipment/roland-modella-mdx.html')

@app.route('/competition/')
def equipment():
    return render_template('competition/index.html')
@app.route('/competition/advice/')
def equipmentadvice():
    return render_template('competition/advice.html')
@app.route('/competition/ceremony/')
def equipmentceremony():
    return render_template('competition/ceremony.html')
@app.route('/competition/contacts/')
def equipmentcontacts():
    return render_template('competition/contacts.html')
@app.route('/competition/diploms/')
def equipmentdiploms():
    return render_template('competition/diploms.html')
@app.route('/competition/exp/')
def equipmentexp():
    return render_template('competition/exp.html')
@app.route('/competition/join/')
def equipmentjoin():
    return render_template('competition/join.html')
@app.route('/competition/list/')
def equipmentlist():
    return render_template('competition/list.html')
@app.route('/competition/news/')
def equipmentnews():
    return render_template('competition/news.html')
@app.route('/competition/official/')
def equipmentofficial():
    return render_template('competition/official.html')
@app.route('/competition/org/')
def equipmentorg():
    return render_template('competition/org.html')
@app.route('/competition/partners/')
def equipmentpartners():
    return render_template('competition/partners.html')
@app.route('/competition/projects/')
def equipmentprojects():
    return render_template('competition/projects.html')
@app.route('/competition/rules/')
def equipmentrules():
    return render_template('competition/rules.html')
@app.route('/competition/winners/')
def equipmentwinners():
    return render_template('competition/winners.html')
# @app.route('/fablab/<path>')
# def fablab(code):
#     # fablab = Fablab.query.filter_by(code=code).first()
#     return render_template('/fablab/' + code + '.html')




# # flask-sqlalchemy model for User
# class User(db.Model, UserMixin):

#     __tablename__ = 'users'

#     id = Column(db.Integer, primary_key=True)
#     name = Column(db.String(32), nullable=False, unique=True)
#     email = Column(db.String, nullable=False, unique=True)
#     activation_key = Column(db.String)
#     created_time = Column(db.DateTime, default=get_current_time)
#     modified_time = Column(db.TIMESTAMP, onupdate=get_current_time(), default=get_current_time())


# # a route for generating sitemap.xml
# @frontend.route('/sitemap.xml', methods=['GET'])
# def sitemap():
#       """Generate sitemap.xml. Makes a list of urls and date modified."""
#       pages=[]
#       ten_days_ago=datetime.now() - timedelta(days=10).date().isoformat()
#       # static pages
#       for rule in current_app.url_map.iter_rules():
#           if "GET" in rule.methods and len(rule.arguments)==0:
#               pages.append(
#                            [rule.rule,ten_days_ago]
#                            )
      
#       # user model pages
#       users=User.query.order_by(User.modified_time).all()
#       for user in users:
#           url=url_for('user.pub',name=user.name)
#           modified_time=user.modified_time.date().isoformat()
#           pages.append([url,modified_time]) 

#       sitemap_xml = render_template('frontend/sitemap_template.xml', pages=pages)
#       response= make_response(sitemap_xml)
#       response.headers["Content-Type"] = "application/xml"    
    
#       return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
