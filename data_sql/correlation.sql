/*
 Navicat Premium Data Transfer

 Source Server         : flask
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : localhost:3306
 Source Schema         : flask

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 19/07/2021 10:23:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for correlation
-- ----------------------------
DROP TABLE IF EXISTS `correlation`;
CREATE TABLE `correlation`  (
  `symbol` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ADA` float(255, 6) NULL DEFAULT NULL,
  `BNB` float(255, 6) NULL DEFAULT NULL,
  `BTC` float(255, 6) NULL DEFAULT NULL,
  `BUSD` float(255, 6) NULL DEFAULT NULL,
  `DOGE` float(255, 6) NULL DEFAULT NULL,
  `ETH` float(255, 6) NULL DEFAULT NULL,
  `SOL` float(255, 6) NULL DEFAULT NULL,
  `UNI` float(255, 6) NULL DEFAULT NULL,
  `USDC` float(255, 6) NULL DEFAULT NULL,
  `USDT` float(255, 6) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of correlation
-- ----------------------------
INSERT INTO `correlation` VALUES ('ADA', 1.000000, 0.928876, 0.865326, -0.190426, 0.934907, 0.947288, 0.738491, 0.950161, -0.236224, -0.069191);
INSERT INTO `correlation` VALUES ('BNB', 0.928876, 1.000000, 0.921694, -0.125832, 0.914666, 0.966160, 0.757116, 0.948687, -0.194065, -0.173417);
INSERT INTO `correlation` VALUES ('BTC', 0.865326, 0.921694, 1.000000, -0.196794, 0.895729, 0.929493, 0.660475, 0.884807, -0.246808, -0.089618);
INSERT INTO `correlation` VALUES ('BUSD', -0.190426, -0.125832, -0.196794, 1.000000, -0.104200, -0.214600, -0.056186, -0.225905, 0.965012, 0.519739);
INSERT INTO `correlation` VALUES ('DOGE', 0.934907, 0.914666, 0.895729, -0.104200, 1.000000, 0.934835, 0.685372, 0.908156, -0.144207, 0.061165);
INSERT INTO `correlation` VALUES ('ETH', 0.947288, 0.966160, 0.929493, -0.214600, 0.934835, 1.000000, 0.708878, 0.978670, -0.263806, -0.091166);
INSERT INTO `correlation` VALUES ('SOL', 0.738491, 0.757116, 0.660475, -0.056186, 0.685372, 0.708878, 1.000000, 0.664237, -0.091869, -0.041254);
INSERT INTO `correlation` VALUES ('UNI', 0.950161, 0.948687, 0.884807, -0.225905, 0.908156, 0.978670, 0.664237, 1.000000, -0.282891, -0.114016);
INSERT INTO `correlation` VALUES ('USDC', -0.236224, -0.194065, -0.246808, 0.965012, -0.144207, -0.263806, -0.091869, -0.282891, 1.000000, 0.602828);
INSERT INTO `correlation` VALUES ('USDT', -0.069191, -0.173417, -0.089618, 0.519739, 0.061165, -0.091166, -0.041254, -0.114016, 0.602828, 1.000000);

SET FOREIGN_KEY_CHECKS = 1;
