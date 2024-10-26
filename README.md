1. Используя команду cat в терминале операционной системы Linux, создать два файла Домашние животные (заполнив файл собаками, кошками, хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и ослы), а затем объединить их. Просмотреть содержимое созданного файла. Переименовать файл, дав ему новое имя (Друзья человека). 
2. Создать директорию, переместить файл туда. 
3. Подключить дополнительный репозиторий MySQL. Установить любой пакет из этого репозитория. 
4. Установить и удалить deb-пакет с помощью dpkg. 
5. Выложить историю команд в терминале ubuntu

 Задание: 1-5



230  cat > домашние_животные.txt <<EOL
Собака
Кошка
Хомяк
EOL

  231  cat > вьючные_животные.txt <<EOL
Лошадь
Верблюд
Осел
EOL

  232  cat домашние_животные.txt вьючные_животные.txt > друзья_человека.txt
  233  mv друзья_человека.txt друзья_человека_новый.txt
  234  cat друзья_человека_новый.txt
  235  mkdir питомник
  236  mv друзья_человека_новый.txt питомник/
  237  sudo apt update
  238  sudo apt install -y wget
  239  wget https://dev.mysql.com/get/mysql-apt-config_0.8.17-1_all.deb
  240  sudo dpkg -i mysql-apt-config_0.8.17-1_all.deb
  241  sudo apt update
  242  sudo apt install mysql-server
  243  sudo dpkg -i пакет.deb
  244  sudo dpkg -r пакет
  245  history > history_commands.txt

6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние животные и вьючные животные, в составы которых в случае домашних животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные войдут: Лошади, верблюды и ослы).

Диаграмма классов включает следующие элементы: 
Родительский класс Animal. 
Два подкласса: Pet (Домашние животные) и PackAnimal (Вьючные животные). 
Подклассы Pet включают Dog (Собаки), Cat (Кошки) и Hamster (Хомяки). 
Подклассы PackAnimal включают Horse (Лошади), Camel (Верблюды) и Donkey (Ослы).

7. В подключенном MySQL репозитории создать базу данных “Друзья человека” 
8. Создать таблицы с иерархией из диаграммы в БД 
9. Заполнить низкоуровневые таблицы именами(животных), командами которые они выполняют и датами рождения 
10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу. 
11.Создать новую таблицу “молодые животные” в которую попадут все животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью до месяца подсчитать возраст животных в новой таблице 
12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на прошлую принадлежность к старым таблицам.

 Задание: 7-12

CREATE DATABASE IF NOT EXISTS FriendsOfHuman;
USE FriendsOfHuman;

Переключение на базу данных FriendsOfHuman
USE FriendsOfHuman;

Таблица для хранения основных данных о животных (Animal)
CREATE TABLE IF NOT EXISTS Animal (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    birth_date DATE,
    type ENUM('Pet', 'PackAnimal') NOT NULL
);

Таблица для домашних животных (Pet)
CREATE TABLE IF NOT EXISTS Pet (
    animal_id INT PRIMARY KEY,
    species ENUM('Dog', 'Cat', 'Hamster') NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES Animal(id)
);

Таблица для вьючных животных (PackAnimal)
CREATE TABLE IF NOT EXISTS PackAnimal (
    animal_id INT PRIMARY KEY,
    species ENUM('Horse', 'Camel', 'Donkey') NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES Animal(id)
);

Таблица для команд домашних животных (PetCommands)
CREATE TABLE IF NOT EXISTS PetCommands (
    animal_id INT,
    command VARCHAR(50) NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES Pet(animal_id)
);

Таблица для команд вьючных животных (PackAnimalCommands)
CREATE TABLE IF NOT EXISTS PackAnimalCommands (
    animal_id INT,
    command VARCHAR(50) NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES PackAnimal(animal_id)
);

Добавление животных в таблицу Animal
INSERT INTO Animal (name, birth_date, type) VALUES 
('Buddy', '2020-05-10', 'Pet'),
('Whiskers', '2021-06-15', 'Pet'),
('Sparky', '2021-03-20', 'Pet'),
('Thunder', '2019-07-01', 'PackAnimal'),
('Sandy', '2020-11-25', 'PackAnimal'),
('Hector', '2021-09-14', 'PackAnimal');

Заполнение таблицы Pet
INSERT INTO Pet (animal_id, species) VALUES 
(1, 'Dog'), 
(2, 'Cat'), 
(3, 'Hamster');

