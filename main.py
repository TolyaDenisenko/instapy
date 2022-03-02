from instapy import InstaPy

insta_username = 'Ваш логин или фэйковый логин'
insta_password = 'Пароль от вашего акк'

# Введите свой или фейковый аккаунт и пароль дл бота(username="instagram", password="test1234")

session = InstaPy(username=insta_username, password=insta_password, browser_profile_path=False)

session.login()

session.set_do_comment(True, percentage=100)
session.set_user_interact(amount=70, randomize=True )
#Укажите список комментов которые хотите использовать. стиль оформления, ' текст ',
session.set_comments(['В нашей стране война! Путин -зло! Ваши новости обманывают Вас!','Лукашенко -мразь! Кремлевская подстилка! Лукашенко и его войско убивает мирных людей','Путин сдался, Украина победила','Путин застрелился у себя в бункере на Урале'])
session.like_by_tags(['россия', 'москва', 'россиясуппер', 'раша', 'белорусь', 'минск', 'московия' , 'путлер' , 'путиннаш' , 'русскиегерои' , 'russia' , 'russian' , 'moskva' , 'minsk','russianhero'])

#Засрем в ответку русского захватчика! Слава Украине!
