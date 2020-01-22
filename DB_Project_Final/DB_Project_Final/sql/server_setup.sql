-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jun 30, 2019 at 11:16 AM
-- Server version: 5.7.25
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `Ticket_Booking`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline`
--

CREATE TABLE `airline` (
  `airline_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airline`
--

INSERT INTO `airline` (`airline_name`) VALUES
('Air China');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff`
--

CREATE TABLE `airline_staff` (
  `username` varchar(20) NOT NULL,
  `password` varchar(2000) DEFAULT NULL,
  `airline_name` varchar(20) DEFAULT NULL,
  `first_name` varchar(10) DEFAULT NULL,
  `last_name` varchar(10) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airline_staff`
--

INSERT INTO `airline_staff` (`username`, `password`, `airline_name`, `first_name`, `last_name`, `date_of_birth`) VALUES
('admin', 'e2fc714c4727ee9395f324cd2e7f331f', 'Air China', 'Roe', 'Zhang', '1978-05-25');

-- --------------------------------------------------------

--
-- Table structure for table `airplane`
--

CREATE TABLE `airplane` (
  `airline_name` varchar(20) NOT NULL,
  `planeID` varchar(8) NOT NULL,
  `seats` decimal(3,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airplane`
--

INSERT INTO `airplane` (`airline_name`, `planeID`, `seats`) VALUES
('Air China', '1', '4'),
('Air China', '2', '4'),
('Air China', '3', '50');

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `name` varchar(20) NOT NULL,
  `city` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`name`, `city`) VALUES
('BEI', 'Beijing'),
('BOS', 'Boston'),
('HKA', 'Hong Kong'),
('JFK', 'NYC'),
('LAX', 'Los Angeles'),
('PVG', 'Shanghai'),
('SFO', 'San Francisco'),
('SHEN', 'Shenzhen');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `email` varchar(40) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `password` varchar(2000) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `building_no` varchar(20) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `passport_no` varchar(15) DEFAULT NULL,
  `passport_exp` date DEFAULT NULL,
  `passport_country` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`email`, `name`, `password`, `date_of_birth`, `state`, `city`, `street`, `building_no`, `phone_no`, `passport_no`, `passport_exp`, `passport_country`) VALUES
