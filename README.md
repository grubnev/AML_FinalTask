#Проект для выполнения финального задания по курсу "Автоматизация машинного обучения" (MLOps).

Цель проекта: разработать конвеер машинного обучения data-продукта (Web или API приложение).
Команда проекта. Проект выполняется в команде из 3-4 человека.

Требования к реализации проекта:

Исходные коды проекта должны находиться в репозитории GitHub.
Проект оркестируется с помощью ci/cd (jenkins или gitlab).
Датасеты версионируются с помощью dvc и синхронизируются с удалённым хранилищем.
Разработка возможностей приложения должна проводиться в отдельных ветках, наборы фичей и версии данных тоже.
В коневеере запускаются не только модульные тесты, но и проверка тестами на качество данных.
Итоговое приложение реализуется в виде образа docker. Сборка образа происходит в конвеере.
В проекте может использоваться предварительно обученная модель. Обучать собственную модель не требуется.

## Установка и использование

1. Склонируйте репозиторий:

git clone https://github.com/grubnev/AML_FinalTask.git

2. Установите зависимости:

pip install -r requirements.txt

3. Запустите веб-приложение:
streamlit run app.py
