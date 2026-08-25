# ITMO Notebook

[![Website Live](https://img.shields.io/badge/Website-Live-22C55E?logo=githubpages&logoColor=white)](https://sergeypugin.github.io/itmo-notebook)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-22C55E?logo=github-actions&logoColor=white)](https://pages.github.com/)
[![Template](https://img.shields.io/badge/Template-quartz--ready--template-blue?logo=github&logoColor=white)](https://github.com/sergeypugin/quartz-ready-template)
[![Quartz 5](https://img.shields.io/badge/Engine-Quartz%205-7C3AED?logo=obsidian&logoColor=white)](https://quartz.jzhao.xyz)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE.md)

Материалы для подготовки к экзаменам студентов СППО ПИиКТ Университета ИТМО.

[О проекте](#о-проекте) | [Участники](#участники) | [Как внести вклад](#как-внести-вклад)

## О проекте

Репозиторий содержит разобранные экзаменационные билеты по предметам:
- [ОПД - Основы Профессиональной деятельности](https://sergeypugin.github.io/itmo-notebook/opd)
- [МатАн - Математический Анализ](https://sergeypugin.github.io/itmo-notebook/matan)
Материалы автоматически публикуются на сайт https://sergeypugin.github.io/itmo-notebook, поддериживающим Markdown flavored Obsidian:
- **Вики-ссылки:** `[[Имя заметки]]` и `[[Имя заметки|Кастомный текст]]` с авто-поиском путей
- **Коллауты:** теперь доступны `> [!quote]`, `> [!success]`, `> [!bug]` и другие. Поддерживается сворачивание и кастомные заголовки (`> [!note]- Уточнение`, `> [!important]+ Важно!`)
- Поддержка баз данных Bases (`.base`) и Canvas (`.canvas`) от Obsidian и многое другое

Шаблон сайта: https://github.com/sergeypugin/quartz-ready-template

## Участники

Проект развивается совместными усилиями студентов и депендабота:

[![Contributors](https://contrib.rocks/image?repo=sergeypugin/itmo-notebook&max=100&columns=10)](https://github.com/sergeypugin/itmo-notebook/graphs/contributors)

## Как внести вклад

Мы приветствуем дополнения, исправления опечаток и новые билеты от студентов младших курсов:
1. Сделайте **Fork** этого репозитория
2. Для удобства работы с заметками рекомендуется открывать не сам репозиторий как Vault, а именно папку `itmo-notebook/`.
3. Внесите правки и/или добавьте новые статьи
4. Создайте **Pull Request**

> [!important]
> Файлы заметок рекомендуется называть на латинице (например, `question-1.md`), а отображаемый заголовок на русском языке указывать в YAML-свойстве `title`. Это обеспечивает корректные URL-адреса страниц при публикации.

>[!tip]
>После форка и клонирования репозитория для предпросмотра сайта локально требуется [Node.js](https://nodejs.org/) версии 22 или новее. Выполните следующие команды в **корне** репозитория.
> ```bash
> # Установка базовых зависимостей
> npm ci
> 
> # Загрузка плагинов Quartz
> npx quartz plugin install --from-config
> 
> # Запуск локального сервера с указанием рабочей папки
> npx quartz build --serve -d itmo-notebook
> ```
> 
> После выполнения команд локальная версия сайта будет доступна по адресу [http://localhost:8080](http://localhost:8080).
