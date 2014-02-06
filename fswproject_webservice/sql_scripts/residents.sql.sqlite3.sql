begin;
-- phpMyAdmin SQL Dump
-- version 3.4.3.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 01, 2013 at 07:02 PM
-- Server version: 5.6.14
-- PHP Version: 5.3.26



/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `residents`
--

-- --------------------------------------------------------

-- --------------------------------------------------------

--
-- Table structure for table `resident`
--

CREATE TABLE IF NOT EXISTS `resident` (
  `resident_id` integer NOT NULL primary key autoincrement,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50)   NULL,
  `last_name` varchar(50) NOT NULL,
  `address1` varchar(95) NOT NULL,
  `address2` varchar(95)   NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zip_code` varchar(16) NOT NULL,
  `home_phone` varchar(30) NOT NULL,
  `cell_phone` varchar(30)   NULL,
  `date_of_birth` date NOT NULL
)           ;

--
-- Dumping data for table `resident`
--

INSERT INTO `resident` (`resident_id`, `first_name`, `middle_name`, `last_name`, `address1`, `address2`, `city`, `state`, `zip_code`, `home_phone`, `cell_phone`, `date_of_birth`) VALUES
(1, 'Jaime', NULL, 'Emiaj', '100 Maple Place', 'Apt #1', 'Ossining', 'NY', '10562', '(123) 456-7890', '(098) 765-4321', '1954-01-14'),
(2, 'John', NULL, 'Doe', '100 Maple Place', 'Apt #2', 'Ossining', 'NY', '10562', '(123) 456-7890', '(098) 765-4321', '1953-04-23'),
(3, 'Matthew ', NULL, 'Gibson', '100 Maple Place', 'Apt #3', 'Ossining', 'NY', '10562', '(123) 456-7890', '(098) 765-4321', '1948-10-01'),
(4, 'Teodulo', NULL, 'Quezada', '18665 Juniper St', NULL, 'Hesperia', 'CA', '92345', '(760) 244-2448', '(760) 261-2886', '1963-02-17');


--
-- Table structure for table `doctor`
--

CREATE TABLE IF NOT EXISTS `doctor` (
  `doctor_id` integer NOT NULL primary key autoincrement,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50)   NULL,
  `last_name` varchar(50) NOT NULL,
  `specialization` varchar(70) NOT NULL,
  `phone_number` varchar(30) NOT NULL
)           ;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doctor_id`, `first_name`, `middle_name`, `last_name`, `specialization`, `phone_number`) VALUES
(1, 'Bob', NULL, 'Brown', 'Primary', '(123) 456-7890'),
(2, 'Lisa', NULL, 'Matthews', 'Primary', '(123) 456-7890'),
(3, 'Patricia', NULL, 'Millwood', 'Primary', '(123) 456-7890');
--
-- Table structure for table `allergic_medication`
--

CREATE TABLE IF NOT EXISTS `allergic_medication` (
  `allergic_med_id` integer NOT NULL primary key autoincrement,
  `resident_id` integer NOT NULL,
  `medication_name` varchar(70) NOT NULL,
  `allergic_diagnosis` text
)           ;

--
-- Dumping data for table `allergic_medication`
--

