# Генератор QR кодов

#### Python, Redis, Docker, gRPC, Fastapi

Онлайн генератор __QR кодов__: пользователь дает ссылку и название для кода, hanler (__fastapi__) обробатывает данные, полученные данные отправляются в __redis__ через __http__,  redis проверяет , есть ли у него подсохраненные данные с таким названием, если данные есть - отдаем пользователю, если нет отправляем данные воркеру через __gRPC__, далее происходит генерацция кода после чего готовый qr отдается пользователю и сохраняется в redis.

##### Использованные технологии:

1. Backend
	1. python
	2. fastapi
	3. redis
	4. http
	5. pydantic
	6. gRPC
	7. qrcode
