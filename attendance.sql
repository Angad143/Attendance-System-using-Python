-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2023 at 12:11 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `a_java`
--

CREATE TABLE `a_java` (
  `date` varchar(50) NOT NULL,
  `sEnroll` varchar(50) NOT NULL,
  `sName` varchar(50) NOT NULL,
  `sRoll` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `a_python`
--

CREATE TABLE `a_python` (
  `date` varchar(50) NOT NULL,
  `sEnroll` varchar(50) NOT NULL,
  `sName` varchar(50) NOT NULL,
  `sRoll` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `btech_a`
--

CREATE TABLE `btech_a` (
  `sEnroll` varchar(50) NOT NULL,
  `sName` varchar(50) NOT NULL,
  `sRoll` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `btech_a`
--

INSERT INTO `btech_a` (`sEnroll`, `sName`, `sRoll`) VALUES
('21SOECE11y', 'POR', '56');

-- --------------------------------------------------------

--
-- Table structure for table `mtech_o`
--

CREATE TABLE `mtech_o` (
  `sEnroll` varchar(50) NOT NULL,
  `sName` varchar(50) NOT NULL,
  `sRoll` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `o_java`
--

CREATE TABLE `o_java` (
  `date` varchar(50) NOT NULL,
  `sEnroll` varchar(50) NOT NULL,
  `sName` varchar(50) NOT NULL,
  `sRoll` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `o_python`
--

CREATE TABLE `o_python` (
  `date` varchar(50) NOT NULL,
  `sEnroll` varchar(50) NOT NULL,
  `sName` varchar(50) NOT NULL,
  `sRoll` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
