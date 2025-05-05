from src.api import api_class
from src.api.api_class import ApiClass
from src.tests.constant import BASE_URL
import src.api.api_class


class TestItems:

    def test_create_item(self, auth_session, item_data):
        response = ApiClass.post_create(auth_session, item_data)

    def test_get_items(self, auth_session):
        response = ApiClass.get_items(auth_session)

    def test_put_items(self, test_item, upd_item_data, auth_session):
        response = ApiClass.put_items(auth_session, upd_item_data, test_item)

    def test_delete_items(self, auth_session, item_data):
        response = auth_session.post(f"{BASE_URL}/api/v1/items/", json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None

        response = auth_session.delete(f"{BASE_URL}/api/v1/items/{item_id}")
        assert response.status_code == 200, "Запись не удалена"
