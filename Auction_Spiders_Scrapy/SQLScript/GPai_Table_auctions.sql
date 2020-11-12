/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : auction_spider_ali

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-11-02 22:13:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auctions
-- ----------------------------
DROP TABLE IF EXISTS `auctions`;
CREATE TABLE `auctions` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `AuctionId` varchar(14) NOT NULL,
  `CourtId` varchar(20) NOT NULL,
  `Title` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `CategoryId` int NOT NULL,
  `Url` varchar(80) NOT NULL,
  `StartPrice` decimal(18,2) NOT NULL,
  `CurrentPrice` decimal(18,2) NOT NULL,
  `CashDeposit` varchar(80) DEFAULT NULL,
  `PaymentAdvance` varchar(80) DEFAULT NULL,
  `AccessPrice` decimal(18,2) DEFAULT NULL,
  `FareIncrease` decimal(18,2) DEFAULT NULL,
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
  `StatusId` int NOT NULL,
  `SpiderStatusId` int NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=29913 DEFAULT CHARSET=utf8;
