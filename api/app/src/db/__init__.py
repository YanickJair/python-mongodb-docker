import mongoengine

def global_init():
    mongoengine.connect(alias='core', name='oculyze_ch', host='mongodb://root:oculyze@mongodb:27017/?authSource=admin')


class Output(mongoengine.Document):
    text = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'outputs'
    }