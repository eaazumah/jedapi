import uuid
import firebase_admin
from firebase_admin import firestore
from firebase_admin import storage
from jsonmodels import fields
from jsonmodels.models import Base, JsonmodelMeta
from .base import FirestoreORM


class Model(Base):
    """Firestore Models all inherit from jsonmodels.models.Base.\n
    This is exposed as `from firestore_orm import model`.

    Arguments:
        Base {:class:`jsonmodels.models.Base`} -- To create models you need to create class that inherits from :class:`jsonmodels.models.Base`.\n
        For more details, refer to https://jsonmodels.readthedocs.io/en/latest/usage.html.\n
        __tablename__ {str} -- Collection name of model in firestore
    Keyword Arguments:
        metaclass {:class:`firestore_orm.models.ModelMeta`} --  (default: {ModelMeta})

    """

    hidden_fields = ['password', 'is_deleted']
    __collection__ = None
    id = fields.StringField()
    created_at = fields.DateTimeField()
    modefied_at = fields.DateTimeField()

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)
        self.id = uuid.uuid4().__str__() if not self.id else self.id
        self.query = FirestoreORM(
            db=firestore.client(),
            bucket=storage.bucket(
                name=firebase_admin.get_app().options.get('storageBucket')),
        )

    def save(self):
        """Save model instance to firestore
        """
        self.query.commit(self.id, self)

    def to_dict(self, show=[], hide=[]) -> dict:
        """ Return a dictionary representation of this model.
        """
        hidden = []

        if hasattr(self, 'hidden_fields'):
            hidden = self.hidden_fields.copy()
            hidden.extend(hide)

        resp = {}
        for _, name, field in self.iterate_with_name():
            value = field.__get__(self)
            if name not in show and name in hidden:
                continue

            if value is None:
                resp[name] = None
                continue
            value = field.to_struct(value)
            resp[name] = value

        # jsonify relationships
        for key in self.show_relationships:
            val: Model = getattr(self, key)
            if not val or not isinstance(val, Base):
                continue
            resp[key] = val.to_dict()
        return resp
