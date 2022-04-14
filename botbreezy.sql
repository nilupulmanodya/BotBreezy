-- MySQL dump 10.17  Distrib 10.3.23-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: botbreezy
-- ------------------------------------------------------
-- Server version	10.3.23-MariaDB-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$7yzunkRFRzzu0tzsGJ0s9f$My0m3d58SOZLXZFk5whBCXJNCVqRuIgjGfGdSPKA1O0=','2022-04-04 17:41:03.208800',1,'admin','','','admin@admin.com',1,1,'2022-03-06 19:05:37.067838');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `career_info`
--

DROP TABLE IF EXISTS `career_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `career_info` (
  `course_label` varchar(50) DEFAULT NULL,
  `course_des` varchar(10000) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `career_info`
--

LOCK TABLES `career_info` WRITE;
/*!40000 ALTER TABLE `career_info` DISABLE KEYS */;
INSERT INTO `career_info` VALUES ('bme','If you want to combine your love for engineering with the ability to design life-saving medical products, a career in biomedical engineering may be your calling. Advances in technology and the need to care for an aging population make biomedical engineers one of the most in-demand positions in the country. Their are so many career prospects including Biomaterials Developer, Manufacturing Engineer, Independent Consultant, Doctor, Biomedical Scientist/Researcher, Rehabilitation Engineer, and Medical Technology Developer.',1),('ccs','Common employers are IT consultancies and IT service providers. However, as most businesses rely on computers to function effectively, there are also opportunities within the IT departments of major organisations in many sectors. Based on your talents you can choose many job options Application analyst, Applications developer, Cyber security analyst, Data analyst, Database dministrator, Forensic computer analyst, Game designer, Games developer, Information systems manager, IT consultant, Software engineer, Systems analyst, UX designer, Web designer, and Web developer.',2);
/*!40000 ALTER TABLE `career_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_info`
--

DROP TABLE IF EXISTS `course_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course_info` (
  `course_name` varchar(50) DEFAULT NULL,
  `info` varchar(200) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_info`
--

