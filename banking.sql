-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 11, 2018 at 10:40 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `banking`
--

-- --------------------------------------------------------

--
-- Table structure for table `balance`
--

CREATE TABLE `balance` (
  `id` bigint(20) NOT NULL,
  `accno` bigint(20) NOT NULL,
  `balance` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `balance`
--

INSERT INTO `balance` (`id`, `accno`, `balance`) VALUES
(1, 12345, 10000);

-- --------------------------------------------------------

--
-- Table structure for table `passbook`
--

CREATE TABLE `passbook` (
  `id` bigint(20) NOT NULL,
  `accno` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `narration` varchar(100) NOT NULL,
  `dorc` int(10) NOT NULL,
  `Balance` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `passbook`
--

INSERT INTO `passbook` (`id`, `accno`, `date`, `narration`, `dorc`, `Balance`) VALUES
(1, 123456, '2018-11-07', 'Credit', 1400, 10000);

-- --------------------------------------------------------

--
-- Table structure for table `reg`
--

CREATE TABLE `reg` (
  `No` bigint(20) NOT NULL,
  `accno` bigint(30) NOT NULL,
  `username` varchar(20) NOT NULL,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `zip` int(6) NOT NULL,
  `country` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `aadharno` bigint(12) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobno` int(10) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reg`
--

INSERT INTO `reg` (`No`, `accno`, `username`, `firstname`, `lastname`, `address`, `city`, `state`, `zip`, `country`, `dob`, `aadharno`, `email`, `mobno`, `pass`) VALUES
(1, 32465, 'knkdfkg', 'mrsbhjs', 'ghjgjh', 'kljhghghhkj', 'bjjbhjk', 'nbnb', 0, 'kbhkj', '0000-00-00', 87542, 'klsf@kd.csdf', 85285258, 'lkjbvvb'),
(2, 32465, 'knkdfkg', 'mrsbhjs', 'ghjgjh', 'kljhghghhkj', 'bjjbhjk', 'nbnb', 0, 'kbhkj', '0000-00-00', 87542, 'klsf@kd.csdf', 85285258, 'lkjbvvb'),
(3, 12354, 'ravi', 'Mr.Ravi', 'Patel', 'Ahmedabad', 'Ahmedabad', 'gujarat', 382350, 'India', '0000-00-00', 123456789012, 'impatelravi@gmail.com', 2147483647, '123'),
(4, 12345689, 'ravi21', 'mrRavi', 'Patel', 'Ahmedabad', 'Ahmedabad', 'Gujarat', 0, 'India', '1998-01-21', 1123456789, 'impatelravi@gmai.com', 2147483647, '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `balance`
--
ALTER TABLE `balance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `passbook`
--
ALTER TABLE `passbook`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reg`
--
ALTER TABLE `reg`
  ADD PRIMARY KEY (`No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `balance`
--
ALTER TABLE `balance`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `passbook`
--
ALTER TABLE `passbook`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `reg`
--
ALTER TABLE `reg`
  MODIFY `No` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
