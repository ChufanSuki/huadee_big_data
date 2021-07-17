/*
Navicat MySQL Data Transfer

Source Server         : ailab
Source Server Version : 80018
Source Host           : localhost:3306
Source Database       : encryption_currency

Target Server Type    : MYSQL
Target Server Version : 80018
File Encoding         : 65001

Date: 2021-07-17 11:14:00
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `name` varchar(255) NOT NULL,
  `position` varchar(255) DEFAULT NULL,
  `work_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `jurisdiction` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('xwb', 'manager', '2021-07-01 18:55:06', '1');
