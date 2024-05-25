from db_api import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger, Boolean, Text
from sqlalchemy import Table
from sqlalchemy.orm import relationship

mailinglist_contacts_relation = Table(
    "first_app_mailinglist_contacts",
    Base.metadata,
    Column("mailinglist_id", Integer, ForeignKey("first_app_mailinglist.id")),
    Column("contact_id", Integer, ForeignKey("first_app_contact.id")),
)

mailinglist_mailingservices_relation = Table(
    "first_app_mailinglist_mailing_services",
    Base.metadata,
    Column("mailinglist_id", Integer, ForeignKey("first_app_mailinglist.id")),
    Column("mailingservice_id", Integer, ForeignKey("first_app_mailingservice.id")),
)

mailinglist_sites_relation = Table(
    "first_app_mailinglist_sites",
    Base.metadata,
    Column("mailinglist_id", Integer, ForeignKey("first_app_mailinglist.id")),
    Column("site_id", Integer, ForeignKey("first_app_site.id")),
)

class Contact(Base):
    __tablename__ = "first_app_contact"

    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable = False)
    contact_string = Column(String(255), nullable = False)
    is_active = Column(Boolean, default=False)

class Site(Base):
    __tablename__ = "first_app_site"

    label = Column(String(255), nullable=False)
    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    expected_responce_code = Column(String(255), nullable=False)
    expected_responce_code_pattern = Column(String(255), nullable=False)
    cheking_active = Column(String(255))
    inversive_condition = Column(Boolean)
    cron_schedule = Column(String(255))
    last_checked = Column(DateTime)
    is_alive = Column(Boolean)

class Service(Base):
    __tablename__ = "first_app_mailingservice"

    id = Column(Integer, primary_key=True, nullable=True)
    label = Column(Integer, primary_key=True, nullable=True)
    type = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)
    message_pattern = Column(Text, nullable=True)
    is_active = Column(Boolean, nullable=False)
    login = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    headers = Column(Text, nullable=True)
    api_url = Column(String(255), nullable=False)
    request_type = Column(String(255), nullable=False)
    body_pattern = Column(Text, nullable=True)
    body_format = Column(Text, nullable=False)

class MailingList(Base):
    __tablename__ = "first_app_mailinglist"

    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False)

    contacts = relationship('Contact', secondary=mailinglist_contacts_relation)
    mailing_services = relationship('Service', secondary=mailinglist_mailingservices_relation, lazy=False)
    sites = relationship('Site', secondary=mailinglist_sites_relation, lazy=False)
