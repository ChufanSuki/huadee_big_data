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

 Date: 16/07/2021 15:06:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for marketcap_percentage
-- ----------------------------
DROP TABLE IF EXISTS `marketcap_percentage`;
CREATE TABLE `marketcap_percentage`  (
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `symbol` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `date` datetime(0) NULL DEFAULT NULL,
  `market_cap` double(255, 0) NULL DEFAULT NULL,
  `percentage` float(255, 4) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of marketcap_percentage
-- ----------------------------
INSERT INTO `marketcap_percentage` VALUES ('Bitcoin', 'BTC', '2021-07-11 00:00:00', 642138000000, 0.4669);
INSERT INTO `marketcap_percentage` VALUES ('Ethereum', 'ETH', '2021-07-11 00:00:00', 249602000000, 0.1815);
INSERT INTO `marketcap_percentage` VALUES ('Tether', 'USDT', '2021-07-11 00:00:00', 62219400000, 0.0452);
INSERT INTO `marketcap_percentage` VALUES ('Binance Coin', 'BNB', '2021-07-11 00:00:00', 49410200000, 0.0359);
INSERT INTO `marketcap_percentage` VALUES ('Cardano', 'ADA', '2021-07-11 00:00:00', 43068300000, 0.0313);
INSERT INTO `marketcap_percentage` VALUES ('XRP', 'XRP', '2021-07-11 00:00:00', 29362300000, 0.0214);
INSERT INTO `marketcap_percentage` VALUES ('Dogecoin', 'DOGE', '2021-07-11 00:00:00', 28147300000, 0.0205);
INSERT INTO `marketcap_percentage` VALUES ('USD Coin', 'USDC', '2021-07-11 00:00:00', 26133700000, 0.0190);
INSERT INTO `marketcap_percentage` VALUES ('Polkadot', 'DOT', '2021-07-11 00:00:00', 14857100000, 0.0108);
INSERT INTO `marketcap_percentage` VALUES ('Uniswap', 'UNI', '2021-07-11 00:00:00', 12145700000, 0.0088);
INSERT INTO `marketcap_percentage` VALUES ('Binance USD', 'BUSD', '2021-07-11 00:00:00', 10699000000, 0.0078);
INSERT INTO `marketcap_percentage` VALUES ('Bitcoin Cash', 'BCH', '2021-07-11 00:00:00', 9359950000, 0.0068);
INSERT INTO `marketcap_percentage` VALUES ('Litecoin', 'LTC', '2021-07-11 00:00:00', 8961230000, 0.0065);
INSERT INTO `marketcap_percentage` VALUES ('Solana', 'SOL', '2021-07-11 00:00:00', 8772880000, 0.0064);
INSERT INTO `marketcap_percentage` VALUES ('Chainlink', 'LINK', '2021-07-11 00:00:00', 8052780000, 0.0059);
INSERT INTO `marketcap_percentage` VALUES ('Wrapped Bitcoin', 'WBTC', '2021-07-11 00:00:00', 6750560000, 0.0049);
INSERT INTO `marketcap_percentage` VALUES ('Polygon', 'MATIC', '2021-07-11 00:00:00', 6597400000, 0.0048);
INSERT INTO `marketcap_percentage` VALUES ('THETA', 'THETA', '2021-07-11 00:00:00', 5930010000, 0.0043);
INSERT INTO `marketcap_percentage` VALUES ('Ethereum Classic', 'ETC', '2021-07-11 00:00:00', 5779660000, 0.0042);
INSERT INTO `marketcap_percentage` VALUES ('Stellar', 'XLM', '2021-07-11 00:00:00', 5728290000, 0.0042);
INSERT INTO `marketcap_percentage` VALUES ('Dai', 'DAI', '2021-07-11 00:00:00', 5494800000, 0.0040);
INSERT INTO `marketcap_percentage` VALUES ('Internet Computer', 'ICP', '2021-07-11 00:00:00', 5433580000, 0.0040);
INSERT INTO `marketcap_percentage` VALUES ('VeChain', 'VET', '2021-07-11 00:00:00', 4992730000, 0.0036);
INSERT INTO `marketcap_percentage` VALUES ('Filecoin', 'FIL', '2021-07-11 00:00:00', 4788240000, 0.0035);
INSERT INTO `marketcap_percentage` VALUES ('TRON', 'TRX', '2021-07-11 00:00:00', 4430210000, 0.0032);
INSERT INTO `marketcap_percentage` VALUES ('Aave', 'AAVE', '2021-07-11 00:00:00', 3911050000, 0.0028);
INSERT INTO `marketcap_percentage` VALUES ('EOS', 'EOS', '2021-07-11 00:00:00', 3889620000, 0.0028);
INSERT INTO `marketcap_percentage` VALUES ('Monero', 'XMR', '2021-07-11 00:00:00', 3796930000, 0.0028);
INSERT INTO `marketcap_percentage` VALUES ('Terra', 'LUNA', '2021-07-11 00:00:00', 3532350000, 0.0026);
INSERT INTO `marketcap_percentage` VALUES ('SHIBA INU', 'SHIB', '2021-07-11 00:00:00', 3103830000, 0.0023);
INSERT INTO `marketcap_percentage` VALUES ('Cosmos', 'ATOM', '2021-07-11 00:00:00', 3065220000, 0.0022);
INSERT INTO `marketcap_percentage` VALUES ('PancakeSwap', 'CAKE', '2021-07-11 00:00:00', 2948010000, 0.0021);
INSERT INTO `marketcap_percentage` VALUES ('FTX Token', 'FTT', '2021-07-11 00:00:00', 2923330000, 0.0021);
INSERT INTO `marketcap_percentage` VALUES ('Algorand', 'ALGO', '2021-07-11 00:00:00', 2783900000, 0.0020);
INSERT INTO `marketcap_percentage` VALUES ('UNUS SED LEO', 'LEO', '2021-07-11 00:00:00', 2763290000, 0.0020);
INSERT INTO `marketcap_percentage` VALUES ('Maker', 'MKR', '2021-07-11 00:00:00', 2644280000, 0.0019);
INSERT INTO `marketcap_percentage` VALUES ('Bitcoin SV', 'BSV', '2021-07-11 00:00:00', 2597650000, 0.0019);
INSERT INTO `marketcap_percentage` VALUES ('Bitcoin BEP2', 'BTCB', '2021-07-11 00:00:00', 2505180000, 0.0018);
INSERT INTO `marketcap_percentage` VALUES ('Klaytn', 'KLAY', '2021-07-11 00:00:00', 2455020000, 0.0018);
INSERT INTO `marketcap_percentage` VALUES ('Tezos', 'XTZ', '2021-07-11 00:00:00', 2422650000, 0.0018);
INSERT INTO `marketcap_percentage` VALUES ('Neo', 'NEO', '2021-07-11 00:00:00', 2413830000, 0.0018);
INSERT INTO `marketcap_percentage` VALUES ('IOTA', 'MIOTA', '2021-07-11 00:00:00', 2336080000, 0.0017);
INSERT INTO `marketcap_percentage` VALUES ('Compound', 'COMP', '2021-07-11 00:00:00', 2326430000, 0.0017);
INSERT INTO `marketcap_percentage` VALUES ('Amp', 'AMP', '2021-07-11 00:00:00', 2322540000, 0.0017);
INSERT INTO `marketcap_percentage` VALUES ('Avalanche', 'AVAX', '2021-07-11 00:00:00', 2140340000, 0.0016);
INSERT INTO `marketcap_percentage` VALUES ('The Graph', 'GRT', '2021-07-11 00:00:00', 2060060000, 0.0015);
INSERT INTO `marketcap_percentage` VALUES ('TerraUSD', 'UST', '2021-07-11 00:00:00', 1930960000, 0.0014);
INSERT INTO `marketcap_percentage` VALUES ('Theta Fuel', 'TFUEL', '2021-07-11 00:00:00', 1832970000, 0.0013);
INSERT INTO `marketcap_percentage` VALUES ('Kusama', 'KSM', '2021-07-11 00:00:00', 1783050000, 0.0013);
INSERT INTO `marketcap_percentage` VALUES ('Decred', 'DCR', '2021-07-11 00:00:00', 1753310000, 0.0013);
INSERT INTO `marketcap_percentage` VALUES ('Elrond', 'EGLD', '2021-07-11 00:00:00', 1700520000, 0.0012);
INSERT INTO `marketcap_percentage` VALUES ('BitTorrent', 'BTT', '2021-07-11 00:00:00', 1666780000, 0.0012);
INSERT INTO `marketcap_percentage` VALUES ('Stacks', 'STX', '2021-07-11 00:00:00', 1628210000, 0.0012);
INSERT INTO `marketcap_percentage` VALUES ('Huobi Token', 'HT', '2021-07-11 00:00:00', 1609790000, 0.0012);
INSERT INTO `marketcap_percentage` VALUES ('Hedera Hashgraph', 'HBAR', '2021-07-11 00:00:00', 1535410000, 0.0011);
INSERT INTO `marketcap_percentage` VALUES ('Chiliz', 'CHZ', '2021-07-11 00:00:00', 1520020000, 0.0011);
INSERT INTO `marketcap_percentage` VALUES ('Waves', 'WAVES', '2021-07-11 00:00:00', 1511520000, 0.0011);
INSERT INTO `marketcap_percentage` VALUES ('TrueUSD', 'TUSD', '2021-07-11 00:00:00', 1509550000, 0.0011);
INSERT INTO `marketcap_percentage` VALUES ('Celsius', 'CEL', '2021-07-11 00:00:00', 1481700000, 0.0011);
INSERT INTO `marketcap_percentage` VALUES ('THORChain', 'RUNE', '2021-07-11 00:00:00', 1471600000, 0.0011);
INSERT INTO `marketcap_percentage` VALUES ('Synthetix', 'SNX', '2021-07-11 00:00:00', 1423360000, 0.0010);
INSERT INTO `marketcap_percentage` VALUES ('Zcash', 'ZEC', '2021-07-11 00:00:00', 1348910000, 0.0010);
INSERT INTO `marketcap_percentage` VALUES ('Dash', 'DASH', '2021-07-11 00:00:00', 1312690000, 0.0010);
INSERT INTO `marketcap_percentage` VALUES ('Decentraland', 'MANA', '2021-07-11 00:00:00', 1254400000, 0.0009);
INSERT INTO `marketcap_percentage` VALUES ('yearn.finance', 'YFI', '2021-07-11 00:00:00', 1236720000, 0.0009);
INSERT INTO `marketcap_percentage` VALUES ('Axie Infinity', 'AXS', '2021-07-11 00:00:00', 1154670000, 0.0008);
INSERT INTO `marketcap_percentage` VALUES ('Helium', 'HNT', '2021-07-11 00:00:00', 1150690000, 0.0008);
INSERT INTO `marketcap_percentage` VALUES ('Enjin Coin', 'ENJ', '2021-07-11 00:00:00', 1146120000, 0.0008);
INSERT INTO `marketcap_percentage` VALUES ('XinFin Network', 'XDC', '2021-07-11 00:00:00', 1139700000, 0.0008);
INSERT INTO `marketcap_percentage` VALUES ('KuCoin Token', 'KCS', '2021-07-11 00:00:00', 1116830000, 0.0008);
INSERT INTO `marketcap_percentage` VALUES ('NEM', 'XEM', '2021-07-11 00:00:00', 1103290000, 0.0008);
INSERT INTO `marketcap_percentage` VALUES ('SushiSwap', 'SUSHI', '2021-07-11 00:00:00', 1036340000, 0.0008);
INSERT INTO `marketcap_percentage` VALUES ('Holo', 'HOT', '2021-07-11 00:00:00', 996498000, 0.0007);
INSERT INTO `marketcap_percentage` VALUES ('Quant', 'QNT', '2021-07-11 00:00:00', 957701000, 0.0007);
INSERT INTO `marketcap_percentage` VALUES ('Telcoin', 'TEL', '2021-07-11 00:00:00', 942413000, 0.0007);
INSERT INTO `marketcap_percentage` VALUES ('Paxos Standard', 'PAX', '2021-07-11 00:00:00', 921450000, 0.0007);
INSERT INTO `marketcap_percentage` VALUES ('Nexo', 'NEXO', '2021-07-11 00:00:00', 913995000, 0.0007);
INSERT INTO `marketcap_percentage` VALUES ('NEAR Protocol', 'NEAR', '2021-07-11 00:00:00', 894611000, 0.0007);
INSERT INTO `marketcap_percentage` VALUES ('Mdex', 'MDX', '2021-07-11 00:00:00', 858588000, 0.0006);
INSERT INTO `marketcap_percentage` VALUES ('Zilliqa', 'ZIL', '2021-07-11 00:00:00', 846868000, 0.0006);
INSERT INTO `marketcap_percentage` VALUES ('Harmony', 'ONE', '2021-07-11 00:00:00', 846804000, 0.0006);
INSERT INTO `marketcap_percentage` VALUES ('Basic Attention Token', 'BAT', '2021-07-11 00:00:00', 842408000, 0.0006);
INSERT INTO `marketcap_percentage` VALUES ('Flow', 'FLOW', '2021-07-11 00:00:00', 826507000, 0.0006);
INSERT INTO `marketcap_percentage` VALUES ('Bitcoin Gold', 'BTG', '2021-07-11 00:00:00', 785524000, 0.0006);
INSERT INTO `marketcap_percentage` VALUES ('Celo', 'CELO', '2021-07-11 00:00:00', 768049000, 0.0006);
INSERT INTO `marketcap_percentage` VALUES ('Bancor', 'BNT', '2021-07-11 00:00:00', 745880000, 0.0005);
INSERT INTO `marketcap_percentage` VALUES ('Horizen', 'ZEN', '2021-07-11 00:00:00', 684569000, 0.0005);
INSERT INTO `marketcap_percentage` VALUES ('0x', 'ZRX', '2021-07-11 00:00:00', 671769000, 0.0005);
INSERT INTO `marketcap_percentage` VALUES ('Curve DAO Token', 'CRV', '2021-07-11 00:00:00', 668494000, 0.0005);
INSERT INTO `marketcap_percentage` VALUES ('Qtum', 'QTUM', '2021-07-11 00:00:00', 659899000, 0.0005);
INSERT INTO `marketcap_percentage` VALUES ('Nano', 'NANO', '2021-07-11 00:00:00', 636815000, 0.0005);
INSERT INTO `marketcap_percentage` VALUES ('Siacoin', 'SC', '2021-07-11 00:00:00', 628554000, 0.0005);
INSERT INTO `marketcap_percentage` VALUES ('SwissBorg', 'CHSB', '2021-07-11 00:00:00', 619381000, 0.0005);
INSERT INTO `marketcap_percentage` VALUES ('Ontology', 'ONT', '2021-07-11 00:00:00', 615373000, 0.0004);
INSERT INTO `marketcap_percentage` VALUES ('ICON', 'ICX', '2021-07-11 00:00:00', 607666000, 0.0004);
INSERT INTO `marketcap_percentage` VALUES ('DigiByte', 'DGB', '2021-07-11 00:00:00', 601211000, 0.0004);
INSERT INTO `marketcap_percentage` VALUES ('OKB', 'OKB', '2021-07-11 00:00:00', 591926000, 0.0004);
INSERT INTO `marketcap_percentage` VALUES ('Fantom', 'FTM', '2021-07-11 00:00:00', 588390000, 0.0004);
INSERT INTO `marketcap_percentage` VALUES ('Arweave', 'AR', '2021-07-11 00:00:00', 379543000, 0.0003);
INSERT INTO `marketcap_percentage` VALUES ('QuadrantProtocol', 'EQUAD', '2021-07-11 00:00:00', 1815100, 0.0000);
INSERT INTO `marketcap_percentage` VALUES ('other5', 'other5', '2021-07-11 00:00:00', 328821000000, 0.2392);
INSERT INTO `marketcap_percentage` VALUES ('other6', 'other6', '2021-07-11 00:00:00', 299459000000, 0.2178);
INSERT INTO `marketcap_percentage` VALUES ('other7', 'other7', '2021-07-11 00:00:00', 271311000000, 0.1973);

SET FOREIGN_KEY_CHECKS = 1;
