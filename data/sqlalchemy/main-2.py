from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model import Base, Publisher, Book, Shop, Stock, Sale
from datetime import datetime

DATABASE = 'postgresql://postgres:postgres@localhost:5432/book_store'
engine = create_engine(DATABASE)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name="Пушкин")
session.add(publisher1)
session.flush()

book1 = Book(title='Капитанская дочка', publisher=publisher1)
book2 = Book(title='Руслан и Людмила', publisher=publisher1)
book3 = Book(title='Евгений Онегин', publisher=publisher1)
shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Лабиринт')
shop3 = Shop(name='Книжный Дом')
stock1 = Stock(book=book1, shop=shop1, count=1)
stock2 = Stock(book=book2, shop=shop1, count=1)
stock3 = Stock(book=book1, shop=shop2, count=1)
stock4 = Stock(book=book3, shop=shop3, count=1)
sale1 = Sale(price=600, date_sale = datetime(2022, 11, 9), stock=stock1, count=1)
sale2 = Sale(price=500, date_sale = datetime(2022, 11, 8), stock=stock2, count=1)
sale3 = Sale(price=580, date_sale = datetime(2022, 11, 5), stock=stock3, count=1)
sale4 = Sale(price=490, date_sale = datetime(2022, 11, 2), stock=stock4, count=1)
sale5 = Sale(price=600, date_sale = datetime(2022, 10, 26), stock=stock1, count=1)

session.add_all([publisher1, book1, book2, book3, stock1, stock2, stock3, stock4, sale1, sale2, sale3, sale4, sale5])
session.commit()


publisher_input = input("Введите имя или ID издателя:")

try:
    publisher_id = int(publisher_input)
except ValueError:
    publisher_id = None

query = (
    session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
    .join(Publisher, Publisher.id == Book.id_publisher)
    .join(Stock, Stock.id_book == Book.id)
    .join(Shop, Shop.id == Stock.id_shop)
    .join(Sale, Sale.id_stock == Stock.id)
    .filter(or_(Publisher.name == publisher_input, Publisher.id == publisher_id))
    .order_by(Sale.date_sale.desc())
)

result = query.all()

print("Результаты:")
unique_results = set()
for title, shop_name, price, date_sale in result:
    formatted_date = date_sale.strftime('%d-%m-%Y')
    formatted_result = f"{title:<18} | {shop_name:<11} | {price:<4.0f} | {formatted_date}"
    if formatted_result not in unique_results:
        unique_results.add(formatted_result)
        print(formatted_result)

session.close()