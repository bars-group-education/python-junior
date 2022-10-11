from datetime import date

from django.test import (
    TestCase,
)

from block_2.meta_and_inheritance.models import (
    EducationOffice,
    GeneralOffice,
    Department,
    Worker,
    Director,
    OrderedWorker,
)


class WorkerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        education_office = EducationOffice.objects.create(
            address='Москва',
            mail='edu@gmail.com'
        )

        general_office = GeneralOffice.objects.create(
            address='Казань',
            mail='general@gmail.com'
        )

        department = Department.objects.create(
            name='Отдел №1',
            education_office=education_office,
            office=general_office
        )
        workers = [
            Worker(
                first_name='Новый',
                last_name='Новый',
                startwork_date=date(2009, 3, 3),
                department=department
            ),
            Worker(
                first_name='Неизвестный',
                department=department
            ),
            Worker(
                first_name='Владимиров',
                last_name='Владимир',
                startwork_date=date(2011, 11, 11),
                tab_num=2,
                department=department
            ),
            Worker(
                first_name='Алексеев',
                last_name='Алексей',
                startwork_date=date(2008, 8, 8),
                tab_num=33,
                department=department
            ),
            Worker(
                first_name='Алексеев',
                last_name='Андрей',
                startwork_date=date(2004, 1, 1),
                tab_num=3,
                department=department
            ),
            Worker(
                first_name='Алексеев',
                last_name='Андрей',
                startwork_date=date(2009, 9, 9),
                tab_num=2,
                department=department
            ),
        ]

        Worker.objects_all.bulk_create(workers)


        Director.objects.create(
            first_name='Тарасов',
            last_name='Тарас',
            startwork_date=date(1999, 1, 1),
            tab_num=1,
            department=department)


    def test_all_count_workers(self):
        all_count = Worker.objects_all.all().count()
        self.assertEquals(all_count, 7)

    def test_count_only_workers(self):
        only_workers = Worker.objects.all().count()
        self.assertEquals(only_workers, 6)

    def test_ordered_worker_model(self):
        worker = OrderedWorker.objects.all().first()
        self.assertEquals(worker.startwork_year, 2004)

    def test_department_office(self):
        department = Department.objects.all().first()
        self.assertEquals(department.education_office.address, 'Москва')
        self.assertEquals(department.office.address, 'Казань')
