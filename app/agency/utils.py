from datetime import datetime

from flask_login import current_user

from app.lib.utils import eval_request_bool
from app.lib.db_utils import (
    update_object,
    create_object
)
from app.models import (
    Agencies,
    Events
)
from app.constants.event_type import AGENCY_ACTIVATED


def update_agency_active_status(agency_ein, is_active):
    """
    Update the active status of an agency.
    :param agency_ein: String identifier for agency (4 characters)
    :param is_active: Boolean value for agency active status (True = Active)
    :return: Boolean value (True if successfully changed active status)
    """
    is_valid_agency = Agencies.query.filter_by(ein=agency_ein).first() is not None

    if is_active is not None and is_valid_agency:
        update_object(
            {'is_active': eval_request_bool(is_active)},
            Agencies,
            agency_ein
        )
        create_object(
            Events(
                request_id=None,
                user_guid=current_user.guid,
                auth_user_type=current_user.auth_user_type,
                type_=AGENCY_ACTIVATED,
                new_value={"ein": agency_ein},
                timestamp=datetime.utcnow()
            )
        )

        return True
    return False


def get_agency_feature(agency_ein, feature):
    """
    Retrieve the specified agency feature for the specified agency.

    :param agency_ein:  String identifier for agency (4 characters)
    :param feature: Feature specified. See app/lib/constants/agency_features.py for possible values (String)

    :return: JSON Object
    """

    agency_features = get_agency_features(agency_ein)

    if agency_features is not None and feature in agency_features:
        return {feature: agency_features[feature]}

    return None


def get_agency_features(agency_ein):
    """
    Retrieve the agency features JSON object for the specified agency.

    :param agency_ein: String identifier for agency (4 characters)
    :return: JSON Object
    """
    is_valid_agency = Agencies.query.filter_by(ein=agency_ein).first() is not None

    if is_valid_agency:
        agency_features = Agencies.query.filter_by(ein=agency_ein).first().agency_features

        return agency_features

    return None