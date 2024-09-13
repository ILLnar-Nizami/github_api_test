import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение значений переменных окружения
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

# Установка базового URL для API GitHub и заголовков для запросов
BASE_URL = 'https://api.github.com'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def test_create_repo():
    """Тестирование создания репозитория"""
    url = f'{BASE_URL}/user/repos'
    data = {
        'name': REPO_NAME,
        'description': 'Тестовый репозиторий, созданный через API',
        'private': False
    }
    response = requests.post(url, json=data, headers=HEADERS)
    assert response.status_code == 201, f"Не удалось создать репозиторий: {
        response.text}"


def test_check_repo_exists():
    """Проверка существования репозитория"""
    url = f'{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200, f"Репозиторий не найден: {
        response.text}"


def test_delete_repo():
    """Тестирование удаления репозитория"""
    url = f'{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.delete(url, headers=HEADERS)
    assert response.status_code == 204, f"Не удалось удалить репозиторий: {
        response.text}"


def test_github_api_flow():
    """Выполнение полного потока тестирования API GitHub"""
    try:
        test_create_repo()
        test_check_repo_exists()
    finally:
        test_delete_repo()
