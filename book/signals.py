import os
import json
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_delete

from config.settings import BASE_DIR
from config.settings import DEFAULT_FROM_EMAIL
from book.models import Book, Author

def post_save_book(sender,instance,created,**kwargs):
    if created:
        print(f'Product {instance.book_name}  created ')
        subject = 'Product '
        message = f'SIZNING BAZANGIZDA  => {instance.book_name} NOMLI Product YARATILDI '
        for_email = DEFAULT_FROM_EMAIL
        to = 'nikola19testla98@gmail.com'
        send_mail(subject,message,for_email,[to,],fail_silently=False)
    else:
        print(f'Product {instance.product_name}  updated ')
post_save.connect(post_save_book,sender=Book)

def post_save_author(sender,instance,created,**kwargs):
    if created:
        print(f'Group {instance.full_name}  created ')
        subject = 'Group '
        message = f'SIZNING BAZANGIZDA  => {instance.full_name} NOMLI Group  YARATILDI '
        for_email = DEFAULT_FROM_EMAIL
        to = 'nikola19testla98@gmail.com'
        send_mail(subject,message,for_email,[to,],fail_silently=False)
    else:
        print(f'Group {instance.full_name}  updated ')
post_save.connect(post_save_author, sender=Author)


# DELETE
def pre_delet_book(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'book/delete/book', f'Product{instance.book_name}.json')
    category_data = {
        'id': instance.id,
        'Name': instance.product_name,
        'Price':instance.price,
        'Description':instance.description,
        'Quantity':instance.quantity,
        'Rating':instance.rating,
        'Slug': instance.slug,
    }
    with open(file_path, 'w') as json_file:
        json.dump(category_data, json_file, indent=4)


    print(f'Kiroblarni Ochirishdan oldin {instance.book_name}  json faylga saqlandi  ')
    subject = 'Book'
    message = f'SIZNING BAZANGIZDA  => {instance.book_name} NOMLI Product  O\'chirildi  VA olcha/delete/book papkaga malumotlar saqlandi'
    for_email = DEFAULT_FROM_EMAIL
    to = 'nikola19testla98@gmail.com'
    send_mail(subject, message, for_email, [to, ], fail_silently=False)
pre_delete.connect(pre_delet_book, sender=Book)

def pre_delet_auther(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'book/delete/author', f'Group{instance.id}.json')
    category_data = {
        'id': instance.id,
        'Full_name': instance.full_name,
        'Phone': instance.phone,
        'Adres': instance.adress,
        'Email': instance.email,
        'Slug': instance.slug,
    }
    with open(file_path, 'w') as json_file:
        json.dump(category_data, json_file, indent=4)
    print(f'Author Ochirishdan oldin {instance.full_name}  json faylga saqlandi  ')

    subject = 'Auther'
    message = f'SIZNING BAZANGIZDA  => {instance.full_name} NOMLI Group  O\'chirildi  VA book/delete/author papkaga malumotlar saqlandi '
    for_email = DEFAULT_FROM_EMAIL
    to = 'nikola19testla98@gmail.com'
    send_mail(subject, message, for_email, [to, ], fail_silently=False)
pre_delete.connect(pre_delet_auther, sender=Author)


