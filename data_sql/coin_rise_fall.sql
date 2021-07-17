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

 Date: 17/07/2021 09:58:18
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for coin_rise_fall
-- ----------------------------
DROP TABLE IF EXISTS `coin_rise_fall`;
CREATE TABLE `coin_rise_fall`  (
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `symbol` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `close_today` float(255, 4) NULL DEFAULT NULL,
  `close_one_day_ago` float(255, 4) NULL DEFAULT NULL,
  `one_day_%` float(255, 2) NULL DEFAULT NULL,
  `close_one_week_ago` float(255, 4) NULL DEFAULT NULL,
  `one_week_%` float(255, 2) NULL DEFAULT NULL,
  `close_one_month_ago` float(255, 4) NULL DEFAULT NULL,
  `one_month_%` float(255, 2) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of coin_rise_fall
-- ----------------------------
INSERT INTO `coin_rise_fall` VALUES ('Synthetix', 'SNX', 12.3941, 11.0510, 12.15, 8.6175, 43.83, 8.6218, 43.75);
INSERT INTO `coin_rise_fall` VALUES ('Stacks', 'STX', 1.3774, 1.2296, 12.01, 0.8554, 61.03, 0.8830, 55.99);
INSERT INTO `coin_rise_fall` VALUES ('Nano', 'NANO', 4.7792, 4.3084, 10.93, 4.9288, -3.04, 6.0826, -21.43);
INSERT INTO `coin_rise_fall` VALUES ('KuCoin Token', 'KCS', 13.9397, 12.7759, 9.11, 7.7263, 80.42, 7.9339, 75.70);
INSERT INTO `coin_rise_fall` VALUES ('Axie Infinity', 'AXS', 18.9577, 17.6503, 7.41, 8.7953, 115.54, 4.2751, 343.45);
INSERT INTO `coin_rise_fall` VALUES ('Enjin Coin', 'ENJ', 1.3737, 1.2875, 6.69, 1.1705, 17.36, 1.2966, 5.95);
INSERT INTO `coin_rise_fall` VALUES ('Terra', 'LUNA', 8.4223, 7.8951, 6.68, 5.9733, 41.00, 5.5515, 51.71);
INSERT INTO `coin_rise_fall` VALUES ('IOTA', 'MIOTA', 0.8405, 0.7930, 5.99, 0.8441, -0.44, 1.0383, -19.05);
INSERT INTO `coin_rise_fall` VALUES ('Arweave', 'AR', 11.3654, 10.7626, 5.60, 10.9647, 3.65, 15.4979, -26.66);
INSERT INTO `coin_rise_fall` VALUES ('The Graph', 'GRT', 0.7109, 0.6840, 3.92, 0.7200, -1.26, 0.6147, 15.65);
INSERT INTO `coin_rise_fall` VALUES ('Huobi Token', 'HT', 9.4302, 9.1090, 3.53, 10.7284, -12.10, 13.7422, -31.38);
INSERT INTO `coin_rise_fall` VALUES ('Aave', 'AAVE', 304.6820, 294.8110, 3.35, 277.0390, 9.98, 285.0820, 6.88);
INSERT INTO `coin_rise_fall` VALUES ('Horizen', 'ZEN', 60.6447, 58.7131, 3.29, 67.3187, -9.91, 79.4354, -23.66);
INSERT INTO `coin_rise_fall` VALUES ('Avalanche', 'AVAX', 12.4137, 12.0257, 3.23, 12.3501, 0.51, 13.4190, -7.49);
INSERT INTO `coin_rise_fall` VALUES ('Flow', 'FLOW', 19.4796, 18.8697, 3.23, 11.0651, 76.05, 13.0421, 49.36);
INSERT INTO `coin_rise_fall` VALUES ('ICON', 'ICX', 0.9511, 0.9221, 3.15, 0.8487, 12.06, 0.9046, 5.14);
INSERT INTO `coin_rise_fall` VALUES ('THORChain', 'RUNE', 6.2857, 6.1055, 2.95, 6.2492, 0.58, 7.2701, -13.54);
INSERT INTO `coin_rise_fall` VALUES ('NEAR Protocol', 'NEAR', 2.1686, 2.1080, 2.87, 2.2914, -5.36, 3.0219, -28.24);
INSERT INTO `coin_rise_fall` VALUES ('Compound', 'COMP', 435.0520, 422.9770, 2.85, 444.5560, -2.14, 294.6310, 47.66);
INSERT INTO `coin_rise_fall` VALUES ('FTX Token', 'FTT', 30.9848, 30.1395, 2.80, 27.4490, 12.88, 31.5204, -1.70);
INSERT INTO `coin_rise_fall` VALUES ('Internet Computer', 'ICP', 39.6904, 38.6132, 2.79, 46.8516, -15.28, 58.2379, -31.85);
INSERT INTO `coin_rise_fall` VALUES ('EOS', 'EOS', 4.0725, 3.9721, 2.53, 4.0599, 0.31, 4.9195, -17.22);
INSERT INTO `coin_rise_fall` VALUES ('SHIBA INU', 'SHIB', 0.0000, 0.0000, 2.48, 0.0000, -9.86, 0.0000, 26.57);
INSERT INTO `coin_rise_fall` VALUES ('Fantom', 'FTM', 0.2312, 0.2256, 2.46, 0.2427, -4.76, 0.2528, -8.56);
INSERT INTO `coin_rise_fall` VALUES ('Telcoin', 'TEL', 0.0174, 0.0170, 2.36, 0.0245, -29.10, 0.0299, -41.80);
INSERT INTO `coin_rise_fall` VALUES ('Zcash', 'ZEC', 110.6980, 108.1530, 2.35, 120.1590, -7.87, 124.7180, -11.24);
INSERT INTO `coin_rise_fall` VALUES ('Klaytn', 'KLAY', 0.9881, 0.9657, 2.32, 1.0293, -4.01, 1.0083, -2.01);
INSERT INTO `coin_rise_fall` VALUES ('VeChain', 'VET', 0.0776, 0.0759, 2.21, 0.0878, -11.59, 0.1049, -25.98);
INSERT INTO `coin_rise_fall` VALUES ('Wrapped Bitcoin', 'WBTC', 34253.8008, 33516.6992, 2.20, 35289.8008, -2.94, 37259.8984, -8.07);
INSERT INTO `coin_rise_fall` VALUES ('Uniswap', 'UNI', 20.6810, 20.2438, 2.16, 20.7719, -0.44, 21.8510, -5.35);
INSERT INTO `coin_rise_fall` VALUES ('Bitcoin', 'BTC', 34240.1992, 33520.5000, 2.15, 35287.8008, -2.97, 37334.3984, -8.29);
INSERT INTO `coin_rise_fall` VALUES ('Tezos', 'XTZ', 2.8431, 2.7859, 2.05, 3.0405, -6.49, 3.1358, -9.33);
INSERT INTO `coin_rise_fall` VALUES ('Ontology', 'ONT', 0.7020, 0.6883, 1.99, 0.7206, -2.58, 0.9265, -24.24);
INSERT INTO `coin_rise_fall` VALUES ('DigiByte', 'DGB', 0.0415, 0.0407, 1.97, 0.0456, -9.02, 0.0563, -26.28);
INSERT INTO `coin_rise_fall` VALUES ('Bitcoin BEP2', 'BTCB', 34272.8008, 33622.8984, 1.93, 35403.1992, -3.19, 37167.1992, -7.79);
INSERT INTO `coin_rise_fall` VALUES ('Binance Coin', 'BNB', 322.0320, 316.1400, 1.86, 307.7320, 4.65, 345.9340, -6.91);
INSERT INTO `coin_rise_fall` VALUES ('SushiSwap', 'SUSHI', 8.1445, 7.9964, 1.85, 7.9389, 2.59, 8.5613, -4.87);
INSERT INTO `coin_rise_fall` VALUES ('yearn.finance', 'YFI', 33757.5000, 33158.6016, 1.81, 33404.6016, 1.06, 36897.1016, -8.51);
INSERT INTO `coin_rise_fall` VALUES ('QuadrantProtocol', 'EQUAD', 0.0044, 0.0043, 1.75, 0.0045, -3.91, 0.0052, -16.73);
INSERT INTO `coin_rise_fall` VALUES ('XRP', 'XRP', 0.6359, 0.6255, 1.67, 0.6949, -8.49, 0.8484, -25.05);
INSERT INTO `coin_rise_fall` VALUES ('Amp', 'AMP', 0.0550, 0.0542, 1.55, 0.0557, -1.24, 0.0614, -10.49);
INSERT INTO `coin_rise_fall` VALUES ('Filecoin', 'FIL', 55.0963, 54.2645, 1.53, 58.7723, -6.25, 70.8168, -22.20);
INSERT INTO `coin_rise_fall` VALUES ('SwissBorg', 'CHSB', 0.6194, 0.6102, 1.51, 0.6280, -1.37, 0.6793, -8.82);
INSERT INTO `coin_rise_fall` VALUES ('Siacoin', 'SC', 0.0130, 0.0128, 1.49, 0.0140, -6.98, 0.0154, -15.67);
INSERT INTO `coin_rise_fall` VALUES ('Holo', 'HOT', 0.0058, 0.0057, 1.48, 0.0062, -6.51, 0.0075, -23.22);
INSERT INTO `coin_rise_fall` VALUES ('OKB', 'OKB', 9.8654, 9.7220, 1.47, 10.7238, -8.00, 13.8486, -28.76);
INSERT INTO `coin_rise_fall` VALUES ('Bitcoin Gold', 'BTG', 44.8514, 44.2044, 1.46, 48.5066, -7.54, 58.0387, -22.72);
INSERT INTO `coin_rise_fall` VALUES ('Bancor', 'BNT', 3.2375, 3.1933, 1.39, 3.3789, -4.18, 3.7947, -14.68);
INSERT INTO `coin_rise_fall` VALUES ('Hedera Hashgraph', 'HBAR', 0.1716, 0.1692, 1.37, 0.1942, -11.67, 0.1996, -14.07);
INSERT INTO `coin_rise_fall` VALUES ('Kusama', 'KSM', 210.5110, 207.6890, 1.36, 210.1210, 0.19, 414.6320, -49.23);
INSERT INTO `coin_rise_fall` VALUES ('Ethereum', 'ETH', 2139.6599, 2111.3999, 1.34, 2321.7200, -7.84, 2353.7700, -9.10);
INSERT INTO `coin_rise_fall` VALUES ('PancakeSwap', 'CAKE', 15.1519, 14.9594, 1.29, 14.1629, 6.98, 15.9665, -5.10);
INSERT INTO `coin_rise_fall` VALUES ('Polkadot', 'DOT', 15.4824, 15.2908, 1.25, 16.0140, -3.32, 20.9859, -26.22);
INSERT INTO `coin_rise_fall` VALUES ('Solana', 'SOL', 32.1778, 31.7886, 1.22, 34.3106, -6.22, 36.0461, -10.73);
INSERT INTO `coin_rise_fall` VALUES ('Polygon', 'MATIC', 1.0421, 1.0299, 1.19, 1.1479, -9.21, 1.2520, -16.76);
INSERT INTO `coin_rise_fall` VALUES ('Zilliqa', 'ZIL', 0.0738, 0.0730, 1.12, 0.0830, -11.06, 0.1023, -27.88);
INSERT INTO `coin_rise_fall` VALUES ('NEM', 'XEM', 0.1226, 0.1213, 1.07, 0.1376, -10.92, 0.1641, -25.32);
INSERT INTO `coin_rise_fall` VALUES ('Ethereum Classic', 'ETC', 49.6904, 49.1709, 1.06, 56.2457, -11.65, 56.9562, -12.76);
INSERT INTO `coin_rise_fall` VALUES ('Elrond', 'EGLD', 89.1919, 88.2634, 1.05, 93.5920, -4.70, 81.0330, 10.07);
INSERT INTO `coin_rise_fall` VALUES ('XinFin Network', 'XDC', 0.0928, 0.0919, 1.04, 0.1185, -21.70, 0.0480, 93.47);
INSERT INTO `coin_rise_fall` VALUES ('Monero', 'XMR', 211.5210, 209.5570, 0.94, 219.8410, -3.78, 242.9820, -12.95);
INSERT INTO `coin_rise_fall` VALUES ('Chiliz', 'CHZ', 0.2579, 0.2555, 0.94, 0.2432, 6.04, 0.2959, -12.84);
INSERT INTO `coin_rise_fall` VALUES ('BitTorrent', 'BTT', 0.0025, 0.0025, 0.94, 0.0027, -7.63, 0.0035, -27.32);
INSERT INTO `coin_rise_fall` VALUES ('Dogecoin', 'DOGE', 0.2159, 0.2139, 0.91, 0.2465, -12.43, 0.3194, -32.41);
INSERT INTO `coin_rise_fall` VALUES ('Theta Fuel', 'TFUEL', 0.3458, 0.3427, 0.90, 0.3757, -7.96, 0.4814, -28.18);
INSERT INTO `coin_rise_fall` VALUES ('Waves', 'WAVES', 14.3129, 14.1847, 0.90, 16.8867, -15.24, 14.0156, 2.12);
INSERT INTO `coin_rise_fall` VALUES ('Cardano', 'ADA', 1.3481, 1.3361, 0.90, 1.4582, -7.55, 1.4364, -6.14);
INSERT INTO `coin_rise_fall` VALUES ('Basic Attention Token', 'BAT', 0.5622, 0.5574, 0.88, 0.6045, -6.98, 0.6476, -13.19);
INSERT INTO `coin_rise_fall` VALUES ('Chainlink', 'LINK', 18.3640, 18.2078, 0.86, 19.2628, -4.67, 21.4790, -14.50);
INSERT INTO `coin_rise_fall` VALUES ('Qtum', 'QTUM', 6.6980, 6.6417, 0.85, 7.3923, -9.39, 9.0624, -26.09);
INSERT INTO `coin_rise_fall` VALUES ('TRON', 'TRX', 0.0618, 0.0614, 0.73, 0.0673, -8.14, 0.0691, -10.59);
INSERT INTO `coin_rise_fall` VALUES ('0x', 'ZRX', 0.7947, 0.7891, 0.71, 0.7236, 9.83, 0.8637, -7.99);
INSERT INTO `coin_rise_fall` VALUES ('UNUS SED LEO', 'LEO', 2.8967, 2.8780, 0.65, 2.4084, 20.27, 2.4039, 20.50);
INSERT INTO `coin_rise_fall` VALUES ('THETA', 'THETA', 5.9300, 5.9027, 0.46, 6.3502, -6.62, 7.9582, -25.49);
INSERT INTO `coin_rise_fall` VALUES ('Curve DAO Token', 'CRV', 1.7567, 1.7500, 0.38, 1.8408, -4.56, 2.1565, -18.54);
INSERT INTO `coin_rise_fall` VALUES ('Stellar', 'XLM', 0.2462, 0.2453, 0.34, 0.2681, -8.19, 0.3187, -22.75);
INSERT INTO `coin_rise_fall` VALUES ('Neo', 'NEO', 34.2199, 34.1085, 0.33, 37.4491, -8.62, 47.4673, -27.91);
INSERT INTO `coin_rise_fall` VALUES ('Nexo', 'NEXO', 1.6321, 1.6275, 0.28, 1.5548, 4.98, 1.9174, -14.88);
INSERT INTO `coin_rise_fall` VALUES ('Litecoin', 'LTC', 134.2460, 133.9870, 0.19, 144.9060, -7.36, 162.8810, -17.58);
INSERT INTO `coin_rise_fall` VALUES ('Bitcoin Cash', 'BCH', 498.2140, 497.5000, 0.14, 526.4300, -5.36, 578.2720, -13.84);
INSERT INTO `coin_rise_fall` VALUES ('Algorand', 'ALGO', 0.8924, 0.8919, 0.06, 0.8798, 1.43, 0.9712, -8.11);
INSERT INTO `coin_rise_fall` VALUES ('Dai', 'DAI', 1.0007, 1.0000, 0.06, 1.0006, 0.01, 1.0013, -0.07);
INSERT INTO `coin_rise_fall` VALUES ('Decred', 'DCR', 133.7450, 133.6780, 0.05, 138.5460, -3.47, 139.2510, -3.95);
INSERT INTO `coin_rise_fall` VALUES ('TrueUSD', 'TUSD', 1.0004, 1.0000, 0.04, 0.9993, 0.11, 1.0006, -0.02);
INSERT INTO `coin_rise_fall` VALUES ('Paxos Standard', 'PAX', 1.0003, 1.0000, 0.03, 0.9993, 0.10, 1.0004, -0.01);
INSERT INTO `coin_rise_fall` VALUES ('Dash', 'DASH', 128.3680, 128.3340, 0.03, 140.2720, -8.49, 165.6770, -22.52);
INSERT INTO `coin_rise_fall` VALUES ('TerraUSD', 'UST', 1.0007, 1.0003, 0.03, 0.9997, 0.10, 1.0000, 0.07);
INSERT INTO `coin_rise_fall` VALUES ('Tether', 'USDT', 1.0002, 1.0000, 0.02, 0.9995, 0.07, 1.0005, -0.03);
INSERT INTO `coin_rise_fall` VALUES ('Binance USD', 'BUSD', 1.0003, 1.0001, 0.02, 0.9994, 0.09, 1.0004, -0.01);
INSERT INTO `coin_rise_fall` VALUES ('USD Coin', 'USDC', 1.0003, 1.0002, 0.01, 0.9995, 0.08, 1.0004, -0.02);
INSERT INTO `coin_rise_fall` VALUES ('Maker', 'MKR', 2667.4099, 2667.5200, 0.00, 2798.5200, -4.68, 2920.7000, -8.67);
INSERT INTO `coin_rise_fall` VALUES ('Celsius', 'CEL', 6.2031, 6.2073, -0.07, 6.9208, -10.37, 7.1672, -13.45);
INSERT INTO `coin_rise_fall` VALUES ('Mdex', 'MDX', 1.6126, 1.6185, -0.37, 1.6695, -3.41, 2.0048, -19.56);
INSERT INTO `coin_rise_fall` VALUES ('Harmony', 'ONE', 0.0821, 0.0824, -0.40, 0.0667, 23.02, 0.0786, 4.51);
INSERT INTO `coin_rise_fall` VALUES ('Bitcoin SV', 'BSV', 138.2880, 138.9680, -0.49, 149.3190, -7.39, 164.1900, -15.78);
INSERT INTO `coin_rise_fall` VALUES ('Celo', 'CELO', 2.8876, 2.9056, -0.62, 3.4154, -15.45, 2.6056, 10.82);
INSERT INTO `coin_rise_fall` VALUES ('Helium', 'HNT', 12.8115, 12.9427, -1.01, 13.3806, -4.25, 13.4288, -4.60);
INSERT INTO `coin_rise_fall` VALUES ('Decentraland', 'MANA', 0.7442, 0.7522, -1.06, 0.5805, 28.21, 0.6940, 7.23);
INSERT INTO `coin_rise_fall` VALUES ('Quant', 'QNT', 79.3276, 80.9000, -1.94, 81.7589, -2.97, 51.6637, 53.55);
INSERT INTO `coin_rise_fall` VALUES ('Cosmos', 'ATOM', 14.0626, 14.4009, -2.35, 12.2635, 14.67, 11.9371, 17.81);

SET FOREIGN_KEY_CHECKS = 1;
