CREATE DATABASE  IF NOT EXISTS `linkedin` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `linkedin`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: linkedin
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `application`
--

DROP TABLE IF EXISTS `application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `application` (
  `application_id` int NOT NULL AUTO_INCREMENT,
  `job_id` int NOT NULL,
  `user_id` int NOT NULL,
  `application_status` varchar(50) NOT NULL,
  `application_date` date NOT NULL,
  PRIMARY KEY (`application_id`),
  KEY `job_id` (`job_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `application_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `job` (`job_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `application_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `application`
--

LOCK TABLES `application` WRITE;
/*!40000 ALTER TABLE `application` DISABLE KEYS */;
INSERT INTO `application` VALUES (1,1,3,'Pending','2023-09-15'),(2,2,5,'Accepted','2023-09-10'),(3,3,4,'Rejected','2023-09-05'),(4,4,2,'Pending','2023-09-20'),(5,5,1,'Accepted','2023-09-01'),(6,1,1,'Pending','2023-09-15'),(7,1,2,'Accepted','2023-09-16'),(8,1,3,'Rejected','2023-09-17'),(9,2,1,'Accepted','2023-09-10'),(10,2,2,'Pending','2023-09-11'),(11,2,3,'Accepted','2023-09-12'),(12,2,4,'Rejected','2023-09-13'),(13,3,1,'Rejected','2023-09-05'),(14,3,2,'Pending','2023-09-06'),(15,4,1,'Pending','2023-09-20'),(16,4,2,'Accepted','2023-09-21'),(17,5,1,'Accepted','2023-09-01'),(18,5,2,'Rejected','2023-09-02'),(19,5,3,'Pending','2023-09-03'),(20,6,6,'Pending','2023-10-01'),(21,7,7,'Accepted','2023-10-02'),(22,8,8,'Rejected','2023-10-03'),(23,9,9,'Pending','2023-10-04'),(24,10,10,'Accepted','2023-10-05'),(25,11,11,'Pending','2023-10-06'),(26,12,12,'Rejected','2023-10-07'),(27,13,13,'Accepted','2023-10-08'),(28,14,14,'Pending','2023-10-09'),(29,15,15,'Accepted','2023-10-10'),(30,1,6,'Rejected','2023-10-11'),(31,2,7,'Pending','2023-10-12'),(32,3,8,'Accepted','2023-10-13'),(33,4,9,'Rejected','2023-10-14'),(34,5,10,'Pending','2023-10-15');
/*!40000 ALTER TABLE `application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `connection`
--

DROP TABLE IF EXISTS `connection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `connection` (
  `connection_id` int NOT NULL AUTO_INCREMENT,
  `userIdA` int NOT NULL,
  `userIdB` int NOT NULL,
  `connection_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`connection_id`),
  UNIQUE KEY `userIdA` (`userIdA`,`userIdB`),
  KEY `userIdB` (`userIdB`),
  CONSTRAINT `connection_ibfk_1` FOREIGN KEY (`userIdA`) REFERENCES `user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `connection_ibfk_2` FOREIGN KEY (`userIdB`) REFERENCES `user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `connection_chk_1` CHECK ((`userIdA` < `userIdB`))
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `connection`
--

