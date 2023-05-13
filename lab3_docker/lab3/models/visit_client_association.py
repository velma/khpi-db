import sqlalchemy as sa
from .base import myBase


class VisitClientAssociation(myBase):
    __tablename__ = 'visit_clients'

    visit_id = sa.Column(sa.Integer,
                         sa.ForeignKey('visits.visit_id',
                                       name='visit_clients_visit_fk',
                                       ondelete='cascade',
                                       onupdate='cascade'),
                         primary_key=True,
                         nullable=False)
    client_id = sa.Column(sa.Integer,
                          sa.ForeignKey('clients.client_id',
                                        name='visit_clients_client_fk',
                                        ondelete='cascade',
                                        onupdate='cascade'),
                          primary_key=True,
                          nullable=False)
