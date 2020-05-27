from namex.models import User

# params = {
#   name,
#   location, one of: [‘bc’, ‘ca’, ‘us’, or ‘it’],
#   entity_type: abbreviation. convention not finalized yet.
#   request_type, one of: [‘new’, ‘existing’, ‘continuation’]
# }

token_header = {
    "alg": "RS256",
    "typ": "JWT",
    "kid": "flask-jwt-oidc-test-client"
}

claims = {
    "iss": "https://sso-dev.pathfinder.gov.bc.ca/auth/realms/sbc",
    "sub": "43e6a245-0bf7-4ccf-9bd0-e7fb85fd18cc",
    "aud": "NameX-Dev",
    "exp": 31531718745,
    "iat": 1531718745,
    "jti": "flask-jwt-oidc-test-support",
    "typ": "Bearer",
    "username": "test-user",
    "realm_access": {
        "roles": [
            "{}".format(User.EDITOR),
            "{}".format(User.APPROVER),
            "viewer",
            "user"
        ]
    }
}

API_BASE_URI = '/api/v1/'
ENDPOINT_PATH = API_BASE_URI + 'name-analysis'

# @pytest.mark.xfail(raises=ValueError)
def test_contains_unclassifiable_word_request_response(client, jwt, app):
    test_params = {
        'name': 'MOUNTAIN VIEW FOOD BLOGGINS ULC.',
        'location': 'CA',
        'entity_type': 'XUL',
        'request_type': 'NEW'
    }


# @pytest.mark.xfail(raises=ValueError)
def test_contains_words_to_avoid_request_response(client, jwt, app):
    test_params = {
        'name': 'MOUNTAIN VIEW VSC ULC.',
        'location': 'CA',
        'entity_type': 'XUL',
        'request_type': 'NEW'
    }


# @pytest.mark.xfail(raises=ValueError)
def test_name_requires_consent_request_response(client, jwt, app):
    test_params = {
        'name': 'MOUNTAIN VIEW FOOD ENGINEERING ULC.',
        'location': 'CA',
        'entity_type': 'XUL',
        'request_type': 'NEW'
    }


# @pytest.mark.xfail(raises=ValueError)
def test_corporate_name_conflict_request_response(client, jwt, app):
    test_params = {
        'name': 'MOUNTAIN VIEW FOOD GROWERS ULC.',
        'location': 'CA',
        'entity_type': 'XUL',
        'request_type': 'NEW'
    }