LOCK TABLES `connection` WRITE;
/*!40000 ALTER TABLE `connection` DISABLE KEYS */;
INSERT INTO `connection` VALUES (76,1,2,'2023-09-30 18:30:00'),(77,1,3,'2023-10-01 18:30:00'),(78,2,4,'2023-10-02 18:30:00'),(79,2,5,'2023-10-03 18:30:00'),(80,3,6,'2023-10-04 18:30:00'),(81,3,7,'2023-10-05 18:30:00'),(82,4,8,'2023-10-06 18:30:00'),(83,4,9,'2023-10-07 18:30:00'),(84,5,10,'2023-10-08 18:30:00'),(85,5,11,'2023-10-09 18:30:00'),(86,6,12,'2023-10-10 18:30:00'),(87,6,13,'2023-10-11 18:30:00'),(88,7,14,'2023-10-12 18:30:00'),(89,7,15,'2023-10-13 18:30:00'),(90,1,8,'2023-10-14 18:30:00');
/*!40000 ALTER TABLE `connection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `education`
--

DROP TABLE IF EXISTS `education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `education` (
  `edu_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `institution_id` int NOT NULL,
  `start` date NOT NULL,
  `end` date NOT NULL,
  `course` varchar(50) NOT NULL,
  `duration` int GENERATED ALWAYS AS ((to_days(`end`) - to_days(`start`))) VIRTUAL,
  PRIMARY KEY (`edu_id`),
  KEY `user_id` (`user_id`),
  KEY `institution_id` (`institution_id`),
  CONSTRAINT `education_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `education_ibfk_2` FOREIGN KEY (`institution_id`) REFERENCES `institution` (`institution_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `education`
--

LOCK TABLES `education` WRITE;
/*!40000 ALTER TABLE `education` DISABLE KEYS */;
INSERT INTO `education` (`edu_id`, `user_id`, `institution_id`, `start`, `end`, `course`) VALUES (1,1,5,'2010-09-01','2014-06-30','Computer Science'),(2,2,1,'2008-09-01','2012-06-30','Business Administration'),(3,3,4,'2013-09-01','2017-06-30','Biomedical Engineering'),(4,4,3,'2011-09-01','2015-06-30','Environmental Science'),(5,5,2,'2012-09-01','2016-06-30','Economics'),(43,6,16,'2015-09-01','2019-06-30','Computer Science'),(44,7,17,'2014-09-01','2018-06-30','Electrical Engineering'),(45,8,18,'2016-09-01','2020-06-30','Mechanical Engineering'),(46,9,19,'2013-09-01','2017-06-30','Physics'),(47,10,20,'2017-09-01','2021-06-30','Chemistry'),(48,11,21,'2012-09-01','2016-06-30','Mathematics'),(49,12,22,'2015-09-01','2019-06-30','Biology'),(50,13,23,'2014-09-01','2018-06-30','Economics'),(51,14,24,'2016-09-01','2020-06-30','Psychology'),(52,15,25,'2013-09-01','2017-06-30','Political Science'),(53,11,16,'2018-09-01','2022-06-30','Data Science'),(54,9,17,'2017-09-01','2021-06-30','Artificial Intelligence'),(55,15,18,'2019-09-01','2023-06-30','Robotics'),(56,12,19,'2016-09-01','2020-06-30','Biochemistry'),(57,14,20,'2015-09-01','2019-06-30','International Relations');
/*!40000 ALTER TABLE `education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experience`
--

DROP TABLE IF EXISTS `experience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experience` (
  `exp_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `institution_id` int DEFAULT NULL,
  `start` date NOT NULL,
  `end` date NOT NULL,
  `description` varchar(255) NOT NULL,
  `title` varchar(50) NOT NULL,
  `duration` int GENERATED ALWAYS AS ((to_days(`end`) - to_days(`start`))) VIRTUAL,
  PRIMARY KEY (`exp_id`),
  KEY `user_id` (`user_id`),
  KEY `institution_id` (`institution_id`),
  KEY `idx_experience_dates` (`start`,`end`),
  KEY `idx_experience_title` (`title`),
  CONSTRAINT `experience_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `experience_ibfk_2` FOREIGN KEY (`institution_id`) REFERENCES `institution` (`institution_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experience`
--

LOCK TABLES `experience` WRITE;
/*!40000 ALTER TABLE `experience` DISABLE KEYS */;
INSERT INTO `experience` (`exp_id`, `user_id`, `institution_id`, `start`, `end`, `description`, `title`) VALUES (1,1,1,'2014-07-01','2018-12-31','Developed web applications','Software Engineer'),(2,1,7,'2019-01-01','2023-10-07','Led financial software projects','Senior Developer'),(3,2,3,'2012-07-01','2017-06-30','Managed renewable energy projects','Project Manager'),(4,3,9,'2017-07-01','2023-10-07','Researched new medical devices','Biomedical Researcher'),(5,4,5,'2015-07-01','2020-12-31','Created online courses','Instructional Designer'),(6,5,7,'2016-07-01','2023-10-07','Analyzed market trends','Data Analyst'),(7,6,8,'2018-03-15','2023-10-07','Optimized renewable energy systems','Energy Systems Engineer'),(8,7,10,'2017-09-01','2023-10-07','Developed AI algorithms for research projects','AI Research Engineer'),(9,8,12,'2016-06-01','2023-10-07','Implemented cybersecurity measures for clients','Cybersecurity Specialist'),(10,9,13,'2019-02-01','2023-10-07','Developed quantum computing algorithms','Quantum Computing Researcher'),(11,10,14,'2018-08-15','2023-10-07','Designed sustainable energy solutions','Sustainability Engineer'),(12,11,15,'2017-11-01','2023-10-07','Programmed advanced robotics systems','Robotics Software Engineer'),(13,12,11,'2016-04-01','2023-10-07','Conducted biotech research and development','Biotech Researcher'),(14,13,6,'2018-01-15','2023-10-07','Managed cloud infrastructure projects','Cloud Solutions Architect'),(15,14,2,'2017-07-01','2023-10-07','Analyzed financial data for global markets','Financial Data Analyst'),(16,15,9,'2019-05-01','2023-10-07','Developed innovative healthcare technologies','Healthcare Technology Engineer');
/*!40000 ALTER TABLE `experience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institution`
--

DROP TABLE IF EXISTS `institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `institution` (
  `institution_id` int NOT NULL AUTO_INCREMENT,
  `no_of_employees` int NOT NULL,
  `website` varchar(255) NOT NULL,
  `industry` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `location_city` varchar(50) NOT NULL,
  `location_state` varchar(50) NOT NULL,
  `location_country` varchar(50) NOT NULL,
  PRIMARY KEY (`institution_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institution`
--

LOCK TABLES `institution` WRITE;
/*!40000 ALTER TABLE `institution` DISABLE KEYS */;
INSERT INTO `institution` VALUES (1,10000,'www.techcorp.com','Technology','TechCorp','Leading technology company','San Jose','CA','USA'),(2,5000,'www.financegroup.com','Finance','Finance Group','Global financial services','New York','NY','USA'),(3,2000,'www.greenenergyco.com','Energy','Green Energy Co','Renewable energy solutions','Berlin','Berlin','Germany'),(4,8000,'www.globalhealth.org','Healthcare','Global Health','International healthcare provider','London','England','UK'),(5,3000,'www.edulearn.com','Education','EduLearn','Online learning platform','Melbourne','VIC','Australia'),(6,5000,'www.techcorp.com','Technology','TechCorp','Leading technology company','San Francisco','CA','USA'),(7,10000,'www.globalfinance.com','Finance','Global Finance','International financial services','New York','NY','USA'),(8,3000,'www.greenenergy.com','Energy','Green Energy Co','Renewable energy solutions','Austin','TX','USA'),(9,7000,'www.healthtech.com','Healthcare','HealthTech','Innovative healthcare technology','Boston','MA','USA'),(10,2000,'www.airesearch.com','Technology','AI Research Labs','Cutting-edge AI research','Seattle','WA','USA'),(11,6000,'www.biotech-innovations.com','Biotechnology','BioTech Innovations','Pioneering biotech research and development','Cambridge','MA','USA'),(12,4500,'www.cybersecure-solutions.com','Cybersecurity','CyberSecure Solutions','Advanced cybersecurity services and products','Tel Aviv','Tel Aviv','Israel'),(13,7500,'www.quantum-computing.co.uk','Technology','Quantum Computing Ltd','Cutting-edge quantum computing research','Oxford','Oxfordshire','UK'),(14,3500,'www.sustainable-energy.de','Energy','Sustainable Energy GmbH','Innovative sustainable energy solutions','Munich','Bavaria','Germany'),(15,5500,'www.ai-robotics.jp','Robotics','AI Robotics Corp','Advanced AI-powered robotics systems','Tokyo','Tokyo','Japan'),(16,15000,'www.harvard.edu','Education','Harvard University','Prestigious Ivy League research university','Cambridge','MA','USA'),(17,12000,'www.stanford.edu','Education','Stanford University','Leading private research university','Stanford','CA','USA'),(18,18000,'www.mit.edu','Education','Massachusetts Institute of Technology','World-renowned institute for technology and science','Cambridge','MA','USA'),(19,20000,'www.ox.ac.uk','Education','University of Oxford','Oldest university in the English-speaking world','Oxford','Oxfordshire','UK'),(20,17000,'www.cam.ac.uk','Education','University of Cambridge','World-leading research institution','Cambridge','Cambridgeshire','UK'),(21,14000,'www.berkeley.edu','Education','University of California, Berkeley','Top-ranked public university','Berkeley','CA','USA'),(22,16000,'www.ethz.ch','Education','ETH Zurich','Leading science and technology university in Europe','Zurich','Zurich','Switzerland'),(23,13000,'www.utokyo.ac.jp','Education','University of Tokyo','Japan\'s top university','Tokyo','Tokyo','Japan'),(24,19000,'www.tsinghua.edu.cn','Education','Tsinghua University','Leading university in China','Beijing','Beijing','China'),(25,11000,'www.nus.edu.sg','Education','National University of Singapore','Top-ranked university in Asia','Singapore','Singapore','Singapore');
/*!40000 ALTER TABLE `institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `job_id` int NOT NULL AUTO_INCREMENT,
  `institution_id` int DEFAULT NULL,
  `job_title` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`job_id`),
  KEY `institution_id` (`institution_id`),
  CONSTRAINT `job_ibfk_1` FOREIGN KEY (`institution_id`) REFERENCES `institution` (`institution_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES (1,1,'Full Stack Developer','Develop web applications using modern technologies. Required skills: JavaScript, Python, SQL, Project Management','Full-time'),(2,2,'Financial Analyst','Analyze financial data and create reports. We\'re looking for candidates with skills in: Java, C++, Data Analysis, Machine Learning','Full-time'),(3,3,'Renewable Energy Engineer','Design and implement green energy solutions. Ideal candidates will have experience in: Python, SQL, Digital Marketing, Data Analysis','Contract'),(4,4,'Clinical Research Coordinator','Coordinate medical research studies. Key skills for this role: JavaScript, Graphic Design, Project Management, Digital Marketing','Part-time'),(5,5,'Online Course Creator','Develop engaging online learning content. Required skills include: Python, Machine Learning, Data Analysis, SQL','Freelance'),(6,6,'Cloud Solutions Architect','Design and implement cloud-based solutions. Required skills: Cloud Computing, DevOps, JavaScript, Python','Full-time'),(7,7,'Blockchain Developer','Develop blockchain applications for financial services. Key skills: Blockchain, JavaScript, Java, Cybersecurity','Full-time'),(8,8,'AI Research Scientist','Conduct cutting-edge research in artificial intelligence. Skills needed: Artificial Intelligence, Machine Learning, Python, Data Analysis','Full-time'),(9,9,'Healthcare Data Analyst','Analyze healthcare data to improve patient outcomes. Required skills: Data Analysis, SQL, Python, Machine Learning','Full-time'),(10,10,'Quantum Computing Researcher','Research quantum computing algorithms and applications. Skills: Artificial Intelligence, Machine Learning, Python, C++','Full-time'),(11,11,'Bioinformatics Specialist','Analyze biological data using computational methods. Required skills: Python, Data Analysis, Machine Learning, SQL','Full-time'),(12,12,'Cybersecurity Consultant','Provide expert advice on cybersecurity measures. Key skills: Cybersecurity, Cloud Computing, DevOps, Blockchain','Contract'),(13,13,'Quantum Software Engineer','Develop software for quantum computing applications. Skills needed: Python, C++, Artificial Intelligence, Cloud Computing','Full-time'),(14,14,'Renewable Energy Data Scientist','Analyze data to optimize renewable energy solutions. Required skills: Data Analysis, Machine Learning, Python, SQL','Full-time'),(15,15,'Robotics Software Engineer','Develop software for advanced robotics systems. Key skills: Artificial Intelligence, Python, C++, DevOps','Full-time');
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `job_application_stats`
--

DROP TABLE IF EXISTS `job_application_stats`;
/*!50001 DROP VIEW IF EXISTS `job_application_stats`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `job_application_stats` AS SELECT 
 1 AS `job_id`,
 1 AS `job_title`,
 1 AS `institution_name`,
 1 AS `total_applications`,
 1 AS `accepted_applications`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `phone_no`
--

DROP TABLE IF EXISTS `phone_no`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phone_no` (
  `phone_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  PRIMARY KEY (`phone_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `phone_no_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone_no`
--

LOCK TABLES `phone_no` WRITE;
/*!40000 ALTER TABLE `phone_no` DISABLE KEYS */;
INSERT INTO `phone_no` VALUES (1,1,'+1-212-555-1234'),(2,2,'+1-415-555-2345'),(3,3,'+44-20-5555-3456'),(4,4,'+61-2-5555-4567'),(5,5,'+1-416-555-5678'),(6,6,'+65-5555-6789'),(7,7,'+33-1-5555-7890'),(8,8,'+20-2-5555-8901'),(9,9,'+34-91-5555-9012'),(10,10,'+81-3-5555-0123'),(11,11,'+86-21-5555-1234'),(12,12,'+91-22-5555-2345'),(13,13,'+82-2-5555-3456'),(14,14,'+62-21-5555-4567'),(15,15,'+84-28-5555-5678');
/*!40000 ALTER TABLE `phone_no` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `post_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `post_content` text NOT NULL,
  `post_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `likes` int DEFAULT '0',
  `last_liked_at` datetime DEFAULT NULL,
  PRIMARY KEY (`post_id`,`user_id`),
  KEY `fk_user` (`user_id`),
  CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,1,'Excited to start my new job at Finance Group!','2023-01-02 09:30:00',0,NULL),(2,2,'Just completed a major project on renewable energy. Feeling accomplished!','2023-03-15 14:45:00',0,NULL),(3,3,'Looking for collaborators on a new medical research project. Any takers?','2023-05-20 11:20:00',0,NULL),(4,4,'Sharing my latest blog post on environmental conservation. Check it out!','2023-07-07 16:00:00',0,NULL),(5,5,'Attended an amazing data science conference today. So much to learn!','2023-09-30 20:15:00',0,NULL),(6,6,'Just launched a new cloud-based solution. Excited to see how it performs!','2023-10-05 10:30:00',0,NULL),(7,7,'Exploring the potential of blockchain in finance. Any thoughts?','2023-10-06 14:15:00',0,NULL),(8,8,'Made a breakthrough in our AI research today. The future is here!','2023-10-07 16:45:00',0,NULL),(9,9,'Analyzing healthcare data to improve patient outcomes. Data saves lives!','2023-10-08 09:00:00',0,NULL),(10,10,'Quantum computing is mind-blowing. Just solved a complex problem in minutes!','2023-10-09 11:30:00',0,NULL),(11,11,'New bioinformatics tool released. Feedback welcome!','2023-10-10 13:20:00',0,NULL),(12,12,'Cybersecurity tip of the day: Always use two-factor authentication!','2023-10-11 15:45:00',0,NULL),(13,13,'Quantum algorithms are revolutionizing cryptography. Exciting times ahead!','2023-10-12 17:10:00',0,NULL),(14,14,'Sustainable energy solutions are the key to our future. Let\'s innovate!','2023-10-13 08:30:00',0,NULL),(15,15,'Just programmed a robot to do backflips. What should I teach it next?','2023-10-14 12:00:00',0,NULL);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill`
--

DROP TABLE IF EXISTS `skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill` (
  `skill_id` int NOT NULL AUTO_INCREMENT,
  `skill_name` varchar(50) NOT NULL,
  PRIMARY KEY (`skill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill`
--

LOCK TABLES `skill` WRITE;
/*!40000 ALTER TABLE `skill` DISABLE KEYS */;
INSERT INTO `skill` VALUES (1,'JavaScript'),(2,'Python'),(3,'SQL'),(4,'Java'),(5,'C++'),(6,'Project Management'),(7,'Data Analysis'),(8,'Machine Learning'),(9,'Digital Marketing'),(10,'Graphic Design'),(11,'Cloud Computing'),(12,'Cybersecurity'),(13,'DevOps'),(14,'Artificial Intelligence'),(15,'Blockchain');
/*!40000 ALTER TABLE `skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `age` int DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `location_city` varchar(50) NOT NULL,
  `location_state` varchar(50) NOT NULL,
  `location_country` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `idx_user_location` (`location_city`,`location_state`,`location_country`),
  KEY `idx_user_dob` (`dob`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'John Doe','1990-05-15',34,'john.jpg','New York','NY','USA'),(2,'Jane Smith','1988-09-22',36,'jane.jpg','San Francisco','CA','USA'),(3,'Alice Johnson','1995-03-10',29,'alice.jpg','London','England','UK'),(4,'Bob Brown','1992-11-30',31,'bob.jpg','Sydney','NSW','Australia'),(5,'Emma Wilson','1993-07-18',31,'emma.jpg','Toronto','ON','Canada'),(6,'Michael Chen','1991-02-25',33,'michael.jpg','Singapore','Singapore','Singapore'),(7,'Sophie Martin','1994-12-05',29,'sophie.jpg','Paris','Île-de-France','France'),(8,'Ahmed Hassan','1989-08-14',35,'ahmed.jpg','Cairo','Cairo Governorate','Egypt'),(9,'Maria Garcia','1996-06-20',28,'maria.jpg','Madrid','Community of Madrid','Spain'),(10,'Yuki Tanaka','1993-01-07',31,'yuki.jpg','Tokyo','Tokyo','Japan'),(11,'Li Wei','1995-08-12',29,'liwei.jpg','Shanghai','Shanghai','China'),(12,'Priya Patel','1993-06-30',31,'priya.jpg','Mumbai','Maharashtra','India'),(13,'Kim Min-jun','1992-01-15',32,'minjun.jpg','Seoul','Seoul','South Korea'),(14,'Nurul Huda','1994-03-25',30,'nurul.jpg','Jakarta','Jakarta','Indonesia'),(15,'Thanh Nguyen','1991-12-07',32,'thanh.jpg','Ho Chi Minh City','Ho Chi Minh','Vietnam');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `user_education_experience_summary`
--

DROP TABLE IF EXISTS `user_education_experience_summary`;
/*!50001 DROP VIEW IF EXISTS `user_education_experience_summary`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `user_education_experience_summary` AS SELECT 
 1 AS `user_id`,
 1 AS `name`,
 1 AS `education_count`,
 1 AS `experience_count`,
 1 AS `latest_education`,
 1 AS `latest_experience`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `user_profile_view`
--

DROP TABLE IF EXISTS `user_profile_view`;
/*!50001 DROP VIEW IF EXISTS `user_profile_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `user_profile_view` AS SELECT 
 1 AS `user_id`,
 1 AS `name`,
 1 AS `location_city`,
 1 AS `location_state`,
 1 AS `location_country`,
 1 AS `skills`,
 1 AS `connection_count`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `user_skill`
--

DROP TABLE IF EXISTS `user_skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_skill` (
  `skill_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`skill_id`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_skill_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `user_skill_ibfk_2` FOREIGN KEY (`skill_id`) REFERENCES `skill` (`skill_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_skill`
--

LOCK TABLES `user_skill` WRITE;
/*!40000 ALTER TABLE `user_skill` DISABLE KEYS */;
INSERT INTO `user_skill` VALUES (1,1),(3,1),(6,1),(2,2),(3,2),(5,2),(7,2),(4,3),(5,3),(8,3),(1,4),(9,4),(10,4),(2,5),(7,5),(8,5),(5,7),(5,8),(4,10),(6,10),(15,10),(1,11),(7,11),(10,11),(2,12),(8,12),(3,13),(9,13),(12,13),(4,14),(13,14),(11,15),(14,15);
/*!40000 ALTER TABLE `user_skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `user_with_age`
--

DROP TABLE IF EXISTS `user_with_age`;
/*!50001 DROP VIEW IF EXISTS `user_with_age`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `user_with_age` AS SELECT 
 1 AS `user_id`,
 1 AS `name`,
 1 AS `dob`,
 1 AS `age`,
 1 AS `profile_pic`,
 1 AS `location_city`,
 1 AS `location_state`,
 1 AS `location_country`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `job_application_stats`
--

/*!50001 DROP VIEW IF EXISTS `job_application_stats`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `job_application_stats` AS select `j`.`job_id` AS `job_id`,`j`.`job_title` AS `job_title`,`i`.`name` AS `institution_name`,count(`a`.`application_id`) AS `total_applications`,sum((case when (`a`.`application_status` = 'Accepted') then 1 else 0 end)) AS `accepted_applications` from ((`job` `j` join `institution` `i` on((`j`.`institution_id` = `i`.`institution_id`))) left join `application` `a` on((`j`.`job_id` = `a`.`job_id`))) group by `j`.`job_id`,`j`.`job_title`,`i`.`name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `user_education_experience_summary`
--

/*!50001 DROP VIEW IF EXISTS `user_education_experience_summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `user_education_experience_summary` AS select `u`.`user_id` AS `user_id`,`u`.`name` AS `name`,count(distinct `ed`.`edu_id`) AS `education_count`,count(distinct `ex`.`exp_id`) AS `experience_count`,max(`ed`.`end`) AS `latest_education`,max(`ex`.`end`) AS `latest_experience` from ((`user` `u` left join `education` `ed` on((`u`.`user_id` = `ed`.`user_id`))) left join `experience` `ex` on((`u`.`user_id` = `ex`.`user_id`))) group by `u`.`user_id`,`u`.`name` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `user_profile_view`
--

/*!50001 DROP VIEW IF EXISTS `user_profile_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `user_profile_view` AS select `u`.`user_id` AS `user_id`,`u`.`name` AS `name`,`u`.`location_city` AS `location_city`,`u`.`location_state` AS `location_state`,`u`.`location_country` AS `location_country`,group_concat(distinct `s`.`skill_name` order by `s`.`skill_name` ASC separator ',') AS `skills`,count(distinct `c`.`connection_id`) AS `connection_count` from (((`user` `u` left join `user_skill` `us` on((`u`.`user_id` = `us`.`user_id`))) left join `skill` `s` on((`us`.`skill_id` = `s`.`skill_id`))) left join `connection` `c` on(((`u`.`user_id` = `c`.`userIdA`) or (`u`.`user_id` = `c`.`userIdB`)))) group by `u`.`user_id`,`u`.`name`,`u`.`location_city`,`u`.`location_state`,`u`.`location_country` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `user_with_age`
--

/*!50001 DROP VIEW IF EXISTS `user_with_age`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `user_with_age` AS select `user`.`user_id` AS `user_id`,`user`.`name` AS `name`,`user`.`dob` AS `dob`,timestampdiff(YEAR,`user`.`dob`,curdate()) AS `age`,`user`.`profile_pic` AS `profile_pic`,`user`.`location_city` AS `location_city`,`user`.`location_state` AS `location_state`,`user`.`location_country` AS `location_country` from `user` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-12  4:28:44
