/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : auction_spider_ali

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-11-18 21:22:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auctions
-- ----------------------------
DROP TABLE IF EXISTS `auctions`;
CREATE TABLE `auctions` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `AuctionId` varchar(14) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `CourtId` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Title` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `CategoryId` int DEFAULT NULL,
  `Url` varchar(80) NOT NULL,
  `StartPrice` decimal(18,2) NOT NULL,
  `CurrentPrice` decimal(18,2) NOT NULL,
  `CashDeposit` decimal(18,2) DEFAULT NULL,
  `PaymentAdvance` varchar(80) DEFAULT NULL,
  `AssessPrice` decimal(18,2) DEFAULT NULL,
  `Increment` decimal(18,2) DEFAULT NULL,
  `AuctionTimes` varchar(10) DEFAULT NULL,
  `AuctionType` varchar(20) DEFAULT NULL,
  `DelayCycle` varchar(80) DEFAULT NULL,
  `CorporateAgent` varchar(30) DEFAULT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  `SellingPeriod` varchar(30) DEFAULT NULL,
  `OnlineCycle` varchar(10) DEFAULT NULL,
  `BiddingRecord` varchar(10) DEFAULT NULL,
  `AuctionModel` varchar(10) DEFAULT NULL,
  `Enrollment` varchar(10) DEFAULT NULL,
  `SetReminders` int DEFAULT NULL,
  `Onlookers` varchar(10) DEFAULT NULL,
  `CreatedOn` datetime DEFAULT NULL,
  `UpdatedOn` datetime DEFAULT NULL,
  `StatusId` int DEFAULT NULL,
  `SpiderStatusId` int DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=227 DEFAULT CHARSET=utf8;
