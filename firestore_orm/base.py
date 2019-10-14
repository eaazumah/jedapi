__author__ = 'Benjamin Arko Afrasah'

from datetime import datetime
from google.cloud import firestore
from google.cloud.firestore_v1beta1 import CollectionReference, DocumentReference, DocumentSnapshot
from typing import TYPE_CHECKING
from typing import List, Tuple, Any

if TYPE_CHECKING:
    from google.cloud.firestore import Client
    from google.cloud.storage import Bucket
    from .model import Model


class FirestoreORM:
    """Base class for handling firestore operations
    """
    db = None
    bucket = None

    def __init__(self, db: 'Client' = None, bucket: 'Bucket' = None) -> None:
        """Constructor for the Firestore ORM query

        Keyword Arguments:
            db {:class:`google.cloud.firestore.Client`} -- Firestore client (default: {None})

            bucket {:class: `google.cloud.storage.Bucket`} -- Firebase storage bucket url (default: {None})
        """

        self.db = db
        self.bucket = bucket

    def _get_ref(self, model: 'Model') -> 'CollectionReference':
        """Get document ref

        Returns:
            :class: `google.cloud.firestore_v1beta1.CollectionReference` -- firestore collection object
        """

        return self.db.collection(model.__tablename__)

    def _get_document(self, id: str, model: 'Model') -> 'DocumentReference':
        """Get Document by id

        Returns:
            :class: `google.cloud.firestore_v1beta1.DocumentReference` -- Firestore document object
        """

        return self._get_ref(model).document(id)

    def commit(self, id: str, model: 'Model') -> None:
        """Save data to firestore

        Arguments:
            id {str} -- model id

            model {:class: `firestore_orm.model.Model`} -- ORM model
        """

        model.created_at = datetime.utcnow()
        model.validate()
        doc_ref = self._get_document(id=id, model=model)
        doc_ref.set(model.to_struct())

    def get(self, id: str, model: 'Model') -> 'Model':
        """Get document by id and serialise into its corresponding ORM model

        Returns:
            :class: `firestore_orm.model.Model`  -- ORM model
        """
        document = self._get_document(id=id, model=model).get()
        return self._doc_to_instance(document, model)

    def query(
            self,
            model: 'Model',
            filters: 'List[Tuple[str, str, Any]]' = None,
            order_by: dict = {'created_at': firestore.Query.DESCENDING},
            # order_by: dict = None,
            start_at: dict = None,
            limit: int = None,
            offset: int = None,
            single: bool = False,
            to_dict: bool = False,
            to_struct: bool = False
    ) -> 'List[Model]':
        """Query all collections

        Arguments:
            model {:class: `firestore_orm.model.Model`} -- ORM model

            filters {dict} -- query filters to filter results, eg: [(key, op_string, value)]. op_string must be one of <, <=, ==, >, >=, or array_contains

            limit {int} -- limit collections

            offset {int} -- offset collections

            order_by {dict} -- order collections by ascending or descending order.

            start_at {dict} -- Refer to https://firebase.google.com/docs/firestore/query-data/query-cursors

            single {bool} -- Return the first of the many results

            to_dict {bool} -- serialise response. set to true to return a list of dict else returns a list of model class, Hides hidden fields

            to_struct {bool} -- serialise response. set to true to return a list of dict else returns a list of model class. Exposes all data

        Returns:
            List[:class: `firestore_orm.model.Model`] -- List of ORM models
        """

        offset = 0 if offset is None else offset
        docs = self._get_ref(model)

        if filters:
            for key, op_string, val in filters:
                docs = docs.where(key, op_string, val)

        if order_by:
            for key, val in order_by.items():
                docs = docs.order_by(key, direction=val.upper(
                ) if val else firestore.Query.ASCENDING)

            if start_at:
                docs = docs.start_at(start_at)

        docs = docs.offset(offset)

        if limit:
            docs = docs.limit(limit)

        def op(doc):
            return self._doc_to_instance(
                doc, model
            ) if not to_dict and not to_struct else self._doc_to_instance(
                doc, model
            ).to_dict() if to_dict else self._doc_to_instance(
                doc, model
            ).to_struct()

        instances = list(map(op, docs.get()))

        if single:
            instances = instances[0] if len(instances) > 0 else None
        return instances

    @staticmethod
    def _doc_to_instance(document: [DocumentSnapshot, DocumentReference], model: 'Model') -> 'Model':
        """Serialise document to its corresponding model

        Returns:
            :class: `firestore_orm.model.Model`  -- ORM model
        """

        document = document.get().to_dict() if isinstance(
            document, DocumentReference) else document.to_dict()
        if not document:
            return None
        kwargs = {}
        for key, _ in model.iterate_over_fields():
            kwargs[key] = document.get(key)

        return model(**kwargs)
