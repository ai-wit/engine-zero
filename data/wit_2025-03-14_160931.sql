-- MySQL dump 10.13  Distrib 9.2.0, for macos14.7 (arm64)
--
-- Host: 127.0.0.1    Database: wit
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AI_Result`
--

DROP TABLE IF EXISTS `AI_Result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AI_Result` (
  `id` int NOT NULL AUTO_INCREMENT,
  `notice_id` int DEFAULT NULL,
  `subject` varchar(255) NOT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `entity` varchar(255) DEFAULT NULL,
  `fund` varchar(255) DEFAULT NULL,
  `support_amount` varchar(255) DEFAULT NULL,
  `target` varchar(255) DEFAULT NULL,
  `loan_limit` varchar(255) DEFAULT NULL,
  `conditions` varchar(255) DEFAULT NULL,
  `application_period` varchar(255) DEFAULT NULL,
  `support_region` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AI_Result`
--

/*!40000 ALTER TABLE `AI_Result` DISABLE KEYS */;
INSERT INTO `AI_Result` VALUES (1,2,'2025년 관광진흥개발기금 관광사업체 운영자금 특별융자 지원 지침(변경)','2025년 관광진흥개발기금에 따라 관광사업체 운영자금을 특별융자 지원하는 지침이 변경되어 공고되었으며, 융자 규모는 500억원 내외로, 대·중견기업과 제주특별자치도 소재 사업체는 제외된다. 신청 기간은 2024년 12월 30일부터 2025년 2월 28일까지이며, 융자 금액은 선정 후 개별 통보된다.','문화체육관광부','관광진흥개발기금','500억원 내외','대·중견기업, 제주특별자치도 소재 사업체 제외','','융자금 신청처: 산업은행 등 14개 은행. 융자금 대출실행은 2025. 4. 24.(목)까지 완료해야 함.','2024. 12. 30.(월) ~ 2025. 2. 28.(금)','','2025-02-13 08:25:04','2025-02-13 08:25:04'),(2,3,'1인 자영업자 사회보험망 (고용·산재보험료) 지원사업 공고','2025년도 1인 자영업자를 위한 고용보험료 및 산재보험료 지원사업이 경남신용보증재단에 의해 공고되었으며, 지원대상은 도내 1인 자영업자로, 고용보험료는 납부한 월 보험료의 20%와 산재보험료는 등급에 따라 30~50%를 지원합니다. 신청은 2025년 2월 12일부터 12월 31일까지 가능합니다.','경남신용보증재단','고용보험료 및 산재보험료 지원','고용보험료: 납부한 월 고용보험료의 20% 지원, 산재보험료: 등급별 30~50% 지원','고용보험 및 산재보험에 가입하고, 보험료를 납부한 실적이 있는 도내 1인 자영업자','','지원 기간 중 보험 자격상실 및 미납 보험료가 없는 경우, 경상남도 사회보험망 지원사업에 지원종료 이력이 없는 경우','2025. 2. 12. ~ 12. 31.','경상남도','2025-02-13 08:25:13','2025-02-13 08:25:13'),(3,4,'2025 정책자금 상환연장 대상 확대 안내','소상공인시장진흥공단은 정책자금 상환연장 제도를 통해 소상공인들의 원리금 상환 부담을 경감하고 있으며, 2025년 3월 6일부터 변경된 내용을 안내합니다. 지원대상은 공단 직접대출 이용 중 원리금을 한번 이상 납부한 소상공인 및 경영애로를 겪고 있는 업체입니다. 신청은 매월 1일부터 10일까지 가능하며, 상환기간 연장과 적용금리 조정 등의 조건이 있습니다.','소상공인시장진흥공단','정책자금','','공단 직접대출 이용 중 원리금을 한번 이상 납부한 소상공인, 경영애로로 인정된 업체','','신청 시점 기준 공단대출 30일 초과 연체, 신용정보 등재, 세금체납 사실이 없고 휴·폐업 상태가 아닐 것','매월 1일부터 10일까지','','2025-03-07 02:17:14','2025-03-07 02:17:14');
/*!40000 ALTER TABLE `AI_Result` ENABLE KEYS */;

--
-- Table structure for table `Notice`
--

DROP TABLE IF EXISTS `Notice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Notice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) NOT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `department` varchar(255) DEFAULT NULL,
  `agency` varchar(255) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Notice`
--

/*!40000 ALTER TABLE `Notice` DISABLE KEYS */;
INSERT INTO `Notice` VALUES (1,'2025년 관광진흥개발기금 관광사업체 운영자금 특별융자 지원 지침 변경 공고','','문화체육관광부','한국관광협회중앙회','25년 관광기금 관광사업체 운영자금 특별융자 지원 지침(변경).pdf','2025-02-13 17:24:00','2025-02-13 17:24:00','2025-02-13 08:24:00','2025-02-13 08:24:00'),(2,'2025년 관광진흥개발기금 관광사업체 운영자금 특별융자 지원 지침 변경 공고','','문화체육관광부','한국관광협회중앙회','25년 관광기금 관광사업체 운영자금 특별융자 지원 지침(변경).pdf','2025-02-13 17:24:59','2025-02-13 17:24:59','2025-02-13 08:24:59','2025-02-13 08:24:59'),(3,'[경남] 2025년 1인 자영업자 사회보험망(고용ㆍ산재보험료) 지원사업 공고','','경상남도','경남신용보증재단','2025년+경남+1인+자영업자+고용·산재보험+지원사업+공고최종.pdf','2025-02-13 17:25:05','2025-02-13 17:25:05','2025-02-13 08:25:05','2025-02-13 08:25:05'),(4,'2025년 정책자금 상환연장 대상 확대 공고','','중소벤처기업부','소상공인시장진흥공단','「정책자금+상환연장」대상+확대+안내.pdf','2025-03-07 11:17:09','2025-03-07 11:17:09','2025-03-07 02:17:09','2025-03-07 02:17:09');
/*!40000 ALTER TABLE `Notice` ENABLE KEYS */;

--
-- Dumping routines for database 'wit'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-14 16:09:37