('testcustomer@nyu.edu', 'Test Customer 1,', '81dc9bdb52d04dc20036dbd8313ed055', '1999-12-19', 'Shanghai', 'Pudong', 'Century Avenue', '15555', '123-4321-4321', '54321', '2025-12-24', 'China'),
('user1@nyu.edu', 'User 1,', '81dc9bdb52d04dc20036dbd8313ed055', '1999-11-19', 'Shanghai', 'Pudong', 'Century Avenue', '15555', '123-4322-4322', '54322', '2025-12-25', 'China'),
('user2@nyu.edu', 'User 2,', '81dc9bdb52d04dc20036dbd8313ed055', '1999-10-19', 'Shanghai', 'Pudong', 'Century Avenue', '1702', '123-4323-4323', '54323', '2025-10-24', 'China'),
('user3@nyu.edu', 'User 3,', '81dc9bdb52d04dc20036dbd8313ed055', '1999-09-19', 'Shanghai', 'Pudong', 'Century Avenue', '1890', '123-4324-4324', '54324', '2025-09-24', 'China');

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `planeID` varchar(8) DEFAULT NULL,
  `airline_name` varchar(20) NOT NULL,
  `flight_no` varchar(8) NOT NULL,
  `departure_date_time` datetime NOT NULL,
  `arrival_date_time` datetime DEFAULT NULL,
  `departs_from` varchar(20) DEFAULT NULL,
  `arrives_from` varchar(20) DEFAULT NULL,
  `base_price` decimal(7,2) DEFAULT NULL,
  `flight_status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`planeID`, `airline_name`, `flight_no`, `departure_date_time`, `arrival_date_time`, `departs_from`, `arrives_from`, `base_price`, `flight_status`) VALUES
('3', 'Air China', '102', '2019-04-12 13:25:25', '2019-04-12 16:50:25', 'SFO', 'LAX', '300.00', 'ontime'),
('3', 'Air China', '104', '2019-05-12 13:25:25', '2019-05-12 16:50:25', 'PVG', 'BEI', '300.00', 'ontime'),
('3', 'Air China', '106', '2019-03-12 13:25:25', '2019-03-12 16:50:25', 'SFO', 'LAX', '350.00', 'delayed'),
('3', 'Air China', '134', '2019-01-12 13:25:25', '2019-01-12 16:50:25', 'JFK', 'BOS', '300.00', 'delayed'),
('2', 'Air China', '206', '2019-07-12 13:25:25', '2019-07-12 16:50:25', 'SFO', 'LAX', '500.00', 'ontime'),
('2', 'Air China', '207', '2019-08-12 13:25:25', '2019-08-12 16:50:25', 'LAX', 'SFO', '300.00', 'ontime'),
('1', 'Air China', '296', '2019-07-01 13:25:25', '2019-07-01 16:50:25', 'PVG', 'SFO', '2000.00', 'ontime'),
('1', 'Air China', '715', '2019-04-28 10:25:25', '2019-04-28 13:50:25', 'PVG', 'BEI', '500.00', 'delayed'),
('3', 'Air China', '839', '2018-10-12 13:25:25', '2018-10-12 16:50:25', 'SHEN', 'BEI', '300.00', 'ontime');

-- --------------------------------------------------------

--
-- Stand-in structure for view `flight_avail`
-- (See below for the actual view)
--
CREATE TABLE `flight_avail` (
`flight_no` varchar(8)
,`airline_name` varchar(20)
,`departure_date_time` datetime
,`sold` bigint(21)
,`seats` decimal(3,0)
,`percentage_full` decimal(27,4)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `monthly_revenue`
-- (See below for the actual view)
--
CREATE TABLE `monthly_revenue` (
`airline_name` varchar(20)
,`month` varchar(7)
,`revenue` decimal(29,2)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `monthly_spend`
-- (See below for the actual view)
--
CREATE TABLE `monthly_spend` (
`email` varchar(40)
,`month` varchar(7)
,`purchase_date_time` datetime
,`spending` decimal(29,2)
);

-- --------------------------------------------------------

--
-- Table structure for table `phone_number`
--

CREATE TABLE `phone_number` (
  `username` varchar(20) DEFAULT NULL,
  `phone_number` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Stand-in structure for view `pricing`
-- (See below for the actual view)
--
CREATE TABLE `pricing` (
`flight_no` varchar(8)
,`base_price` decimal(7,2)
,`real_price` decimal(9,3)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `pricing2`
-- (See below for the actual view)
--
CREATE TABLE `pricing2` (
`flight_no` varchar(8)
,`base_price` decimal(7,2)
,`real_price` decimal(9,3)
);

-- --------------------------------------------------------

--
-- Table structure for table `rates`
--

CREATE TABLE `rates` (
  `email` varchar(40) NOT NULL,
  `airline_name` varchar(20) NOT NULL,
  `flight_no` varchar(8) NOT NULL,
  `departure_date_time` datetime NOT NULL,
  `rating` decimal(1,0) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rates`
--

INSERT INTO `rates` (`email`, `airline_name`, `flight_no`, `departure_date_time`, `rating`, `comment`) VALUES
('testcustomer@nyu.edu', 'Air China', '102', '2019-04-12 13:25:25', '4', 'Very Comfortable'),
('testcustomer@nyu.edu', 'Air China', '104', '2019-05-12 13:25:25', '1', 'Customer Care services are not good'),
('user1@nyu.edu', 'Air China', '102', '2019-04-12 13:25:25', '5', 'Relaxing, check-in and onboarding very professional'),
('user1@nyu.edu', 'Air China', '104', '2019-05-12 13:25:25', '5', 'Comfortable journey and Professional'),
('user2@nyu.edu', 'Air China', '102', '2019-04-12 13:25:25', '3', 'Satisfied and will use the same flight again');

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `ticketID` varchar(30) NOT NULL,
  `email` varchar(40) DEFAULT NULL,
  `airline_name` varchar(20) DEFAULT NULL,
  `flight_no` varchar(8) DEFAULT NULL,
  `departure_date_time` datetime DEFAULT NULL,
  `sold_price` decimal(7,2) DEFAULT NULL,
  `purchase_date_time` datetime DEFAULT NULL,
  `card_type` varchar(10) DEFAULT NULL,
  `card_no` varchar(20) DEFAULT NULL,
  `name_on_card` varchar(50) DEFAULT NULL,
  `exp_date` date DEFAULT NULL,
  `sec_code` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`ticketID`, `email`, `airline_name`, `flight_no`, `departure_date_time`, `sold_price`, `purchase_date_time`, `card_type`, `card_no`, `name_on_card`, `exp_date`, `sec_code`) VALUES
