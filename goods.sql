USE fxjdb;

SET NAMES utf8;

CREATE DATABASE IF NOT EXISTS fxjdb DEFAULT CHARACTER SET utf8;

CREATE TABLE fxjdb.goods (
	pid INT UNSIGNED AUTO_INCREMENT,
	pcode VARCHAR(255) NOT NULL UNIQUE,
	pname VARCHAR(50) NOT NULL,
	price CHAR(11) NOT NULL,
	pnumber varchar(255) NOT NULL,
	PRIMARY KEY (pid)
) ENGINE=INNODB AUTO_INCREMENT=1000 DEFAULT CHARACTER SET utf8;


DESC goods;


-- CREATE USER 'dj'@'127.0.0.1' IDENTIFIED BY '123456';
-- GRANT ALL ON mydb.* to 'dj'@'127.0.0.1';
-- FLUSH PRIVILEGES;


-- 创建新用户
-- create user 'dj'@'%' identified by 'abc123';

-- 创建数据库
-- create database mydb default character set utf8;

-- 给用户授权
-- grant all on mydb.* to 'dj'@'%';

-- 刷新授权
-- flush privileges;

-- 查看用户
--select host,user from mysql.user; 

-- 重命名   
-- rename user dj to jj;

-- 修改密码
-- set password for 'jj'@'%' = password('123456')
