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
- [ОПД - Основы Профессиональной Деятельности](https://sergeypugin.github.io/itmo-notebook/opd)
- [МатАн - Математический анализ](https://sergeypugin.github.io/itmo-notebook/matan)
Материалы автоматически публикуются на сайте https://sergeypugin.github.io/itmo-notebook. Заметки поддерживают Markdown-синтаксис, коллауты Obsidian и другие возможности Quartz.

Для ссылок используйте стандартный Markdown-синтаксис. Как устроить окружение, какие правила оформления действуют и как прогнать проверки перед PR, описано в [CONTRIBUTING](CONTRIBUTING.md); устройство скриптов -- в [README папки `scripts`](scripts/README.md).

Шаблон сайта: https://github.com/sergeypugin/quartz-ready-template

## Участники

Проект развивается совместными усилиями студентов и депендабота:

[![Contributors](https://contrib.rocks/image?repo=sergeypugin/itmo-notebook&max=100&columns=10)](https://github.com/sergeypugin/itmo-notebook/graphs/contributors)

## Как внести вклад

Мы приветствуем дополнения, исправления опечаток и новые билеты от студентов младших курсов. Пошаговая инструкция, правила оформления заметок и команды для локальной проверки собраны в [CONTRIBUTING](CONTRIBUTING.md).

Коротко: сделайте форк, внесите правки, выполните `python scripts/normalize.py` и откройте Pull Request в `main`. Скрипты сами приведут заметки к каноническому виду, так что помнить все правила наизусть не нужно.
