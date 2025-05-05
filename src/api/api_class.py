from src.tests.constant import BASE_URL

class ApiClass:
    @staticmethod
    def post_create(auth_session, item_data):
        response = auth_session.post(f"{BASE_URL}/api/v1/items/", json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None

        response = auth_session.delete(f"{BASE_URL}/api/v1/items/{item_id}")
        assert response.status_code == 200, "Ошибка удаления"

        return item_id

    @staticmethod
    def get_items(auth_session):
        response = auth_session.get(f"{BASE_URL}/api/v1/items/")

        assert response.status_code == 200, f"Ошибка: {response.text}"
        items = response.json()  # Получаем список items в формате JSON
        assert len(items) > 0, "Список items пуст"
        # return response  # Возвращаем объект ответа

    @staticmethod
    def put_items(auth_session, upd_item_data, test_item):
        item_id = test_item
        response = auth_session.put(f"{BASE_URL}/api/v1/items/{item_id}", json=upd_item_data)

        assert response.status_code == 200, "Введенные данные некорректны"
        assert response.json()["description"] == upd_item_data["description"], "Обновление не прошло"
        assert response.json()["title"] == upd_item_data["title"], "Обновление не прошло"

        return response

    def delete_items(self, post_create, item_id):
        response = post_create.delete(f"{BASE_URL}/api/v1/items/{item_id}")
        assert response.status_code == 200, "Запись не удалена"
