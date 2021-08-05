/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.6.24 : Database - 公安局人员管理系统
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`公安局人员管理系统` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `公安局人员管理系统`;

/*Table structure for table `local` */

DROP TABLE IF EXISTS `local`;

CREATE TABLE `local` (
  `id` varchar(40) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `passwd` varchar(20) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL,
  `province` varchar(20) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `door` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `immi` date DEFAULT NULL,
  `credit` int(11) DEFAULT NULL,
  `culture` int(11) DEFAULT NULL,
  `learn_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `local` */

insert  into `local`(`id`,`name`,`sex`,`age`,`passwd`,`status`,`country`,`province`,`street`,`door`,`date`,`immi`,`credit`,`culture`,`learn_num`) values ('5wxtaahvkrzglbsvrhil7rts5v3n2g32','李四','女',54,'123123',1,'中国','上海','东方明珠','A002','2021-08-05',NULL,2,0,0),('7iyg5qes8t5ckvhe61ow4kgm2vwpjrcy','赵瑞','男',21,'123456',1,'中国','北京','中关村','s001','2021-08-05','2021-08-05',2,0,0),('admin',NULL,NULL,NULL,'admin1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('n3ryjagpevnm4i7tkzt6pvr1pml6fjwd','赵瑞','男',21,'123456',1,'中国','北京','中关村','s001','2021-08-05',NULL,2,0,0),('ncfs2r4xnrshgm3hmyvvyb8qpelele5r','张三','男',32,'123654',1,'中国','北京','积水潭','A001','2021-08-05',NULL,2,0,0),('z28byxxgsq3wqx82c8wsulpahkovebn7','赵瑞','男',21,'123456',1,'中国','北京','中关村','s001','2021-08-05',NULL,2,0,0);

/*Table structure for table `state` */

DROP TABLE IF EXISTS `state`;

CREATE TABLE `state` (
  `id` varchar(40) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `passwd` varchar(20) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL,
  `province` varchar(20) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `door` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `immi` date DEFAULT NULL,
  `credit` int(11) DEFAULT NULL,
  `culture` int(11) DEFAULT NULL,
  `learn_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `state` */

insert  into `state`(`id`,`name`,`sex`,`age`,`passwd`,`status`,`country`,`province`,`street`,`door`,`date`,`immi`,`credit`,`culture`,`learn_num`) values ('5wxtaahvkrzglbsvrhil7rts5v3n2g32','李四','女',54,'123123',1,'中国','上海','东方明珠','A002','2021-08-05',NULL,2,0,0),('7iyg5qes8t5ckvhe61ow4kgm2vwpjrcy','赵瑞','男',21,'123456',1,'中国','北京','中关村','s001','2021-08-05','2021-08-05',2,0,0),('admin',NULL,NULL,NULL,'admin2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('n3ryjagpevnm4i7tkzt6pvr1pml6fjwd','赵瑞','男',21,'123456',1,'中国','北京','中关村','s001','2021-08-05',NULL,2,0,0),('ncfs2r4xnrshgm3hmyvvyb8qpelele5r','张三','男',32,'123654',1,'中国','北京','积水潭','A001','2021-08-05',NULL,2,0,0),('z28byxxgsq3wqx82c8wsulpahkovebn7','赵瑞','男',21,'123456',1,'中国','北京','中关村','s001','2021-08-05',NULL,2,0,0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
