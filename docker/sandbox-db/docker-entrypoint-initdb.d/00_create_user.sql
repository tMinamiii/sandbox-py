CREATE USER 'user'@'%' IDENTIFIED BY 'passwd00';
GRANT ALL ON *.* TO 'user'@'%';
CREATE DATABASE IF NOT EXISTS `sandbox`;
