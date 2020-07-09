import os

from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), ".env"))

MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME", "")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
MYSQL_HOSTNAME = os.environ.get("MYSQL_HOSTNAME", "")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "")
MYSQL_PORT = os.environ.get("MYSQL_PORT", "")

LOG_LEVEL = os.environ.get("LOG_LEVEL", "")

ELASTICSEARCH_HOST = os.environ.get("ELASTICSEARCH_HOST", "")
ELASTICSEARCH_PORT = os.environ.get("ELASTICSEARCH_PORT", "")
