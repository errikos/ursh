from flask import Blueprint


bp = Blueprint('urls', __name__)

import urlshortener.blueprints.urls_bp.urls  # noqa isort:skip
import urlshortener.blueprints.urls_bp.callbacks  # noqa isort:skip
