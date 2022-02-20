#Installation

docker-compose up --build

#Run

docker-compose up

#Usage

0.0.0.0:8000/deals

Для отправки файла через POST-запрос необходимо перейти 
на страницу и прикрепить файл в поле.

Для получения обработанных данных необходимо отправить 
GET-запрос.

#Errors description

- The submitted data was not a file. Check the encoding type on the form. Файл не был прикреплен в соответсвующее поле.
- В процессе обработки файла произошла ошибка. Файл содержит некоректные 
  данные.
