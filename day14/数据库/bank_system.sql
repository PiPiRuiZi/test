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

insert  into `user`(`id`,`username`,`password`,`money`,`country`,`province`,`street`,`door`,`bank_name`) values (10000001,'test1','123456',8400,'中国','北京','沙河镇街道','s001','中国建设银行昌平支行'),(10000002,'test2','654321',4294967285,'中国','北京','回龙观街道','s002','中国建设银行昌平支行'),(10000003,'test3','123456',30000,'中国','北京','中关村街道','s003','中国建设银行昌平支行'),(10288083,'张三2','123456',993,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(10796329,'张三2','123456',996,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(11859218,'张三','123456',70,'中国','上海','太白路','d001','中国建设银行昌平支行'),(12628839,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(12889709,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(13542226,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(13774475,'张三','123456',40,'中国','上海','太白路','d001','中国建设银行昌平支行'),(18583339,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(19343052,'张三1','123456',983,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(20213324,'张三2','123456',978,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(21890963,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(22155841,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(22482582,'张三3','123456',1010,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(23730200,'张三2','123456',1008,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(24113989,'张三1','123456',1031,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(24140878,'张三','123456',160,'中国','上海','太白路','d001','中国建设银行昌平支行'),(24761959,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(25213726,'张三3','123456',1021,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(26147889,'张三','123456',124,'中国','上海','太白路','d001','中国建设银行昌平支行'),(27032967,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(29121316,'张三2','123456',995,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(30140118,'张三2','123456',1002,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(30596696,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(32990163,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(33202808,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(33653761,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(34257471,'张三3','123456',2203,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(34689319,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(35003568,'张三2','123456',1002,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(35853952,'张三2','123456',1002,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(35882987,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(35962168,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(36303397,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(36556850,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(37603329,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(38437134,'张三2','123456',1002,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(38776705,'张三2','123456',1002,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(39514372,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(40293083,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(41029324,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(41268277,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(41639673,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(43302505,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(43860937,'张三2','123456',1002,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(44303833,'张三3','123456',1003,'中国3','上海3','太白路3','d0013','中国建设银行昌平支行'),(46314771,'张三1','123456',1001,'中国1','上海1','太白路1','d0011','中国建设银行昌平支行'),(47144519,'张三2','123456',1002,'中国2','上海2','太白路2','d0012','中国建设银行昌平支行'),(47686321,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(48375077,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(48787682,'赵瑞','111111',200,'中国','北京','天安门街道','s004','中国建设银行昌平支行'),(49708813,'张三','123456',100,'中国','上海','太白路','d001','中国建设银行昌平支行'),(95338785,'10000001','123456',66,'5','1','1','1','中国建设银行昌平支行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
