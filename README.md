# cadastral_num

# cadastral numиук



**Описание**  
Клиент и сервер, которые эмулируют отправку кадастрового номера и координат на сервер. Сервер может обрабатывать информацию до 60 секунд и возвращает bool значение.
Эндпоинты:
- /query для отпрвки запроса
- /result для получения результата
- /ping для проверки доступности

**Технологии:**  
- [Python](https://www.python.org/doc/) 
- [FastAPI](https://fastapi.tiangolo.com/)
- [aiohttp](https://docs.aiohttp.org/en/stable/)
- [Docker](https://www.docker.com/)


---
## Документация  
**Запуск проекта в Docker:**
- **Переходим в коталог с docker-compose.yaml `./cadastral_num/`:**
    ```bash
    cd cadastral_num/
    ```  
- **Запускаем контейнеры:**  
    ```bash
    docker-compose up -d
    ``` 
**Клиент доступен по адресу:**  
```bash
http://127.0.0.1:8000/ 
```
**Документация к клиенту:**  
```bash
http://127.0.0.1:8000/docs 
```
**Сервер доступен по адресу:**  
```bash
http://127.0.0.1:8001/ 
```
**Документация к серверу:**  
```bash
http://127.0.0.1:8001/docs 
```

**Остановка проекта:**
    ```bash
    docker-compose down 
    ```
