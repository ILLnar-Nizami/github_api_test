# GitHub API Test

Этот проект содержит автоматический тест для GitHub API используя Python и необходимые библиотеки.

## Предвариетельные требования

- Python 3.8+
- GitHub аккаунт и персональный токен доступа

## Установка

1. Склонировать этот репозиторий:
   ```
   git clone https://github.com/your-username/github-api-test.git
   cd github-api-test
   ```

2. Создать virtual environment и активировать его:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Установить необходимые пакеты:
   ```
   pip install -r requirements.txt
   ```

4. Создать файл `.env` в корневом каталоге и добавить ваши учётные данные GitHub:
   ```
   GITHUB_USERNAME=your_username
   GITHUB_TOKEN=your_personal_access_token
   REPO_NAME=test_repo_name
   ```

## Выполнение теста

```
pytest tests/test_api.py
```

## Notes

- Убедитесь, что вы создали на GitHub персональный токен доступа с необходимыми правами (repo, delete_repo, admin:org).
- Тест создаст и удалит тестовый репозиторий. Убедитесь, что имя REPO_NAME в вашем файле .env уникально и не конфликтует с существующими репозиториями.
