/*
Navicat MySQL Data Transfer

Source Server         : ailab
Source Server Version : 80018
Source Host           : localhost:3306
Source Database       : encryption_currency

Target Server Type    : MYSQL
Target Server Version : 80018
File Encoding         : 65001

Date: 2021-07-15 13:36:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `name` varchar(255) NOT NULL,
  `pwd` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('Anne', '123456', '213121@qq.com');
INSERT INTO `user` VALUES ('Jack', '111111', '123456@qq.com');
INSERT INTO `user` VALUES ('Tom', '123456', '10086@qq.com');
INSERT INTO `user` VALUES ('wj', '123456', 'wj@163.com');
INSERT INTO `user` VALUES ('www', '111111', '111111@qq.com');
INSERT INTO `user` VALUES ('xf', '111111', '111@163.com');
INSERT INTO `user` VALUES ('xwb', '123456', 'xwb_byron@163.com');
