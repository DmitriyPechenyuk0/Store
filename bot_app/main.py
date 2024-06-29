import sqlite3, telebot, os, re

bot = telebot.TeleBot(token= "")

# 0 - id, 1 - login, 2-email, 3-password, 4-is_admin

get_users = telebot.types.InlineKeyboardButton(text='GET USERS', callback_data='get_users')
get_product = telebot.types.InlineKeyboardButton(text='GET PRODUCTS', callback_data='get_products')
add_product = telebot.types.InlineKeyboardButton(text='ADD PRODUCT', callback_data='add_product')

ye = telebot.types.InlineKeyboardButton(text='Yes', callback_data='yes')
no = telebot.types.InlineKeyboardButton(text='No', callback_data='no')

keyboard = telebot.types.InlineKeyboardMarkup(keyboard=[[get_users, get_product, add_product]], row_width=2)

modal_messages = {}

user_states = {}
STATE_WAITING_FOR_PRODUCT = 1

abspath = os.path.abspath(__file__ + '/../../project/data.db')

connect = sqlite3.connect(database=abspath, check_same_thread=False)

cursor = connect.cursor()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id = message.chat.id, text = F'<b>Привіт, користувач</b>', reply_markup = keyboard, parse_mode='html')


@bot.callback_query_handler(func=lambda callback: True)
def handle_query(callback):
    # print(callback)
    #if callback.message.chat.id == :
    #if callback.data == 'get_users':
    #    bot.send_message(chat_id=callback.message.chat.id, text=f" id: {l[0][0]}\n login: {l[0][1]}\n email:{l[0][2]}\n password: {l[0][3]}\n is_admin:{l[0][4]}")
    if callback.data == 'get_users':
        cursor.execute('SELECT * FROM user')
        users = cursor.fetchall()
        
        for user in users:

            global user_id, login, email, is_admin

            user_id = user[0]
            login = user[1]
            email = user[2]
            is_admin = user[4]

            global delete_button, make_admin_button, remove_admin_button, user_markup
            
            delete_button = telebot.types.InlineKeyboardButton(text='Видалити користувача', callback_data=f'delete_user_{user_id}') #f'delete_{user_id}'
            make_admin_button = telebot.types.InlineKeyboardButton(text='Видати адміна', callback_data=f'give_admin_{user_id}') #f'give_admin_{user_id}'
            remove_admin_button = telebot.types.InlineKeyboardButton(text='Забрати адміна', callback_data=f'remove_admin_{user_id}') #f'remove_admin_{user_id}'

            user_markup = telebot.types.InlineKeyboardMarkup(keyboard=[[delete_button, make_admin_button, remove_admin_button]], row_width=2)

            bot.send_message(chat_id=callback.message.chat.id,
                            message_thread_id=2,
                            text=f"ID: {user_id}\nlogin: {login}\nemail: {email}\nadmin: {is_admin}",
                            reply_markup=user_markup)
            
    elif callback.data.startswith('delete_user_'):

        confirm_button = telebot.types.InlineKeyboardButton(text='Видалити', callback_data=f'confirm_and_delete_user_{user_id}')
        cancel_button = telebot.types.InlineKeyboardButton(text='Відмінити', callback_data='cancel_deletion')

        user_deletion_confirm_markup = telebot.types.InlineKeyboardMarkup(keyboard=[[confirm_button, cancel_button]], row_width=2)

        modal_message = bot.send_message(
            chat_id = callback.message.chat.id,
            text = F'<b>Видалити користувача?</b>',
            message_thread_id=2,
            reply_markup = user_deletion_confirm_markup, parse_mode='html')

        modal_messages[callback.message.chat.id] = modal_message.message_id

    elif callback.data.startswith('confirm_and_delete_user_'):
        user_id1 = callback.data
        match = re.search(r'\d+', user_id1)
        if match:
            user_id1 = int(match.group())
            # bot.send_message(chat_id=callback.message.chat.id, message_thread_id=2, text=user_id1)
            try:
                cursor.execute('DELETE FROM user WHERE id = ?', (user_id1,))
                connect.commit()
                if callback.message.chat.id in modal_messages:
                    bot.delete_message(chat_id=callback.message.chat.id, message_id=modal_messages[callback.message.chat.id])
                    del modal_messages[callback.message.chat.id]
    
                bot.send_message(chat_id = callback.message.chat.id, text = F'<b>Користувач з id: {user_id1} видален</b>', parse_mode='html')
            except Exception as e:
                bot.send_message(chat_id = callback.message.chat.id, text = f'Помилка {e}')

    elif callback.data == 'cancel_deletion':
        if callback.message.chat.id in modal_messages:
            bot.delete_message(chat_id=callback.message.chat.id, message_thread_id=2, message_id=modal_messages[callback.message.chat.id])
            del modal_messages[callback.message.chat.id]

        bot.send_message(chat_id = callback.message.chat.id,message_thread_id=2, text = F'<b>Відмінено</b>', parse_mode='html')

    elif callback.data.startswith('give_admin_'):
        user_id1 = callback.data
        match = re.search(r'\d+', user_id1)
        if match:
            user_id1 = int(match.group())
            try:
                cursor.execute('UPDATE user SET is_admin = 1 WHERE id = ?', (user_id1))
                connect.commit()

                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                    text=f"ID: {user_id}\nlogin: {login}\nemail: {email}\nadmin: {is_admin}",
                    reply_markup=user_markup)
            except Exception as e:
                bot.send_message(chat_id = callback.message.chat.id, text = f'Помилка {e}')

    elif callback.data.startswith('remove_admin_'):
        user_id1 = callback.data
        match = re.search(r'\d+', user_id1)
        if match:
            user_id1 = int(match.group())
            try:
                cursor.execute('UPDATE user SET is_admin = 0 WHERE id = ?', (user_id1))
                connect.commit()
    
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                    text=f"ID: {user_id}\nlogin: {login}\nemail: {email}\nadmin: {is_admin}",
                    reply_markup=user_markup)
            except Exception as e:
                bot.send_message(chat_id = callback.message.chat.id, text = f'Помилка {e}')



    elif callback.data == 'get_products':
        cursor.execute('SELECT * from product')
        products = cursor.fetchall()

        for product in products:

            
            global product_id, name, discount, price, count

            product_id = product[0]
            name = product[1]
            discount = product[2]
            price = product[3]
            count = product[4]

            delete_product_button = telebot.types.InlineKeyboardButton(text='Видалити', callback_data=f'delete_product_{product_id}')

            product_markup = telebot.types.InlineKeyboardMarkup(keyboard=[[delete_product_button]], row_width=2)

            bot.send_message(chat_id=callback.message.chat.id,
                            message_thread_id=6,
                            text=f"<b>name: {name}</b>\n\ndiscount: {discount}\nprice: {price}\ncount: {count}",
                            reply_markup=product_markup,
                            parse_mode='html')
            
    elif callback.data.startswith('delete_product_'):
        product_id1 = callback.data
        match = re.search(r'\d+', product_id1)
        if match:
            product_id1 = int(match.group())
            try:
                cursor.execute('DELETE FROM product WHERE id = ?', (product_id1,))
                connect.commit()

                bot.send_message(chat_id = callback.message.chat.id, text = f'Продукт видалений {product_id1}')
            except Exception as e:
                bot.send_message(chat_id = callback.message.chat.id, text = f'Помилка {e}')

    #elif callback.data == 'add_product':
