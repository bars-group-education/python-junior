from django.test import RequestFactory, TestCase


class MiddlewareTestCase(TestCase):

    def test_FormatterMiddleware(self):
        response = self.client.get('/calc/?maths=3*3;10-2;12/5&delimiter=;')
        content = response.content.decode()
        self.assertEqual(content, '<p>3*3 = 9</p><p>10-2 = 8</p><p>12/5 = 2.4</p>')

    def test_default_FormatterMiddleware(self):
        response = self.client.get('/calc/?maths=300*30,1-2,100/5')
        content = response.content.decode()
        self.assertEqual(content, '<p>300*30 = 9000</p><p>1-2 = -1</p><p>100/5 = 20.0</p>')

    def test_CheckErrorMiddleware(self):
        response = self.client.get('/calc/?maths=3*3;10-2;12/0&delimiter=;')
        content = response.content.decode().split(':')[0]

        self.assertEqual(content, 'Ошибка')

    def test_default_CheckErrorMiddleware(self):
        response = self.client.get('/calc/?maths=3*3;10-2;12/5')
        content = response.content.decode().split(':')[0]

        self.assertEqual(content, 'Ошибка')
