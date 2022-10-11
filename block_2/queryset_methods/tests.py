from datetime import (
    date,
)
from decimal import (
    Decimal,
)

from django.test import (
    TestCase,
)

from block_2.queryset_methods.models import (
    Product,
    ProductCount,
    ProductCost,
    Customer,
    Order,
    OrderItem,
)


class BaseTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        milk = Product.objects.create(name='Молоко')

        ProductCount.objects.bulk_create([
            ProductCount(
                product=milk,
                begin=date(2021, 1, 1),
                end=date(2021, 1, 31),
                value=10,
            ),
            ProductCount(
                product=milk,
                begin=date(2021, 2, 1),
                end=date(2021, 2, 28),
                value=4,
            ),
            ProductCount(
                product=milk,
                begin=date(2021, 3, 1),
                end=date(2021, 3, 31),
                value=7,
            )
        ])

        ProductCost.objects.bulk_create([
            ProductCost(
                product=milk,
                begin=date(2021, 1, 1),
                end=date(2021, 1, 31),
                value=Decimal(50),
            ),
            ProductCost(
                product=milk,
                begin=date(2021, 2, 1),
                end=date(2021, 2, 14),
                value=Decimal(60),
            ),
            ProductCost(
                product=milk,
                begin=date(2021, 2, 15),
                end=date(2021, 2, 28),
                value=Decimal(65),
            ),
            ProductCost(
                product=milk,
                begin=date(2021, 3, 1),
                end=date(2021, 3, 31),
                value=Decimal(60),
            )
        ])

        bread = Product.objects.create(name='Хлеб')

        ProductCount.objects.bulk_create([
            ProductCount(
                product=bread,
                begin=date(2021, 1, 1),
                end=date(2021, 1, 31),
                value=100,
            ),
            ProductCount(
                product=bread,
                begin=date(2021, 2, 1),
                end=date(2021, 2, 28),
                value=50,
            ),
            ProductCount(
                product=bread,
                begin=date(2021, 3, 1),
                end=date(2021, 3, 1),
                value=0,
            )
        ])

        ProductCost.objects.bulk_create([
            ProductCost(
                product=bread,
                begin=date(2021, 1, 1),
                end=date(2021, 1, 31),
                value=Decimal(30),
            ),
            ProductCost(
                product=bread,
                begin=date(2021, 2, 1),
                end=date(2021, 2, 14),
                value=Decimal(32),
            ),
            ProductCost(
                product=bread,
                begin=date(2021, 3, 1),
                end=date(2021, 3, 31),
                value=Decimal(35),
            )
        ])

        tea = Product.objects.create(name='Чай')

        ProductCount.objects.bulk_create([
            ProductCount(
                product=tea,
                begin=date(2021, 1, 1),
                end=date(2021, 1, 31),
                value=64,
            ),
            ProductCount(
                product=tea,
                begin=date(2021, 3, 1),
                end=date(2021, 3, 1),
                value=32,
            )
        ])

        ProductCost.objects.bulk_create([
            ProductCost(
                product=tea,
                begin=date(2021, 1, 1),
                end=date(2021, 1, 31),
                value=Decimal(150),
            ),
            ProductCost(
                product=tea,
                begin=date(2021, 2, 1),
                end=date(2021, 2, 14),
                value=Decimal(140),
            ),
            ProductCost(
                product=tea,
                begin=date(2021, 3, 1),
                end=date(2021, 3, 31),
                value=Decimal(160),
            )
        ])

        salt = Product.objects.create(name='Соль')

        ivan = Customer.objects.create(name='Иван')
        pavel = Customer.objects.create(name='Павел')
        oleg = Customer.objects.create(name='Олег')
        egor = Customer.objects.create(name='Егор')

        order_1 = Order.objects.create(
            number='1',
            date_formation=date(2021, 1, 1),
            customer=ivan,
        )
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order_1,
                product=milk,
                count=1,
            ),
            OrderItem(
                order=order_1,
                product=bread,
                count=1,
            ),
            OrderItem(
                order=order_1,
                product=tea,
                count=1,
            )
        ])

        order_2 = Order.objects.create(
            number='2',
            date_formation=date(2021, 1, 10),
            customer=oleg,
        )
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order_2,
                product=milk,
                count=3,
            ),
            OrderItem(
                order=order_2,
                product=tea,
                count=2,
            )
        ])

        order_3 = Order.objects.create(
            number='3',
            date_formation=date(2021, 1, 15),
            customer=pavel,
        )
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order_3,
                product=milk,
                count=6,
            ),
            OrderItem(
                order=order_3,
                product=tea,
                count=1,
            )
        ])

        order_4 = Order.objects.create(
            number='4',
            date_formation=date(2021, 1, 15),
            customer=ivan,
        )
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order_4,
                product=bread,
                count=1,
            ),
            OrderItem(
                order=order_4,
                product=tea,
                count=4,
            )
        ])

        order_5 = Order.objects.create(
            number='5',
            date_formation=date(2021, 2, 7),
            customer=oleg,
        )
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order_5,
                product=milk,
                count=4,
            ),
            OrderItem(
                order=order_5,
                product=bread,
                count=2,
            )
        ])

        order_6 = Order.objects.create(
            number='6',
            date_formation=date(2021, 2, 19),
            customer=ivan,
        )
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order_6,
                product=tea,
                count=3,
            ),
        ])

        order_7 = Order.objects.create(
            number='7',
            date_formation=date(2021, 3, 1),
            customer=pavel,
        )
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order_7,
                product=milk,
                count=8,
            ),
        ])