#
#
    #    user_states[callback.message.chat.id] = STATE_WAITING_FOR_PRODUCT
#
    #    add_product_button = telebot.types.InlineKeyboardButton(text='Додати', callback_data='confirm_product')
#
    #    add_product_markup = telebot.types.InlineKeyboardMarkup(keyboard=[[add_product_button]], row_width=2)
#
    #    bot.send_message(chat_id = callback.message.chat.id, text = 'Прикріпіть зображення продукту потім назву, ціну, знижку, короткий опис та кількість', reply_markup=add_product_markup)
#
    #elif callback.data == 'confirm_product':
    #    if callback.message.chat.id in user_states:
    #        if user_states[callback.message.chat.id] == STATE_WAITING_FOR_PRODUCT:
    #            msg = callback.message.text.strip()
#
    #            # Разделяем строки и убираем пустые строки
    #            lines = [line.strip() for line in msg.split('\n') if line.strip()]
#
    #            if len(lines) != 5:
    #                bot.send_message(chat_id=callback.message.chat.id, text="Помилка: текст має містити рівно 5 строк.")
    #                bot.send_message(chat_id=callback.message.chat.id, text=msg)
    #                return
#
    #            try:
    #                name = lines[0]
    #                price = float(lines[1])
    #                discount = float(lines[2])
    #                description = lines[3]
    #                quantity = int(lines[4])
#
    #                cursor.execute('''
    #                    INSERT INTO products (name, price, discount, description, count)
    #                    VALUES (?, ?, ?, ?, ?)
    #                ''', (name, price, discount, description, quantity))
#
    #                connect.commit()
    #                bot.send_message(chat_id=callback.message.chat.id, text="Продукт успішно додано.")
    #            except ValueError:
    #                bot.send_message(chat_id=callback.message.chat.id, text="Помилка: не вдалося обробити числові значення. Перевірте формат цін, знижки та кількості.")
    #            except Exception as e:
    #                bot.send_message(chat_id=callback.message.chat.id, text=f"Помилка: {e}")
#

    elif callback.data == 'add_product':
        user_states[callback.message.chat.id] = STATE_WAITING_FOR_PRODUCT
        bot.send_message(chat_id=callback.message.chat.id, text='Пришліть назву, ціну, знижку, короткий опис та кількість через нове повідомлення (по одному значению на строку).')

@bot.message_handler(func=lambda message: message.chat.id in user_states and user_states[message.chat.id] == STATE_WAITING_FOR_PRODUCT)
def receive_product_info(message):
    msg = message.text.strip()

    lines = [line.strip() for line in msg.split('\n') if line.strip()]

    if len(lines) != 5:
        bot.send_message(chat_id=message.chat.id, text="Помилка: текст має містити рівно 5 строк.")
        return

    try:
        name = lines[0]
        price = float(lines[1])
        discount = float(lines[2])
        description = lines[3]
        quantity = int(lines[4])

        cursor.execute('''
            INSERT INTO product (name, discount, price, count)
            VALUES (?, ?, ?, ?)
        ''', (name, discount, price, quantity))

        connect.commit()
        bot.send_message(chat_id=message.chat.id, text="Продукт успішно додано.")
        bot.send_message(chat_id=message.chat.id, text=f"<b>name: {name}</b>\n\ndiscount: {discount}\ndescription: {description}\nprice: {price}\ncount: {quantity}", parse_mode="html")
        del user_states[message.chat.id]  # Удаляем состояние после успешного добавления продукта
    except ValueError:
        bot.send_message(chat_id=message.chat.id, text="Помилка: не вдалося обробити числові значення. Перевірте формат цін, знижки та кількості.")
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f"Помилка: {e}")
        

bot.infinity_polling()
connect.close()
