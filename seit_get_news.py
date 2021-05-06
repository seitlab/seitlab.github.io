import re, random
import pymysql, datetime
from pymysql.converters import escape_string

class CTI_DB(object):
    def __init__(self, tableName):
        self.tableName = tableName

    def connection(self):
        try:
            db=pymysql.connect(host='cti.ckhlebdeaf8u.us-east-1.rds.amazonaws.com', user='seit', password='cti_seit666', database='ThreatIntelligence', charset='utf8mb4')
        except Exception as e:
            print("Connection to database failed!")
        return db

    def get_news(self, db):
        cursor = db.cursor()
        sql = "select * from ThreatIntelligence.cti_cps where `publishdate` regexp '.*(April|May).*2021'"
        cursor.execute(sql)
        fit_tuple=cursor.fetchall()
        return random.choice(fit_tuple)


if __name__ == '__main__':
    source = CTI_DB('cti_cps')
    db=source.connection()
    item = source.get_news(db)
    image_name = random.choice(['blockchain.jpg', 'smartphone.jpg', 'security.jpg', 'smarthome.jpg'])
    html_link = item[-1]
    html_title = item[2]
    html_author = item[3]
    html_date = item[4]
    if html_author == 'none':
        html_author = 'Anonymous'
    html_string = '<div class="feature_article_img"><img class="img-responsive top_static_article_img" src="assets/img/'+image_name + '" alt="feature-top"> </div> <div class="feature_article_inner"> <div class="tag_lg red">Hot Threat News</div> <div class="feature_article_title"> <h1><a href='+ html_link+ ' target="_self"> ' + html_title + ' </a></h1> </div> <div class="feature_article_date"><a href="#" target="_self"> '+ html_author +' </a>,<a href="#" target="_self"> '+ html_date + ' </a> </div> </div>'
    with open('./data/sub_postshow.txt', 'w') as f:
        f.write(html_string)
