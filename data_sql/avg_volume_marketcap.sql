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

 Date: 15/07/2021 14:50:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for avg_volume_marketcap
-- ----------------------------
DROP TABLE IF EXISTS `avg_volume_marketcap`;
CREATE TABLE `avg_volume_marketcap`  (
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `symbol` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `date` timestamp(0) NULL DEFAULT NULL,
  `volume_today` double NULL DEFAULT NULL,
  `market_cap_today` double NULL DEFAULT NULL,
  `avg_volume_week` double NULL DEFAULT NULL,
  `avg_market_cap_week` double NULL DEFAULT NULL,
  `avg_volume_month` double NULL DEFAULT NULL,
  `avg_market_cap_month` double NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of avg_volume_marketcap
-- ----------------------------
INSERT INTO `avg_volume_marketcap` VALUES ('Bitcoin', 'BTC', '2021-07-11 00:00:00', 20108700000, 642138000000, 25492271429, 632918285714, 35475326667, 655300233333);
INSERT INTO `avg_volume_marketcap` VALUES ('Ethereum', 'ETH', '2021-07-11 00:00:00', 14705400000, 249602000000, 20271228571, 255820857143, 23840713333, 254152866667);
INSERT INTO `avg_volume_marketcap` VALUES ('Tether', 'USDT', '2021-07-11 00:00:00', 33700900000, 62219400000, 46459100000, 62289542857, 57930210000, 62496220000);
INSERT INTO `avg_volume_marketcap` VALUES ('Binance Coin', 'BNB', '2021-07-11 00:00:00', 1189810000, 49410200000, 1626748571, 48570671429, 1885399000, 48295543333);
INSERT INTO `avg_volume_marketcap` VALUES ('Cardano', 'ADA', '2021-07-11 00:00:00', 870306000, 43068300000, 1386636571, 43766114286, 2473760200, 44144310000);
INSERT INTO `avg_volume_marketcap` VALUES ('XRP', 'XRP', '2021-07-11 00:00:00', 1495490000, 29362300000, 2015135714, 29630342857, 2691954333, 32438443333);
INSERT INTO `avg_volume_marketcap` VALUES ('Dogecoin', 'DOGE', '2021-07-11 00:00:00', 719870000, 28147300000, 1500370000, 28816314286, 2233503233, 33369563333);
INSERT INTO `avg_volume_marketcap` VALUES ('USD Coin', 'USDC', '2021-07-11 00:00:00', 1380260000, 26133700000, 1923410000, 25896214286, 2147933333, 25084526667);
INSERT INTO `avg_volume_marketcap` VALUES ('Polkadot', 'DOT', '2021-07-11 00:00:00', 543031000, 14857100000, 916702857, 15069914286, 1298771667, 16721416667);
INSERT INTO `avg_volume_marketcap` VALUES ('Uniswap', 'UNI', '2021-07-11 00:00:00', 268849000, 12145700000, 472082000, 12335914286, 405991867, 11454695333);
INSERT INTO `avg_volume_marketcap` VALUES ('Binance USD', 'BUSD', '2021-07-11 00:00:00', 2436380000, 10699000000, 3476434286, 10726671429, 4008476667, 10050579667);
INSERT INTO `avg_volume_marketcap` VALUES ('Bitcoin Cash', 'BCH', '2021-07-11 00:00:00', 1157460000, 9359950000, 1394465714, 9436034286, 1570407000, 9801741667);
INSERT INTO `avg_volume_marketcap` VALUES ('Litecoin', 'LTC', '2021-07-11 00:00:00', 1267260000, 8961230000, 1462597143, 9054901429, 1929565000, 9589011667);
INSERT INTO `avg_volume_marketcap` VALUES ('Solana', 'SOL', '2021-07-11 00:00:00', 211680000, 8772880000, 361721000, 9124782857, 509180833, 9262551667);
INSERT INTO `avg_volume_marketcap` VALUES ('Chainlink', 'LINK', '2021-07-11 00:00:00', 497212000, 8052780000, 857045000, 8242615714, 1046485267, 8591108667);
INSERT INTO `avg_volume_marketcap` VALUES ('Wrapped Bitcoin', 'WBTC', '2021-07-11 00:00:00', 118637000, 6750560000, 176787143, 6647818571, 199501300, 6745484667);
INSERT INTO `avg_volume_marketcap` VALUES ('Polygon', 'MATIC', '2021-07-11 00:00:00', 266687000, 6597400000, 472191571, 6795485714, 977143000, 7624922000);
INSERT INTO `avg_volume_marketcap` VALUES ('THETA', 'THETA', '2021-07-11 00:00:00', 131329000, 5930010000, 240730429, 6069842857, 289381033, 7191823000);
INSERT INTO `avg_volume_marketcap` VALUES ('Ethereum Classic', 'ETC', '2021-07-11 00:00:00', 1712980000, 5779660000, 2410308571, 5978698571, 2567581000, 5884332333);
INSERT INTO `avg_volume_marketcap` VALUES ('Stellar', 'XLM', '2021-07-11 00:00:00', 272218000, 5728290000, 346636429, 5821685714, 512095400, 6400772333);
INSERT INTO `avg_volume_marketcap` VALUES ('Dai', 'DAI', '2021-07-11 00:00:00', 224381000, 5494800000, 308053143, 5485164286, 328979467, 5306294333);
INSERT INTO `avg_volume_marketcap` VALUES ('Internet Computer', 'ICP', '2021-07-11 00:00:00', 123652000, 5433580000, 191335714, 5808280000, 298907367, 6178081333);
INSERT INTO `avg_volume_marketcap` VALUES ('VeChain', 'VET', '2021-07-11 00:00:00', 381513000, 4992730000, 492952143, 5126774286, 617614367, 5670001667);
INSERT INTO `avg_volume_marketcap` VALUES ('Filecoin', 'FIL', '2021-07-11 00:00:00', 137700000, 4788240000, 264492571, 4781240000, 554447400, 4938128667);
INSERT INTO `avg_volume_marketcap` VALUES ('TRON', 'TRX', '2021-07-11 00:00:00', 576301000, 4430210000, 702388571, 4507440000, 980756667, 4671236000);
INSERT INTO `avg_volume_marketcap` VALUES ('Aave', 'AAVE', '2021-07-11 00:00:00', 294882000, 3911050000, 588189857, 3912704286, 373469300, 3367047000);
INSERT INTO `avg_volume_marketcap` VALUES ('EOS', 'EOS', '2021-07-11 00:00:00', 1240650000, 3889620000, 1156466000, 3736924286, 1134538333, 3960757333);
INSERT INTO `avg_volume_marketcap` VALUES ('Monero', 'XMR', '2021-07-11 00:00:00', 166485000, 3796930000, 168024857, 3822320000, 213714700, 4090857667);
INSERT INTO `avg_volume_marketcap` VALUES ('Terra', 'LUNA', '2021-07-11 00:00:00', 311316000, 3532350000, 296043286, 3038068571, 177210343, 2539235667);
INSERT INTO `avg_volume_marketcap` VALUES ('SHIBA INU', 'SHIB', '2021-07-11 00:00:00', 298920000, 3103830000, 415498429, 3220084286, 559395833, 3055409333);
INSERT INTO `avg_volume_marketcap` VALUES ('Cosmos', 'ATOM', '2021-07-11 00:00:00', 287307000, 3065220000, 293650714, 2899905714, 237198133, 2536936000);
INSERT INTO `avg_volume_marketcap` VALUES ('PancakeSwap', 'CAKE', '2021-07-11 00:00:00', 312665000, 2948010000, 394547857, 2857684286, 255256533, 2705598667);
INSERT INTO `avg_volume_marketcap` VALUES ('FTX Token', 'FTT', '2021-07-11 00:00:00', 39831300, 2923330000, 63548800, 2753812857, 58252793, 2679130000);
INSERT INTO `avg_volume_marketcap` VALUES ('Algorand', 'ALGO', '2021-07-11 00:00:00', 55878500, 2783900000, 76461471, 2782244286, 115202120, 2794220333);
INSERT INTO `avg_volume_marketcap` VALUES ('UNUS SED LEO', 'LEO', '2021-07-11 00:00:00', 2825810, 2763290000, 2896211, 2663897143, 3114218, 2424956000);
INSERT INTO `avg_volume_marketcap` VALUES ('Maker', 'MKR', '2021-07-11 00:00:00', 92776900, 2644280000, 149095729, 2698054286, 125550280, 2587015667);
INSERT INTO `avg_volume_marketcap` VALUES ('Bitcoin SV', 'BSV', '2021-07-11 00:00:00', 444637000, 2597650000, 531791143, 2628432857, 657032367, 2738141667);
INSERT INTO `avg_volume_marketcap` VALUES ('Bitcoin BEP2', 'BTCB', '2021-07-11 00:00:00', 27051900, 2505180000, 38050057, 2470671429, 27354282, 2555245000);
INSERT INTO `avg_volume_marketcap` VALUES ('Klaytn', 'KLAY', '2021-07-11 00:00:00', 65401300, 2455020000, 92552300, 2458641429, 102886607, 2490607000);
INSERT INTO `avg_volume_marketcap` VALUES ('Tezos', 'XTZ', '2021-07-11 00:00:00', 70957200, 2422650000, 76313100, 2390437143, 92148267, 2469971333);
INSERT INTO `avg_volume_marketcap` VALUES ('Neo', 'NEO', '2021-07-11 00:00:00', 278661000, 2413830000, 335560571, 2488462857, 405555867, 2701187667);
INSERT INTO `avg_volume_marketcap` VALUES ('IOTA', 'MIOTA', '2021-07-11 00:00:00', 26321500, 2336080000, 40902886, 2319021429, 45680523, 2461639333);
INSERT INTO `avg_volume_marketcap` VALUES ('Compound', 'COMP', '2021-07-11 00:00:00', 276303000, 2326430000, 438288000, 2382748571, 243585290, 1774074667);
INSERT INTO `avg_volume_marketcap` VALUES ('Amp', 'AMP', '2021-07-11 00:00:00', 9905750, 2322540000, 17822064, 2338462857, 68154058, 2761623333);
INSERT INTO `avg_volume_marketcap` VALUES ('Avalanche', 'AVAX', '2021-07-11 00:00:00', 31468100, 2140340000, 67022600, 2157128571, 65805803, 2144846000);
INSERT INTO `avg_volume_marketcap` VALUES ('The Graph', 'GRT', '2021-07-11 00:00:00', 111043000, 2060060000, 152597586, 2021730000, 111179653, 1569442300);
INSERT INTO `avg_volume_marketcap` VALUES ('TerraUSD', 'UST', '2021-07-11 00:00:00', 20393700, 1930960000, 31812529, 1929515714, 31502120, 1913800000);
INSERT INTO `avg_volume_marketcap` VALUES ('Theta Fuel', 'TFUEL', '2021-07-11 00:00:00', 97538600, 1832970000, 142953471, 1884477143, 159354040, 2350851333);
INSERT INTO `avg_volume_marketcap` VALUES ('Kusama', 'KSM', '2021-07-11 00:00:00', 92602700, 1783050000, 174010671, 1819948571, 259201790, 2151285000);
INSERT INTO `avg_volume_marketcap` VALUES ('Decred', 'DCR', '2021-07-11 00:00:00', 87896200, 1753310000, 81726143, 1749330000, 49285110, 1683001667);
INSERT INTO `avg_volume_marketcap` VALUES ('Elrond', 'EGLD', '2021-07-11 00:00:00', 26271800, 1700520000, 65375471, 1709662857, 51438920, 1460810333);
INSERT INTO `avg_volume_marketcap` VALUES ('BitTorrent', 'BTT', '2021-07-11 00:00:00', 134326000, 1666780000, 178040429, 1700421429, 232519800, 1823918333);
INSERT INTO `avg_volume_marketcap` VALUES ('Stacks', 'STX', '2021-07-11 00:00:00', 232837000, 1628210000, 144308429, 1295816429, 43256283, 988776300);
INSERT INTO `avg_volume_marketcap` VALUES ('Huobi Token', 'HT', '2021-07-11 00:00:00', 117055000, 1609790000, 125558429, 1691982857, 176993237, 1896671333);
INSERT INTO `avg_volume_marketcap` VALUES ('Hedera Hashgraph', 'HBAR', '2021-07-11 00:00:00', 72491100, 1535410000, 150772871, 1589630000, 173569927, 1654243667);
INSERT INTO `avg_volume_marketcap` VALUES ('Chiliz', 'CHZ', '2021-07-11 00:00:00', 250818000, 1520020000, 369153571, 1472790000, 355589967, 1517029667);
INSERT INTO `avg_volume_marketcap` VALUES ('Waves', 'WAVES', '2021-07-11 00:00:00', 108434000, 1511520000, 107691729, 1614344286, 148799330, 1609622000);
INSERT INTO `avg_volume_marketcap` VALUES ('TrueUSD', 'TUSD', '2021-07-11 00:00:00', 63304200, 1509550000, 81590786, 1520291429, 84743960, 1466455000);
INSERT INTO `avg_volume_marketcap` VALUES ('Celsius', 'CEL', '2021-07-11 00:00:00', 7161190, 1481700000, 11024320, 1561022857, 18912391, 1498668667);
INSERT INTO `avg_volume_marketcap` VALUES ('THORChain', 'RUNE', '2021-07-11 00:00:00', 24911400, 1471600000, 77764757, 1506987143, 104271710, 1572692667);
INSERT INTO `avg_volume_marketcap` VALUES ('Synthetix', 'SNX', '2021-07-11 00:00:00', 239594000, 1423360000, 266705571, 1265750000, 110597667, 967039033);
INSERT INTO `avg_volume_marketcap` VALUES ('Zcash', 'ZEC', '2021-07-11 00:00:00', 190071000, 1348910000, 249888714, 1366335714, 325129533, 1442064000);
INSERT INTO `avg_volume_marketcap` VALUES ('Dash', 'DASH', '2021-07-11 00:00:00', 353031000, 1312690000, 417369286, 1334765714, 397089100, 1438621667);
INSERT INTO `avg_volume_marketcap` VALUES ('Decentraland', 'MANA', '2021-07-11 00:00:00', 200863000, 1254400000, 318849071, 1136532571, 113076300, 970839833);
INSERT INTO `avg_volume_marketcap` VALUES ('yearn.finance', 'YFI', '2021-07-11 00:00:00', 144179000, 1236720000, 224132000, 1242114286, 221902700, 1226884333);
INSERT INTO `avg_volume_marketcap` VALUES ('Axie Infinity', 'AXS', '2021-07-11 00:00:00', 951070000, 1154670000, 1086181300, 850547286, 284463723, 411207300);
INSERT INTO `avg_volume_marketcap` VALUES ('Helium', 'HNT', '2021-07-11 00:00:00', 8118760, 1150690000, 12108723, 1137940000, 12219838, 1100951433);
INSERT INTO `avg_volume_marketcap` VALUES ('Enjin Coin', 'ENJ', '2021-07-11 00:00:00', 201626000, 1146120000, 238880757, 1053230143, 144792710, 984073033);
INSERT INTO `avg_volume_marketcap` VALUES ('XinFin Network', 'XDC', '2021-07-11 00:00:00', 3042220, 1139700000, 5684600, 1175920000, 7252809, 933191267);
INSERT INTO `avg_volume_marketcap` VALUES ('KuCoin Token', 'KCS', '2021-07-11 00:00:00', 28116500, 1116830000, 70558343, 1014800571, 26072287, 702043600);
INSERT INTO `avg_volume_marketcap` VALUES ('NEM', 'XEM', '2021-07-11 00:00:00', 43330000, 1103290000, 56280743, 1139778571, 60577640, 1196861767);
INSERT INTO `avg_volume_marketcap` VALUES ('SushiSwap', 'SUSHI', '2021-07-11 00:00:00', 151355000, 1036340000, 268032429, 1059491429, 242659567, 998857233);
INSERT INTO `avg_volume_marketcap` VALUES ('Holo', 'HOT', '2021-07-11 00:00:00', 52246100, 996498000, 70299143, 1011839714, 93868477, 1113283900);
INSERT INTO `avg_volume_marketcap` VALUES ('Quant', 'QNT', '2021-07-11 00:00:00', 6807060, 957701000, 9486197, 947039000, 15391411, 877256600);
INSERT INTO `avg_volume_marketcap` VALUES ('Telcoin', 'TEL', '2021-07-11 00:00:00', 23265800, 942413000, 15186920, 1068345143, 21212975, 1315327867);
INSERT INTO `avg_volume_marketcap` VALUES ('Paxos Standard', 'PAX', '2021-07-11 00:00:00', 73283400, 921450000, 91712671, 927326143, 69283797, 871324767);
INSERT INTO `avg_volume_marketcap` VALUES ('Nexo', 'NEXO', '2021-07-11 00:00:00', 6351000, 913995000, 7762570, 904364143, 9684854, 886727033);
INSERT INTO `avg_volume_marketcap` VALUES ('NEAR Protocol', 'NEAR', '2021-07-11 00:00:00', 31237200, 894611000, 31206186, 894728143, 43590137, 979272167);
INSERT INTO `avg_volume_marketcap` VALUES ('Mdex', 'MDX', '2021-07-11 00:00:00', 49412900, 858588000, 56222286, 866488286, 70571027, 862749400);
INSERT INTO `avg_volume_marketcap` VALUES ('Zilliqa', 'ZIL', '2021-07-11 00:00:00', 41715600, 846868000, 60674600, 881717714, 77681823, 970914833);
INSERT INTO `avg_volume_marketcap` VALUES ('Harmony', 'ONE', '2021-07-11 00:00:00', 23470000, 846804000, 66208686, 817221857, 40278520, 726959533);
INSERT INTO `avg_volume_marketcap` VALUES ('Basic Attention Token', 'BAT', '2021-07-11 00:00:00', 127000000, 842408000, 170279286, 863884286, 166717433, 879343133);
INSERT INTO `avg_volume_marketcap` VALUES ('Flow', 'FLOW', '2021-07-11 00:00:00', 557879000, 826507000, 356657771, 650000286, 125003230, 474307067);
INSERT INTO `avg_volume_marketcap` VALUES ('Bitcoin Gold', 'BTG', '2021-07-11 00:00:00', 23471200, 785524000, 38691214, 806773286, 32908657, 833306333);
INSERT INTO `avg_volume_marketcap` VALUES ('Celo', 'CELO', '2021-07-11 00:00:00', 20111200, 768049000, 30635171, 797833286, 63141290, 731940400);
INSERT INTO `avg_volume_marketcap` VALUES ('Bancor', 'BNT', '2021-07-11 00:00:00', 24090000, 745880000, 41895229, 751845571, 55518343, 734123767);
INSERT INTO `avg_volume_marketcap` VALUES ('Horizen', 'ZEN', '2021-07-11 00:00:00', 29825200, 684569000, 38581757, 701167571, 50534780, 768165167);
INSERT INTO `avg_volume_marketcap` VALUES ('0x', 'ZRX', '2021-07-11 00:00:00', 51320000, 671769000, 93690286, 657374143, 66379830, 633439000);
INSERT INTO `avg_volume_marketcap` VALUES ('Curve DAO Token', 'CRV', '2021-07-11 00:00:00', 83480800, 668494000, 117296314, 691228857, 129295193, 668427900);
INSERT INTO `avg_volume_marketcap` VALUES ('Qtum', 'QTUM', '2021-07-11 00:00:00', 228372000, 659899000, 264526143, 672915286, 263409800, 706249800);
INSERT INTO `avg_volume_marketcap` VALUES ('Nano', 'NANO', '2021-07-11 00:00:00', 46698300, 636815000, 23412514, 603747571, 32120507, 687820067);
INSERT INTO `avg_volume_marketcap` VALUES ('Siacoin', 'SC', '2021-07-11 00:00:00', 26649500, 628554000, 52828871, 648568571, 47196267, 632851600);
INSERT INTO `avg_volume_marketcap` VALUES ('SwissBorg', 'CHSB', '2021-07-11 00:00:00', 797081, 619381000, 1723052, 623655714, 2240551, 594718833);
INSERT INTO `avg_volume_marketcap` VALUES ('Ontology', 'ONT', '2021-07-11 00:00:00', 75120900, 615373000, 103600971, 625524143, 113279543, 648409867);
INSERT INTO `avg_volume_marketcap` VALUES ('ICON', 'ICX', '2021-07-11 00:00:00', 42452800, 607666000, 78641200, 605255000, 52178167, 560476967);
INSERT INTO `avg_volume_marketcap` VALUES ('DigiByte', 'DGB', '2021-07-11 00:00:00', 16033900, 601211000, 20520314, 614092429, 28190923, 672190200);
INSERT INTO `avg_volume_marketcap` VALUES ('OKB', 'OKB', '2021-07-11 00:00:00', 110044000, 591926000, 186210429, 606414571, 317504067, 669819333);
INSERT INTO `avg_volume_marketcap` VALUES ('Fantom', 'FTM', '2021-07-11 00:00:00', 21005000, 588390000, 33235957, 606188429, 52923130, 634507433);
INSERT INTO `avg_volume_marketcap` VALUES ('Arweave', 'AR', '2021-07-11 00:00:00', 8784130, 379543000, 14168586, 370526571, 19048683, 417822733);
INSERT INTO `avg_volume_marketcap` VALUES ('QuadrantProtocol', 'EQUAD', '2021-07-11 00:00:00', 101151, 1815100, 99417, 1845904, 99168, 1888382);

SET FOREIGN_KEY_CHECKS = 1;
