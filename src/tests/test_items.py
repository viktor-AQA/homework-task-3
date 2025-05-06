from src.api.api_class import ApiClass


class TestItems:

    def test_create_item(self, auth_session, item_data):
        response = ApiClass.post_create(auth_session, item_data)

    def test_get_items(self, auth_session):
        response = ApiClass.get_items(auth_session)

    def test_put_items(self, test_item, upd_item_data, auth_session):
        response = ApiClass.put_items(auth_session, upd_item_data, test_item)

    def test_delete_items(self, auth_session, test_item):
        response = ApiClass.delete_items(auth_session, test_item)