Заполнение таблицы PackAnimal (включая верблюда, которого удалим на следующем шаге)
INSERT INTO PackAnimal (animal_id, species) VALUES 
(4, 'Horse'), 
(5, 'Camel'), 
(6, 'Donkey');

Заполнение команд для домашних животных в таблице PetCommands
INSERT INTO PetCommands (animal_id, command) VALUES 
(1, 'Sit'), 
(1, 'Stay'), 
(1, 'Fetch'), 
(2, 'Climb'), 
(3, 'Run in wheel');

Заполнение команд для вьючных животных в таблице PackAnimalCommands
INSERT INTO PackAnimalCommands (animal_id, command) VALUES 
(4, 'Gallop'), 
(4, 'Pull cart'), 
(5, 'Carry load'), 
(6, 'Pull cart');

Удаление всех верблюдов из таблицы PackAnimal
DELETE FROM PackAnimal WHERE species = 'Camel';

Создание объединённой таблицы для лошадей и ослов
CREATE TABLE IF NOT EXISTS HorseAndDonkey (
    animal_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    birth_date DATE,
    species ENUM('Horse', 'Donkey'),
    FOREIGN KEY (animal_id) REFERENCES Animal(id)
);

Перенос данных о лошадях и ослах из таблицы PackAnimal в HorseAndDonkey
INSERT INTO HorseAndDonkey (animal_id, name, birth_date, species)
SELECT a.id, a.name, a.birth_date, p.species
FROM Animal a
JOIN PackAnimal p ON a.id = p.animal_id
WHERE p.species IN ('Horse', 'Donkey');

DELETE FROM PackAnimal WHERE species IN ('Horse', 'Donkey');

Создание таблицы "молодые животные" (YoungAnimals)
CREATE TABLE IF NOT EXISTS YoungAnimals (
    animal_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    species VARCHAR(50),
    age_in_months INT,
    FOREIGN KEY (animal_id) REFERENCES Animal(id)
);

Заполнение таблицы "YoungAnimals" животными, которым от 1 до 3 лет
INSERT INTO YoungAnimals (animal_id, name, birth_date, species, age_in_months)
SELECT a.id, a.name, a.birth_date, 
       COALESCE(p.species, pa.species) AS species,
       TIMESTAMPDIFF(MONTH, a.birth_date, CURDATE()) AS age_in_months
FROM Animal a
LEFT JOIN Pet p ON a.id = p.animal_id
LEFT JOIN PackAnimal pa ON a.id = pa.animal_id
WHERE TIMESTAMPDIFF(YEAR, a.birth_date, CURDATE()) BETWEEN 1 AND 2;

Создание объединённой таблицы "AllAnimals"
CREATE TABLE IF NOT EXISTS AllAnimals (
    animal_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    species VARCHAR(50),
    age_in_months INT,
    source_table VARCHAR(20) 
);

Заполнение объединённой таблицы данными из таблиц Animal, Pet, PackAnimal и YoungAnimals

Вставка данных из таблицы Pet
INSERT INTO AllAnimals (animal_id, name, birth_date, species, source_table)
SELECT a.id, a.name, a.birth_date, p.species, 'Pet'
FROM Animal a
JOIN Pet p ON a.id = p.animal_id;

Вставка данных из таблицы PackAnimal
INSERT INTO AllAnimals (animal_id, name, birth_date, species, source_table)
SELECT a.id, a.name, a.birth_date, pa.species, 'PackAnimal'
FROM Animal a
JOIN PackAnimal pa ON a.id = pa.animal_id;

Вставка данных из таблицы YoungAnimals
INSERT INTO AllAnimals (animal_id, name, birth_date, species, age_in_months, source_table)
SELECT ya.animal_id, ya.name, ya.birth_date, ya.species, ya.age_in_months, 'YoungAnimals'
FROM YoungAnimals ya;

13.Создать класс с Инкапсуляцией методов и наследованием по диаграмме.

14. Написать программу, имитирующую работу реестра домашних животных. В программе должен быть реализован следующий функционал: 
14.1 Завести новое животное 
14.2 определять животное в правильный класс 
14.3 увидеть список команд, которое выполняет животное 
14.4 обучить животное новым командам 
14.5 Реализовать навигацию по меню 

15.Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆ значение внутренней̆int переменной̆на 1 при нажатие “Завести новое животное” Сделайте так, чтобы с объектом такого типа можно было работать в блоке try-with-resources. Нужно бросить исключение, если работа с объектом типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение считать в ресурсе try, если при заведения животного заполнены все поля.

























