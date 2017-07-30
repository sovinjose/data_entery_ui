-- MySQL dump 10.13  Distrib 5.6.25, for osx10.10 (x86_64)
--
-- Host: 104.199.102.4    Database: wtj
-- ------------------------------------------------------
-- Server version	5.7.14-google-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED='3894cade-c300-11e6-8315-42010a840fcf:1-14550462';

--
-- Current Database: `wtj`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `wtj` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `wtj`;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer` varchar(400) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `answer_question_id_62e3ce9b_fk_question_id` (`question_id`),
  CONSTRAINT `answer_question_id_62e3ce9b_fk_question_id` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (17,'',12),(18,'',13),(19,'Likely',14),(20,'Highly Likely',14),(21,'Very Unlikely',14),(22,'Unlikely',14),(23,'Neutral',14),(24,'Yes',15),(25,'No',15),(26,'Salary',16),(27,'To build experience',16),(28,'Employer\'s brand',16),(29,'',17),(30,'',18),(31,'',19),(32,'',20),(33,'A-level',21),(34,'GCSE',21),(35,'Non-honours Bachelor\'s Degree',21),(36,'Higher National Diploma',21),(37,'Higher National Certificate',21),(38,'Doctoral Degree',21),(39,'Master\'s Degree',21),(40,'Bachelor\'s Degree with Honours',21),(41,'3',22),(42,'More than 3',22),(43,'0',22),(44,'1',22),(45,'2',22),(46,'3',23),(47,'More than 3',23),(48,'0',23),(49,'1',23),(50,'2',23),(51,'<DATABASE>',24),(52,'<DATABASE>',25),(53,'3rd or D: Passed (40% - 49%)',26),(54,'2:1  or B: Very good (60% - 70%)',26),(55,'2:2 or C: Improvement Needed (50% - 60%)',26),(56,'1st  or A: Excellent (70% - 100%)',26),(57,'No',27),(58,'Yes',27),(59,'No',28),(60,'Yes',28),(61,'<DATABASE>',29),(62,'<DATABASE>',30),(63,'3rd or D: Passed (40% - 49%)',31),(64,'2:1  or B: Very good (60% - 70%)',31),(65,'2:2 or C: Improvement Needed (50% - 60%)',31),(66,'1st  or A: Excellent (70% - 100%)',31),(67,'No',32),(68,'Yes',32),(69,'No',33),(70,'Yes',33),(71,'3rd or D: Passed (40% - 49%)',34),(72,'2:1  or B: Very good (60% - 70%)',34),(73,'2:2 or C: Improvement Needed (50% - 60%)',34),(74,'1st  or A: Excellent (70% - 100%)',34),(75,'No',35),(76,'Yes',35),(77,'No',36),(78,'Depends on the offer',36),(79,'Yes',36),(80,'No',37),(81,'Yes',37),(82,'No',38),(83,'Yes',38),(84,'No',39),(85,'Yes',39),(86,'Refer List',40),(87,'No',41),(88,'Yes',41),(89,'Phone',42),(90,'Email',42),(91,'Refer List',43),(92,'No',44),(93,'Prefer not to say',44),(94,'Yes',44),(95,'Refer List',45),(96,'Refer List',46),(97,'No',47),(98,'Prefer not to say',47),(99,'Yes',47),(100,'No',48),(101,'Prefer not to say',48),(102,'Yes',48),(103,'Refer List',49),(104,'No',50),(105,'Prefer not to say',50),(106,'Yes',50),(107,'Secondary Carer',51),(108,' Primary Carer',51);
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (12,'Congratulations! Let\'s quickly set you up.','TC','system','2017-05-21 16:51:37.690907'),(13,'We have setup cards (like this one), to push your job applications to the top of employers.','TC','system','2017-05-21 16:52:59.063933'),(14,'\"We have put together very simple questions, to know more about you. Like this one…\r\n\r\nWould you consider exploring job roles distinctly different from your course of studies?\"','LSK','system','2017-05-21 16:56:55.017834'),(15,'\"And questions about your education and experience.\r\n\r\nAre you currently enrolled in university?\"','TXTMCQ2','system','2017-05-21 16:59:33.245907'),(16,'\"Or this one...\r\n\r\nWhat motivates you to have a graduate career? Arrange the tiles in order of your preference and press \'✓\'.\"','TXTARR3','system','2017-05-21 17:01:11.419873'),(17,'If you enter a wrong answer, all you have to do is to tap \'Back\', and correct it.','TC','system','2017-05-21 17:01:54.434242'),(18,'We will never ask any question that is not related to your application.  And we will only ask once!','TC','system','2017-05-21 17:02:36.476097'),(19,'We will show you the best route, based on available jobs and all other candidates - real-time-, to give you your edge.','TC','system','2017-05-21 17:02:55.426581'),(20,'\"To remove bias completely, we guarantee to never share your personal information with anyone, until you\'re shortlisted for a role that you have applied.\r\n\r\nWatch our video on how we do it! :) \"','TC','system','2017-05-21 17:03:52.342376'),(21,'\"We would like to know more about what attracts you to the career you chose.\r\n\r\nWhat is your highest level of educational qualification? Choose from the list to proceed.\"','LONGLIST','system','2017-05-21 17:13:21.489892'),(22,'How many years\' work experience do you have in total, (across any industry)?','TXTMCQ5','system','2017-05-21 17:17:38.442973'),(23,'How many years experience do you have in the <<<<Chosen>>>> industry?','TXTMCQ5','system','2017-05-21 17:18:59.485878'),(24,'From which University did you get your Master\'s Degree?','LONGLIST','system','2017-05-21 18:21:53.040666'),(25,'What was your field of study during your Master\'s program?','LONGLIST','system','2017-05-21 18:22:26.475399'),(26,'Which grade did you attain for this degree?','TXTMCQ4','system','2017-05-21 18:25:22.799321'),(27,'Do you have another Master\'s degree in addition to the one you just mentioned?','TXTMCQ2','system','2017-05-21 18:28:23.689671'),(28,'Do you currently hold an Undergraduate degree?','TXTMCQ2','system','2017-05-21 18:29:01.527420'),(29,'From which University did you get your Undergraduate Degree?','LONGLIST','system','2017-05-21 18:30:12.487809'),(30,'What was your field of study during your Undergraduate program?','LONGLIST','system','2017-05-21 18:30:48.072622'),(31,'Which grade did you attain for this degree?','TXTMCQ4','system','2017-05-21 18:32:36.108623'),(32,'Do you have another Undergraduate degree in addition to the one you just mentioned?','TXTMCQ2','system','2017-05-21 18:33:40.361652'),(33,'Do you hold a HND/HNC?','TXTMCQ2','system','2017-05-21 18:34:25.163307'),(34,'Which grade did you attain for HND/HNC?','TXTMCQ4','system','2017-05-21 18:36:04.022249'),(35,'Do you hold any  professional qualifications?','TXTMCQ2','system','2017-05-21 18:36:42.580431'),(36,'Would you be okay to relocate or travel from your current city?','TXTMCQ3','system','2017-05-21 18:38:10.708215'),(37,'Do you have the right to work in <<<<<Employer country>>>>>?','TXTMCQ2','system','2017-05-21 18:39:06.891422'),(38,'Are you a EU/EEA/Swiss nationality?','TXTMCQ2','system','2017-05-21 18:39:46.812306'),(39,'Would you need a sponsor to work in <<<<<Employer Country>>>>>?','TXTMCQ2','system','2017-05-21 18:40:23.509188'),(40,'What Visa do you currently hold?','LONGLIST','system','2017-05-21 18:41:03.398204'),(41,'Would you like your employers to connect to you in Social Media (LinkedIn), and add your personal websites?','TXTMCQ2','system','2017-05-21 18:41:46.962659'),(42,'How would you prefer to be contacted primarily?','TXTMCQ2','system','2017-05-21 18:44:24.293773'),(43,'What gender do you identify as?','LONGLIST','system','2017-05-21 18:51:06.152407'),(44,'Are you married or in a civil partnership?','TXTMCQ3','system','2017-05-21 18:52:30.234629'),(45,'What is your sexual orientation?','LONGLIST','system','2017-05-21 18:53:25.618371'),(46,'What is your ethnicity?','LONGLIST','system','2017-05-21 18:54:07.946126'),(47,'Do you consider yourself to have a disability or health condition?','TXTMCQ3','system','2017-05-21 18:55:07.475183'),(48,'\"Do you require special changes made in the selection process because you possess a disability, or health condition? \r\n\r\n*This may vary across various job applications.\"','TXTMCQ2','system','2017-05-21 18:55:47.981463'),(49,'What is your religion or belief?','LONGLIST','system','2017-05-21 18:57:09.440621'),(50,'Do you have caring responsibilities?','TXTMCQ2','system','2017-05-21 18:58:07.591636'),(51,'Please select which your current situation.','TXTMCQ2','system','2017-05-21 18:59:30.203711');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'add_data','0001_initial','2017-05-20 11:49:17.471233'),(2,'add_data','0002_answer','2017-05-20 12:58:03.187630');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_wtj`
--

DROP TABLE IF EXISTS `test_wtj`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_wtj` (
  `uid` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `passowrd` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_wtj`
--

LOCK TABLES `test_wtj` WRITE;
/*!40000 ALTER TABLE `test_wtj` DISABLE KEYS */;
INSERT INTO `test_wtj` VALUES ('123asd123123','jibinjosepez@gmail.com','123@2asd'),('123asd123123','jibinjosepez@gmail.com','123@2asd'),('123asd123123','jibinjosepez@gmail.com','123@2asd');
/*!40000 ALTER TABLE `test_wtj` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-03 14:17:39
