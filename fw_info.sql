-- phpMyAdmin SQL Dump
-- version 4.6.0
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 29, 2016 at 02:25 PM
-- Server version: 5.7.11
-- PHP Version: 5.5.36

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `programming`
--

-- --------------------------------------------------------

--
-- Table structure for table `fw_info`
--

DROP TABLE IF EXISTS `fw_info`;
CREATE TABLE `fw_info` (
  `id` bigint(20) NOT NULL,
  `customer` varchar(30) NOT NULL,
  `model` varchar(30) NOT NULL,
  `pn` varchar(30) NOT NULL,
  `chip` varchar(10) NOT NULL,
  `mcu_model` varchar(30) NOT NULL,
  `fw_pathname` varchar(300) NOT NULL,
  `fw_version` varchar(30) NOT NULL,
  `fw_checksum` varchar(100) NOT NULL,
  `dl_port` varchar(30) NOT NULL,
  `dl_speed` varchar(30) NOT NULL,
  `flash_start_addr` varchar(30) NOT NULL,
  `flash_end_addr` varchar(30) NOT NULL,
  `sn_enable` varchar(10) NOT NULL,
  `sn_addr` varchar(30) NOT NULL,
  `sn_length` int(11) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