('1', 'testcustomer@nyu.edu', 'Air China', '102', '2019-04-12 13:25:25', '300.00', '2019-03-12 11:55:55', 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2023-03-01', '101'),
('11', 'user3@nyu.edu', 'Air China', '134', '2019-01-12 13:25:25', '300.00', '2018-10-23 11:55:55', 'credit', '1111-2222-3333-5555', 'User 3', '2023-03-01', '101'),
('12', 'testcustomer@nyu.edu', 'Air China', '715', '2019-04-28 10:25:25', '500.00', '2019-04-05 11:55:55', 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2023-03-01', '101'),
('14', 'user3@nyu.edu', 'Air China', '206', '2019-07-12 13:25:25', '400.00', '2019-05-12 11:55:55', 'credit', '1111-2222-3333-5555', 'User 3', '2023-03-01', '101'),
('15', 'user1@nyu.edu', 'Air China', '206', '2019-07-12 13:25:25', '400.00', '2019-05-13 11:55:55', 'credit', '1111-2222-3333-5555', 'User 1', '2023-03-01', '101'),
('16', 'user2@nyu.edu', 'Air China', '206', '2019-07-12 13:25:25', '400.00', '2019-04-19 11:55:55', 'credit', '1111-2222-3333-5555', 'User 2', '2023-03-01', '101'),
('17', 'user1@nyu.edu', 'Air China', '207', '2019-08-12 13:25:25', '300.00', '2019-03-11 11:55:55', 'credit', '1111-2222-3333-5555', 'User 1', '2023-03-01', '101'),
('18', 'testcustomer@nyu.edu', 'Air China', '207', '2019-08-12 13:25:25', '300.00', '2019-04-25 11:55:55', 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2023-03-01', '101'),
('19', 'user1@nyu.edu', 'Air China', '296', '2019-07-01 13:25:25', '3000.00', '2019-05-04 11:55:55', 'credit', '1111-2222-3333-5555', 'User 1', '2023-03-01', '101'),
('2', 'user1@nyu.edu', 'Air China', '102', '2019-04-12 13:25:25', '300.00', '2019-03-11 11:55:55', 'credit', '1111-2222-3333-5555', 'User 1', '2023-03-01', '101'),
('20', 'testcustomer@nyu.edu', 'Air China', '296', '2019-07-01 13:25:25', '3000.00', '2019-02-12 11:55:55', 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2023-03-01', '101'),
('3', 'user2@nyu.edu', 'Air China', '102', '2019-04-12 13:25:25', '300.00', '2019-04-11 11:55:55', 'credit', '1111-2222-3333-5555', 'User 2,', '2023-03-01', '101'),
('4', 'user1@nyu.edu', 'Air China', '104', '2019-05-12 13:25:25', '300.00', '2019-03-21 11:55:55', 'credit', '1111-2222-3333-5555', 'User 1', '2023-03-01', '101'),
('5', 'testcustomer@nyu.edu', 'Air China', '104', '2019-05-12 13:25:25', '300.00', '2019-04-28 11:55:55', 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2023-03-01', '101'),
('6', 'testcustomer@nyu.edu', 'Air China', '106', '2019-03-12 13:25:25', '350.00', '2019-03-05 11:55:55', 'credit', '1111-2222-3333-4444', 'Test Customer 1', '2023-03-01', '101'),
('7', 'user3@nyu.edu', 'Air China', '106', '2019-03-12 13:25:25', '350.00', '2019-02-03 11:55:55', 'credit', '1111-2222-3333-5555', 'User 3', '2023-03-01', '101'),
('8', 'user3@nyu.edu', 'Air China', '839', '2018-10-12 13:25:25', '300.00', '2018-10-03 11:55:55', 'credit', '1111-2222-3333-5555', 'User 3', '2023-03-01', '101'),
('9', 'user3@nyu.edu', 'Air China', '102', '2019-04-12 13:25:25', '360.00', '2019-02-03 11:55:55', 'credit', '1111-2222-3333-5555', 'User 3', '2023-03-01', '101');

-- --------------------------------------------------------

--
-- Stand-in structure for view `topdest_last_three_months`
-- (See below for the actual view)
--
CREATE TABLE `topdest_last_three_months` (
`city` varchar(20)
,`count` bigint(21)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `topdest_last_year`
-- (See below for the actual view)
--
CREATE TABLE `topdest_last_year` (
`city` varchar(20)
,`count` bigint(21)
);

-- --------------------------------------------------------

--
-- Structure for view `flight_avail`
--
DROP TABLE IF EXISTS `flight_avail`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `flight_avail`  AS  select `flight`.`flight_no` AS `flight_no`,`flight`.`airline_name` AS `airline_name`,`flight`.`departure_date_time` AS `departure_date_time`,count(`ticket`.`ticketID`) AS `sold`,`airplane`.`seats` AS `seats`,((count(`ticket`.`ticketID`) / `airplane`.`seats`) * 100) AS `percentage_full` from ((`flight` join `ticket`) join `airplane`) where ((`ticket`.`flight_no` = `flight`.`flight_no`) and (`airplane`.`planeID` = `flight`.`planeID`) and (`airplane`.`airline_name` = `flight`.`airline_name`)) group by `flight`.`flight_no`,`flight`.`airline_name`,`flight`.`departure_date_time` union select `flight`.`flight_no` AS `flight_no`,`flight`.`airline_name` AS `airline_name`,`flight`.`departure_date_time` AS `departure_date_time`,0 AS `sold`,`airplane`.`seats` AS `seats`,0 AS `percentage_full` from (`flight` join `airplane`) where ((not(`flight`.`flight_no` in (select `flight`.`flight_no` from `flight` where `flight`.`flight_no` in (select `ticket`.`flight_no` from `ticket`)))) and (`airplane`.`planeID` = `flight`.`planeID`) and (`airplane`.`airline_name` = `flight`.`airline_name`)) ;

-- --------------------------------------------------------

--
-- Structure for view `monthly_revenue`
--
DROP TABLE IF EXISTS `monthly_revenue`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `monthly_revenue`  AS  select `ticket`.`airline_name` AS `airline_name`,date_format(`ticket`.`purchase_date_time`,'%Y-%m') AS `month`,sum(`ticket`.`sold_price`) AS `revenue` from `ticket` group by `ticket`.`airline_name`,`month` ;

-- --------------------------------------------------------

--
-- Structure for view `monthly_spend`
--
DROP TABLE IF EXISTS `monthly_spend`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `monthly_spend`  AS  select `ticket`.`email` AS `email`,date_format(`ticket`.`purchase_date_time`,'%Y-%m') AS `month`,`ticket`.`purchase_date_time` AS `purchase_date_time`,sum(`ticket`.`sold_price`) AS `spending` from `ticket` group by `ticket`.`email`,`month` ;

-- --------------------------------------------------------

--
-- Structure for view `pricing`
--
DROP TABLE IF EXISTS `pricing`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pricing`  AS  select `flight`.`flight_no` AS `flight_no`,`flight`.`base_price` AS `base_price`,(`flight`.`base_price` * 1.2) AS `real_price` from (`flight` join `flight_avail` on((`flight`.`flight_no` = `flight_avail`.`flight_no`))) where (`flight_avail`.`percentage_full` >= 70) union select `flight`.`flight_no` AS `flight_no`,`flight`.`base_price` AS `base_price`,`flight`.`base_price` AS `real_price` from (`flight` join `flight_avail` on((`flight`.`flight_no` = `flight_avail`.`flight_no`))) where (`flight_avail`.`percentage_full` < 70) ;

-- --------------------------------------------------------

--
-- Structure for view `pricing2`
--
DROP TABLE IF EXISTS `pricing2`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pricing2`  AS  select `flight`.`flight_no` AS `flight_no`,`flight`.`base_price` AS `base_price`,(`flight`.`base_price` * 1.2) AS `real_price` from (`flight` join `flight_avail` on((`flight`.`flight_no` = `flight_avail`.`flight_no`))) where (`flight_avail`.`percentage_full` > 0) union select `flight`.`flight_no` AS `flight_no`,`flight`.`base_price` AS `base_price`,`flight`.`base_price` AS `real_price` from (`flight` join `flight_avail` on((`flight`.`flight_no` = `flight_avail`.`flight_no`))) where (`flight_avail`.`percentage_full` <= 0) ;

-- --------------------------------------------------------

--
-- Structure for view `topdest_last_three_months`
--
DROP TABLE IF EXISTS `topdest_last_three_months`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `topdest_last_three_months`  AS  select `airport`.`city` AS `city`,count(`airport`.`city`) AS `count` from (`flight` join `airport`) where ((`flight`.`arrives_from` = `airport`.`name`) and (`flight`.`departure_date_time` between (now() - interval 90 day) and now())) group by `airport`.`city` ;

-- --------------------------------------------------------

--
-- Structure for view `topdest_last_year`
--
DROP TABLE IF EXISTS `topdest_last_year`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `topdest_last_year`  AS  select `airport`.`city` AS `city`,count(`airport`.`city`) AS `count` from (`flight` join `airport`) where ((`flight`.`arrives_from` = `airport`.`name`) and (`flight`.`departure_date_time` between (now() - interval 365 day) and now())) group by `airport`.`city` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`airline_name`);

--
-- Indexes for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD PRIMARY KEY (`username`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`planeID`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`flight_no`,`departure_date_time`,`airline_name`),
  ADD KEY `planeID` (`planeID`),
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `departs_from` (`departs_from`),
  ADD KEY `arrives_from` (`arrives_from`);

--
-- Indexes for table `phone_number`
--
ALTER TABLE `phone_number`
  ADD PRIMARY KEY (`phone_number`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `rates`
--
ALTER TABLE `rates`
  ADD PRIMARY KEY (`email`,`airline_name`,`flight_no`,`departure_date_time`),
  ADD KEY `airline_name` (`airline_name`,`flight_no`,`departure_date_time`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`ticketID`),
  ADD KEY `email` (`email`),
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `flight_no` (`flight_no`,`departure_date_time`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD CONSTRAINT `airline_staff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON DELETE SET NULL;

--
-- Constraints for table `airplane`
--
ALTER TABLE `airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON DELETE CASCADE;

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`planeID`) REFERENCES `airplane` (`planeID`) ON DELETE SET NULL,
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON DELETE CASCADE,
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`departs_from`) REFERENCES `airport` (`name`) ON DELETE SET NULL,
  ADD CONSTRAINT `flight_ibfk_4` FOREIGN KEY (`arrives_from`) REFERENCES `airport` (`name`) ON DELETE SET NULL;

--
-- Constraints for table `phone_number`
--
ALTER TABLE `phone_number`
  ADD CONSTRAINT `phone_number_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`) ON DELETE SET NULL;

--
-- Constraints for table `rates`
--
ALTER TABLE `rates`
  ADD CONSTRAINT `rates_ibfk_1` FOREIGN KEY (`email`) REFERENCES `customer` (`email`) ON DELETE CASCADE,
  ADD CONSTRAINT `rates_ibfk_2` FOREIGN KEY (`airline_name`,`flight_no`,`departure_date_time`) REFERENCES `flight` (`airline_name`, `flight_no`, `departure_date_time`) ON DELETE CASCADE;

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`email`) REFERENCES `customer` (`email`) ON DELETE SET NULL,
  ADD CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`airline_name`) ON DELETE SET NULL,
  ADD CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`flight_no`,`departure_date_time`) REFERENCES `flight` (`flight_no`, `departure_date_time`) ON DELETE SET NULL;
