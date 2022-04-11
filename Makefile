init:
	# set up the integration tests
	
	docker compose up -d
	aws s3 --endpoint-url=http://localhost:4566 mb s3://test 

test:
	aws s3 --endpoint-url=http://localhost:4566 cp test.json s3://test/test.json
	pytest tests