LOCK TABLES `course_info` WRITE;
/*!40000 ALTER TABLE `course_info` DISABLE KEYS */;
INSERT INTO `course_info` VALUES ('bme','Biomedical engineering program comprises study about tissue engineering, molecular or systems level biology/ physiology and mathematics.',1),('cs','Computer science is the study of computers and computing as well as their theoretical and practical applications. Computer science applies the principles of mathematics and engineering',2);
/*!40000 ALTER TABLE `course_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(8,'admin_server','careerinfo'),(13,'admin_server','courseinfo'),(9,'admin_server','entryinfo'),(12,'admin_server','eventregistrations'),(15,'admin_server','facultyinfo'),(10,'admin_server','hostelinfo'),(14,'admin_server','students'),(7,'admin_server','testtable'),(11,'admin_server','uniinfodes'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-03-06 19:03:50.185800'),(2,'auth','0001_initial','2022-03-06 19:04:11.471061'),(3,'admin','0001_initial','2022-03-06 19:04:19.559845'),(4,'admin','0002_logentry_remove_auto_add','2022-03-06 19:04:19.652964'),(5,'admin','0003_logentry_add_action_flag_choices','2022-03-06 19:04:19.798499'),(6,'contenttypes','0002_remove_content_type_name','2022-03-06 19:04:22.608712'),(7,'auth','0002_alter_permission_name_max_length','2022-03-06 19:04:25.987333'),(8,'auth','0003_alter_user_email_max_length','2022-03-06 19:04:26.197418'),(9,'auth','0004_alter_user_username_opts','2022-03-06 19:04:26.313349'),(10,'auth','0005_alter_user_last_login_null','2022-03-06 19:04:27.649951'),(11,'auth','0006_require_contenttypes_0002','2022-03-06 19:04:27.802462'),(12,'auth','0007_alter_validators_add_error_messages','2022-03-06 19:04:27.971949'),(13,'auth','0008_alter_user_username_max_length','2022-03-06 19:04:31.940681'),(14,'auth','0009_alter_user_last_name_max_length','2022-03-06 19:04:33.987581'),(15,'auth','0010_alter_group_name_max_length','2022-03-06 19:04:34.120582'),(16,'auth','0011_update_proxy_permissions','2022-03-06 19:04:34.203998'),(17,'auth','0012_alter_user_first_name_max_length','2022-03-06 19:04:36.419454'),(18,'sessions','0001_initial','2022-03-06 19:04:38.566417');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('29strx223ggdl29308ndd3hhn8t6k0m8','.eJxVjDsOwjAQBe_iGlne-Icp6XMGa-3d4ACypTipEHeHSCmgfTPzXiLitpa4dV7iTOIiQJx-t4T5wXUHdMd6azK3ui5zkrsiD9rl2Iif18P9OyjYy7c2mM-oDJmEVjkCZJUnQu9h0GQ1pslpYwdPDpwjp4A56JAoZEbywOL9AfcoOH8:1nbQhL:JKFTGICDpprwbG3c8V4jjOJa1kw46Q5EsN3GVHemVEw','2022-04-18 17:41:03.274890'),('6919ak1m9xwcy24jb7k3pudni50xga9s','.eJxVjDsOwjAQBe_iGlne-Icp6XMGa-3d4ACypTipEHeHSCmgfTPzXiLitpa4dV7iTOIiQJx-t4T5wXUHdMd6azK3ui5zkrsiD9rl2Iif18P9OyjYy7c2mM-oDJmEVjkCZJUnQu9h0GQ1pslpYwdPDpwjp4A56JAoZEbywOL9AfcoOH8:1nQx3M:EkRqUNtKdGQ8i1hM7NYgdGo-FopLVxYPUPHODyfY4ss','2022-03-20 20:00:28.542561');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entry_info`
--

DROP TABLE IF EXISTS `entry_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entry_info` (
  `course_label` varchar(50) DEFAULT NULL,
  `course_des` varchar(10000) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entry_info`
--

LOCK TABLES `entry_info` WRITE;
/*!40000 ALTER TABLE `entry_info` DISABLE KEYS */;
INSERT INTO `entry_info` VALUES ('bme','To get on to a bio medical engineering degree, you require a minimum of two A levels, with three A levels and A/B grades required. Entry requirements range from CCC to AAA. and Demo university will give priority to Z-score as well.',1),('ccs','To get on to a computer science degree, you require a minimum of two A levels, with three A levels and A/B grades required. Entry requirements range from CCC to AAA. and Demo university will give priority to Z-score aswell.',2);
/*!40000 ALTER TABLE `entry_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_info`
--

DROP TABLE IF EXISTS `event_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event_info` (
  `event_label` varchar(50) DEFAULT NULL,
  `event_des` varchar(10000) DEFAULT NULL,
  `id` int(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_info`
--

LOCK TABLES `event_info` WRITE;
/*!40000 ALTER TABLE `event_info` DISABLE KEYS */;
INSERT INTO `event_info` VALUES ('rbd','The Robotics Day is most comprehensive exhibition on robotics for service sectors. The Robotics Day brings together industry, researchers, investors, engineers and students to exchange and share experiences, new ideas, and technologies. Matchmaking sessions facilitate collaborations and partnerships. Presentations of distinguished speakers will focus on innovative technologies, new market trends for robots, logistics, the future of aerial robotics and robots in healthcare. It will be held on 23rd March 2023 at Demo University premises.',NULL),('ine','Invention Exhibition, the Invention & New Product Exposition, is  Largest invention trade show of Demo University. Invention Exhibition provides a forum for inventors to exhibit their inventions and attempt to make contacts with companies interested in licensing, marketing or manufacturing new products. Event will be held on 28th February at the Demo University premises.',NULL);
/*!40000 ALTER TABLE `event_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event_registrations`
--

DROP TABLE IF EXISTS `event_registrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event_registrations` (
  `event_name` varchar(500) NOT NULL,
  `student_reg_no` varchar(10) NOT NULL,
  `is_sent_email` bit(1) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_registrations`
--

LOCK TABLES `event_registrations` WRITE;
/*!40000 ALTER TABLE `event_registrations` DISABLE KEYS */;
INSERT INTO `event_registrations` VALUES ('test_event','S333','\0',1),('test_event','S333','',2),('test_event','S333','\0',3),('test_event_server','S456456','',4),('test_event_server','S456456','',5),('Invention Exhibition','S123','',6),('Invention Exhibition','S123','',7),('Robotics Day','S123','',8),('Invention Exhibition','S123','',9);
/*!40000 ALTER TABLE `event_registrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty_info`
--

DROP TABLE IF EXISTS `faculty_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `faculty_info` (
  `fac_lbl_name` varchar(500) DEFAULT NULL,
  `fac_info` varchar(1000) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty_info`
--

LOCK TABLES `faculty_info` WRITE;
/*!40000 ALTER TABLE `faculty_info` DISABLE KEYS */;
INSERT INTO `faculty_info` VALUES ('foe','The Faculty of Engineering of DEMO University was established on 1st July 1999 Colombo. First batch of students was admitted on 27th March 2000. Admission to the Faculty of Engineering, is subject to the University Grants Commission policy on university admissions. The present annual intake to the Faculty is 530. The Faculty of Engineering offers full-time courses leading to the Degree of Bachelor of the Science of Engineering (B.Sc.Eng.), which is accredited by the Institution of Engineers, Sri Lanka (IESL).',1),('foc','The Faculty of Computing of DEMO University was established on 1st March 2000 Colombo. First batch of students was admitted on 27th March 2001. Admission to the Faculty of Engineering, is subject to the University Grants Commission policy on university admissions. The present annual intake to the Faculty is 800. The Faculty of Computing offers full-time courses leading to the Degree of Bachelor of the Science (B.Sc.).',2);
/*!40000 ALTER TABLE `faculty_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostel_info`
--

DROP TABLE IF EXISTS `hostel_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hostel_info` (
  `hos_info_name` varchar(50) DEFAULT NULL,
  `hos_des` varchar(1000) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostel_info`
--

LOCK TABLES `hostel_info` WRITE;
/*!40000 ALTER TABLE `hostel_info` DISABLE KEYS */;
INSERT INTO `hostel_info` VALUES ('hos_info_1','Demo University offers students hostels with huge facilities, You can use Swimming pools, Gym, Canteens, Grounds and free Wifi in each hostels. You can request your prefer hostel while applying hostel forms.',1);
/*!40000 ALTER TABLE `hostel_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sports_info`
--

DROP TABLE IF EXISTS `sports_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sports_info` (
  `sport_name` varchar(50) DEFAULT NULL,
  `sport_des` varchar(6000) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sports_info`
--

LOCK TABLES `sports_info` WRITE;
/*!40000 ALTER TABLE `sports_info` DISABLE KEYS */;
INSERT INTO `sports_info` VALUES ('krt','karate, (Japanese: empty hand) unarmed martial-arts discipline employing kicking, striking, and defensive blocking with arms and legs. Emphasis is on concentrating as much of the body\'s power as possible at the point and instant of impact... Demo University give oppertunity to training karate with high experience staff.The practice were sheduled in every saturday evening at 7.00pm at University Sport complex.',1),('cri','Cricket is a bat-and-ball game played between two teams of eleven players each on a field at the centre of which is a 22-yard pitch with a wicket at each end, each comprising two bails balanced on three stumps. Demo university cricket team able to won inter university games cricket champion ship in 2021. The practice were sheduled in every week days on 05.00pm onwards at university play ground',2);
/*!40000 ALTER TABLE `sports_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_info`
--

DROP TABLE IF EXISTS `staff_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff_info` (
  `name` varchar(50) DEFAULT NULL,
  `info` varchar(1000) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_info`
--

LOCK TABLES `staff_info` WRITE;
/*!40000 ALTER TABLE `staff_info` DISABLE KEYS */;
INSERT INTO `staff_info` VALUES ('des_staff1','Vice chancellor of the Demo university holds by Prof. S.Devendra, Dean of Faculty of Engineering is Dr. S.Galappaththi, Dean of Faculty of Computing Dr.S. Abeysekara and Student Counseller is Mr. S. Sumanapala. Other academic staffs and their details you can find on web pages ofeach faculties.',1);
/*!40000 ALTER TABLE `staff_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `reg_no` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('S123','Nilupl Manodya','n.manodya@gmail.com',1);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_table`
--

DROP TABLE IF EXISTS `test_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_table` (
  `column1_int` int(11) DEFAULT NULL,
  `column_2` varchar(50) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_table`
--

LOCK TABLES `test_table` WRITE;
/*!40000 ALTER TABLE `test_table` DISABLE KEYS */;
INSERT INTO `test_table` VALUES (1,'value1',1),(2,'value2',2),(3,'value3',3);
/*!40000 ALTER TABLE `test_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uni_info_des`
--

DROP TABLE IF EXISTS `uni_info_des`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `uni_info_des` (
  `des_name` varchar(50) DEFAULT NULL,
  `des` varchar(900) DEFAULT NULL,
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uni_info_des`
--

LOCK TABLES `uni_info_des` WRITE;
/*!40000 ALTER TABLE `uni_info_des` DISABLE KEYS */;
INSERT INTO `uni_info_des` VALUES ('uni_info','DEMO university is an institution of higher education and research which awards academic degrees in several academic disciplines. We typically offer both undergraduate programs in different faculties of learning. Sports facilities and high quality laborataries offer chance to students to achieve their targets easily.',1);
/*!40000 ALTER TABLE `uni_info_des` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-14 12:56:06
