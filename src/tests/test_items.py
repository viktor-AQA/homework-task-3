from src.config.constant import BASE_URL


class TestItems:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"
        print(response.json())

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]

        self.created_item_id = item_id

    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Response missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"

    def test_put_items(self, auth_session, upd_item_data, item_data):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None

        response = auth_session.put(f"{BASE_URL}/api/v1/items/{item_id}", json=upd_item_data)

        assert response.status_code == 200, "Введенные данные некорректны"
        assert response.json()["description"] == upd_item_data["description"], "Обновление не прошло"
        assert response.json()["title"] == upd_item_data["title"], "Обновление не прошло"

    def test_delete_items(self, auth_session, item_data):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None

        response = auth_session.delete(f"{BASE_URL}/api/v1/items/{item_id}")
        assert response.status_code == 200, "Запись не удалена"




