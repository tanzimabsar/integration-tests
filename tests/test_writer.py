import unittest
import boto3


class TestWriter(unittest.TestCase):
    def test_write(self):
        s3 = boto3.client(
            's3',
            region_name='eu-west-1',
            endpoint_url='http://localhost:4566'
        )

        with open('testDownload.json', 'wb') as f:
            data = s3.download_fileobj('test', 'test.json', f)
            print(data)


if __name__ == '__main__':
    unittest.main()