INSERT INTO `allergic_medication` (`allergic_med_id`, `resident_id`, `medication_name`, `allergic_diagnosis`) VALUES
(1, 1, 'Phenytoin', NULL),
(2, 1, 'Xalatan', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `allergy`
--

CREATE TABLE IF NOT EXISTS `allergy` (
  `allergy_id` integer NOT NULL primary key autoincrement,
  `resident_id` integer NOT NULL,
  `allergy_title` varchar(20) NOT NULL,
  `allergy_description` text NOT NULL
)           ;

--
-- Dumping data for table `allergy`
--

INSERT INTO `allergy` (`allergy_id`, `resident_id`, `allergy_title`, `allergy_description`) VALUES
(1, 1, 'pizza_allergy', 'blows up with pizza'),
(2, 2, 'doughnuts', 'turns blue'),
(3, 3, 'glutten', 'allergic to everything');

-- --------------------------------------------------------

--
-- Table structure for table `assessment`
--

CREATE TABLE IF NOT EXISTS `assessment` (
  `assessment_id` integer NOT NULL,
  `resident_id` integer NOT NULL,
  `assessment_date` date NOT NULL,
  `assessment_time` time NOT NULL,
  `weight` double NOT NULL,
  `blood_pressure` varchar(10) NOT NULL,
  `assess_notes` text NOT NULL
)       ;

--
-- Dumping data for table `assessment`
--

INSERT INTO `assessment` (`assessment_id`, `resident_id`, `assessment_date`, `assessment_time`, `weight`, `blood_pressure`, `assess_notes`) VALUES
(1, 1, '2013-01-03', '00:00:20', 132.6, '110/80', 'DROP * ahaha'),
(2, 2, '2013-03-11', '00:00:30', 145.2, '120/80', 'jaime is cool'),
(3, 3, '2013-01-14', '00:00:40', 132.5, '130/80', 'none'),
(4, 1, '2013-11-07', '00:00:50', 145, '36', 'TRUNCTUATE * this');

-- --------------------------------------------------------

--
-- Table structure for table `diet`
--

CREATE TABLE IF NOT EXISTS `diet` (
  `diet_id` integer NOT NULL primary key autoincrement,
  `resident_id` integer NOT NULL,
  `diet_title` varchar(20) NOT NULL,
  `diet_description` text NOT NULL
)           ;

--
-- Dumping data for table `diet`
--

INSERT INTO `diet` (`diet_id`, `resident_id`, `diet_title`, `diet_description`) VALUES
(1, 1, 'Fiber', 'Vegetables and oats'),
(2, 2, 'Sugar Free', 'Sugar Free Gum'),
(3, 3, 'Cholesterol Free', 'Cheerios, cook with vegetable oil');

-- --------------------------------------------------------



-- --------------------------------------------------------

--
-- Table structure for table `emergency_contact`
--

CREATE TABLE IF NOT EXISTS `emergency_contact` (
  `resident_id` integer NOT NULL,
  `em_id` integer NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50)   NULL,
  `last_name` varchar(50) NOT NULL,
  `phone_number` varchar(30) NOT NULL,
  `address1` varchar(95) NOT NULL,
  `address2` varchar(95) NOT NULL,
  `city` varchar(30) NOT NULL,
  `zip_code` varchar(16) NOT NULL,
  `relationship` varchar(50) NOT NULL
)       ;

--
-- Dumping data for table `emergency_contact`
--

INSERT INTO `emergency_contact` (`resident_id`, `em_id`, `first_name`, `middle_name`, `last_name`, `phone_number`, `address1`, `address2`, `city`, `zip_code`, `relationship`) VALUES
(1, 1, 'Trisha', NULL, 'Gonzalez', '(123) 456-7890', '12345 Healthy Lane', 'Paradise', 'NY', '67890', 'Friend'),
(2, 2, 'Benjamin', NULL, 'Williams', '(123) 456-7890', '12345 Healthy Lane', 'Paradise', 'NY', '67890', 'Friend'),
(3, 69, 'Jaime', '', 'Emiaj', '(714) 911 2233', '1169 Neverland ', 'Neverland', 'Santa Ana', '92707', 'Homie');

-- --------------------------------------------------------

--
-- Table structure for table `hospitalization`
--

CREATE TABLE IF NOT EXISTS `hospitalization` (
  `hospitalization_id` integer NOT NULL primary key autoincrement,
  `resident_id` integer NOT NULL,
  `hospitalization_date` date NOT NULL,
  `hospitalization_location` varchar(70) NOT NULL,
  `duration_of_stay` varchar(20) NOT NULL,
  `reason` text NOT NULL,
  `medication_changes` text NOT NULL,
  `diagnosis` varchar(25) NOT NULL,
  `notes` text NOT NULL
)           ;

--
-- Dumping data for table `hospitalization`
--

INSERT INTO `hospitalization` (`hospitalization_id`, `resident_id`, `hospitalization_date`, `hospitalization_location`, `duration_of_stay`, `reason`, `medication_changes`, `diagnosis`, `notes`) VALUES
(1, 1, '2012-06-27', 'Ossining General', '7 days', 'Diabetes', 'N/A', 'jaime', 'no'),
(2, 1, '2012-07-30', 'Ossining General', '10 days', 'Diabetes', 'N/A', 'ja', 'drop *'),
(3, 1, '2012-10-05', 'Ossining General', '12 days', 'Diabetes', 'N/A', 'ham', 'yes'),
(4, 1, '2013-03-05', 'Ossining General', '2 days', 'Diabetes', 'N/A', 'jim', 'idk');

-- --------------------------------------------------------

--
-- Table structure for table `medication`
--

CREATE TABLE IF NOT EXISTS `medication` (
  `medication_id` integer NOT NULL,
  `resident_id` integer NOT NULL,
  `medication_name` varchar(70) NOT NULL,
  `generic_name` varchar(70) NOT NULL,
  `med_expire` date NOT NULL,
  `med_prescribed` date NOT NULL,
  `med_dose(mg)` integer NOT NULL,
  `med_freq` text NOT NULL,
  `med_purpose` text NOT NULL,
  `note` text NOT NULL
)       ;

