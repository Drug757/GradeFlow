# GradeFlow

Простой консольный калькулятор среднего балла.
Позволяет ввести список предметов и оценки, после чего рассчитывает средний арифметический балл и выводит буквенную оценку успеваемости.

## Запуск
```
python main.py
```

## Графический интерфейс
Приложение имеет графический интерфейс на базе Tkinter с прокруткой и цветовым результатом.


## Запуск через Docker

### Сборка образа
```
docker build -t gradeflow .
```

### Запуск контейнера
```
docker run --name gradeflow-container gradeflow
```

### Остановка контейнера
```
docker stop gradeflow-container
```

### Удаление контейнера
```
docker rm gradeflow-container
```

## Инструменты качества кода

Проект использует:
- **Black** — форматирование кода
- **Ruff** — линтер
- **Pre-commit** — автоматические проверки перед коммитом

### Конфигурационные файлы
- `pyproject.toml` — настройки Black и Ruff
- `.pre-commit-config.yaml` — настройки pre-commit hooks

### Запуск проверок вручную

```
# Форматирование
python -m black main.py

# Линтер
python -m ruff check main.py
python -m ruff check main.py --fix
```


