-- 创建数据库
CREATE DATABASE IF NOT EXISTS restful_db;

-- 使用数据库
USE restful_db;

-- 创建表
create table 'books' (
  'id' int not null primary key auto_increment,
  'name' varchar(255) not null unique,
   'author' varchar(255) not null,
    'publish_time' timestamp not null
);

-- 查询验证
SELECT * FROM `books`;


-- 创建用户表
CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

insert into users(id, username, password) values(1, 'Jacke', '123456');