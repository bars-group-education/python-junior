from datetime import (
    date,
)

from django.test import (
    TestCase,
)

from block_2.model_fields.models import (
    Department,
    Worker,
)


class WorkerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods

        department = Department.objects.create(
            name='Отдел №1'
        )
        workers = [
            Worker(
                first_name='Новый',
                last_name='Новый',
                startwork_date=date(2021, 1, 1),
                department=department),
            Worker(
                first_name='Неизвестный',
                department=department
            ),
            Worker(
                first_name='Владимиров',
                last_name='Владимир',
                startwork_date=date(2021, 1, 1),
                tab_num=11,
                department=department
            ),
            Worker(
                first_name='Алексеев',
                last_name='Алексей',
                startwork_date=date(2021, 1, 1),
                tab_num=1,
                department=department
            )
        ]

        Worker.objects_all.bulk_create(workers)

    def test_all_count_workers(self):
        all_count = Worker.objects_all.all().count()
        self.assertEquals(all_count, 4)

    def test_all_count_workers(self):
        active_count = Worker.objects.all().count()
        self.assertEquals(active_count, 2)

    def test_get_active_worker_count(self):
        department = Department.objects.filter(name='Отдел №1').first()
        self.assertEquals(department.get_active_worker_count, 2)

    def test_get_all_worker_count(self):
        department = Department.objects.filter(name='Отдел №1').first()
        self.assertEquals(department.get_all_worker_count, 4)

