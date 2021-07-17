/*
Navicat MySQL Data Transfer

Source Server         : ailab
Source Server Version : 80018
Source Host           : localhost:3306
Source Database       : encryption_currency

Target Server Type    : MYSQL
Target Server Version : 80018
File Encoding         : 65001

Date: 2021-07-17 11:14:15
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
  `regtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('xwb', 'e301e09074272624a246ebe0d25ded764018241a', 'xwb_byron@163.com', '2021-07-09 10:52:00');
INSERT INTO `user` VALUES ('xwb_test', 'd9ee2c4ee1f60fbd61c524c259fd57c9416dd0c8', 'xwb_byron@163.com', '2021-07-17 10:57:12');
INSERT INTO `user` VALUES ('xwb1', 'b55c98b55d061ba98cd8e749de603c7593741ba8', 'xwb_byron@163.com', '2021-07-17 10:58:58');