--
-- Dumping data for table `medication`
--

INSERT INTO `medication` (`medication_id`, `resident_id`, `medication_name`, `generic_name`, `med_expire`, `med_prescribed`, `med_dose(mg)`, `med_freq`, `med_purpose`, `note`) VALUES
(1, 1, 'Accupril', 'Quinapril', '2013-11-07', '0000-00-00', 500, 'twice/day', 'idk', 'hi'),
(2, 2, 'Xalatan', 'Latanoprost', '2013-11-14', '0000-00-00', 600, 'never', 'idk', 'hello'),
(3, 3, 'aderol', 'viagra', '2013-11-13', '0000-00-00', 69, '0', '', '0');

-- --------------------------------------------------------

--
-- Table structure for table `medication_history`
--

CREATE TABLE IF NOT EXISTS `medication_history` (
  `medication_id` integer NOT NULL,
  `resident_id` integer NOT NULL,
  `med_name` varchar(20) NOT NULL   ,
  `generic_name` varchar(15) NOT NULL   ,
  `prescribed` date NOT NULL,
  `expiration` date NOT NULL,
  `dosages` varchar(25) NOT NULL   ,
  `frequency` varchar(25) NOT NULL  ,
  `diets` varchar(30) NOT NULL,
  `purpose` varchar(25) NOT NULL ,
  `note` text NOT NULL
)       ;

--
-- Dumping data for table `medication_history`
--

INSERT INTO `medication_history` (`medication_id`, `resident_id`, `med_name`, `generic_name`, `prescribed`, `expiration`, `dosages`, `frequency`, `diets`, `purpose`, `note`) VALUES
(1, 1, 'idk', 'advil', '2013-11-14', '2013-11-21', 'a lot', 'everyday', 'none', 'to feel better', 'nope'),
(2, 2, 'idkf', 'ail', '2013-11-14', '2013-11-21', 'nope', 'today', 'none', 'just', 'yup'),
(3, 3, 'jaime', 'jaime1', '2013-11-06', '2013-11-06', '3x', '3hours', 'none', 'just', 'nope');

-- --------------------------------------------------------

--
-- Table structure for table `miscellaneous`
--

CREATE TABLE IF NOT EXISTS `miscellaneous` (
  `resident_id` integer NOT NULL,
  `misc_id` integer NOT NULL,
  `notes` text NOT NULL
)       ;

--
-- Dumping data for table `miscellaneous`
--

INSERT INTO `miscellaneous` (`resident_id`, `misc_id`, `notes`) VALUES
(1, 1, 'hey'),
(2, 2, 'no'),
(3, 3, 'jaime');

-- --------------------------------------------------------

--
-- Table structure for table `physical`
--

CREATE TABLE IF NOT EXISTS `physical` (
  `physical_date` date NOT NULL,
  `resident_id` integer NOT NULL
)       ;

--
-- Dumping data for table `physical`
--

INSERT INTO `physical` (`physical_date`, `resident_id`) VALUES
('2013-03-13', 1),
('2013-02-23', 2);

-- --------------------------------------------------------

--
-- Table structure for table `prescription`
--

CREATE TABLE IF NOT EXISTS `prescription` (
  `prescription_number` integer NOT NULL,
  `resident_id` integer NOT NULL,
  `medication_id` integer NOT NULL,
  `date_ordered` date NOT NULL,
  `date_received` date NOT NULL,
  `refill_date` date NOT NULL,
  `quantity` varchar(20) NOT NULL
)       ;

--
-- Dumping data for table `prescription`
--

INSERT INTO `prescription` (`prescription_number`, `resident_id`, `medication_id`, `date_ordered`, `date_received`, `refill_date`, `quantity`) VALUES
(12345, 1, 1, '2013-01-30', '2013-01-30', '2013-05-22', '2ml'),
(12456, 2, 2, '2013-01-01', '2013-01-01', '2013-12-22', '1ml');



-- --------------------------------------------------------

--
-- Table structure for table `resident_to_doctor`
--

CREATE TABLE IF NOT EXISTS `resident_to_doctor` (
  `resident_id` integer NOT NULL,
  `doctor_id` integer NOT NULL   
)       ;

--
-- Dumping data for table `resident_to_doctor`
--

INSERT INTO `resident_to_doctor` (`resident_id`, `doctor_id`) VALUES
(1, 1),
(3, 2),
(2, 3);

commit;
