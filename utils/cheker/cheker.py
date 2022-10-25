# from jsonschema import validate
from utils.error_messages.errors import ErrorMessages


class ResponseValid:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, ErrorMessages.WRONG_STATUS_CODE
        else:
            assert self.response_status == status_code, ErrorMessages.WRONG_STATUS_CODE
        return self

    def assert_len_element(self, response):
        assert len(self.response_json) == response, ErrorMessages.WRONG_ELEMENT_COUNT
        return self

    def assert_response_id(self, id):
        assert self.response_json.get('id') == id, ErrorMessages.WRONG_ID

    def assert_response_name(self, name):
        assert self.response_json.get('name') == name, ErrorMessages.WRONG_NAME

    def assert_response_status(self, status):
        assert self.response_json.get('status') == status, ErrorMessages.WRONG_STATUS

    def assert_response_photourl_not_empty(self):
        assert "https" or "http" in self.response_json.get("photoUrls")[0], ErrorMessages.MISSING_URL

    def assert_message_equal_username(self, user_name):
        assert self.response_json.get("message") == user_name, ErrorMessages.WRONG_NAME

    def assert_all_fields(self, body):
        response_fields = [k for k in self.response_json]
        body_fields = [k for k in body]
        for i in range(len(body_fields)):
            assert response_fields[i] in body_fields, ErrorMessages.MISSING_FIELD
