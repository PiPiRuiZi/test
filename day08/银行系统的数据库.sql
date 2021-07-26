/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.6.24 : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bank`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `money` int(10) unsigned DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL,
  `province` varchar(20) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `door` varchar(20) DEFAULT NULL,
  `bank_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`,`money`,`country`,`province`,`street`,`door`,`bank_name`) values (10000001,'test1','123456',9394,'中国','北京','沙河镇街道','s001','中国建设银行昌平支行'),(10000002,'test2','654321',20611,'中国','北京','回龙观街道','s002','中国建设银行昌平支行'),(10000003,'test3','123456',30000,'中国','北京','中关村街道','s003','中国建设银行昌平支行'),(45214284,'1','1',1,'1','1','1','1','中国建设银行昌平支行'),(48787682,'zhaorui','111111',200,'中国','北京','天安门','003','中国建设银行昌平支行'),(82763832,'李白','123456',1230,'中国','河北','实际安装','的说法','中国建设银行昌平支行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
