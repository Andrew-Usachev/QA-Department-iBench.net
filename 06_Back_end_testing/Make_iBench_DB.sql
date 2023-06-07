#INTRO
#First create the database and tables with this script and then use the test case scripts from the file 'Test_Cases_Scripts_iBench_DB'

DROP DATABASE IF EXISTS iBench_net_DB;
CREATE DATABASE iBench_net_DB;
USE iBench_net_DB;


CREATE TABLE `Find_Contractors` (
  `Id_Contractors` INT NOT NULL,
  `Verified_companies` enum ('All companies','Only verified'),
  `Slot_name` VARCHAR (45) NULL,
  `Developers_location` enum ('United States','Canada', 'Mexico', 'Kyrgyzstan', 'India'),
  `Job_title` enum ('QA Automation','QA Manual'),
  `Maximum_hourly_rate` INT NOT NULL,
  `Position_level` enum ('Junior','Middle','Senior','Team Lead'),
  `Experience` enum ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'),
  `English_level` enum ('0 (Begginer)','A1 (Elementary)','A2 (Pre-Entermediate)','B1 (Entermediate)','B2 (Upper Intermediate)','C1 (Advanced)','C2 (Proficient)'),
  `Skills` enum ('SQL','MySQL','MongoDB','Git','GitHUB'),
  `Project_Description` VARCHAR (1000) NOT NULL,
  PRIMARY KEY (`Id_Contractors`));
  
  
  CREATE TABLE `Find_Employee` (
  `Id_Employee` INT NOT NULL,
  `Verified_companies` enum ('All companies','Only verified'),
  `Developers_location` enum ('United States','Canada', 'Armenia', 'France', 'China'),
  `Job_title` enum ('QA Automation','QA Manual'),
  `Position_Description` VARCHAR (1000) NOT NULL,
  `Benefits` VARCHAR (1000) NOT NULL,
  `Salary_month` INT NOT NULL,
  `Position_level` enum ('Junior','Middle','Senior','Team Lead'),
  `Experience` enum ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'),
  `English_level` enum ('0 (Begginer)','A1 (Elementary)','A2 (Pre-Entermediate)','B1 (Entermediate)','B2 (Upper Intermediate)','C1 (Advanced)','C2 (Proficient)'),
  `Skills` enum ('SQL','MySQL','MongoDB','GIT','GitHUB'),
  PRIMARY KEY (`Id_Employee`));
  
    CREATE TABLE `Publci_Marketplace` (
  `Id_Marketplace` INT NOT NULL,
  `Id_Contractors` VARCHAR (45) NULL,
  `Id_Employee` VARCHAR (45) NULL,
  PRIMARY KEY (`Id_Marketplace`));


INSERT INTO Find_Contractors VALUE 
(1001,'All companies', 'Test Slot 1', 'United States', 'QA Automation', 50, 'Middle', '5', 'C1 (Advanced)', 'MySQL', 'Hello i am QA Automation Engineer'),
(1002,'Only verified', 'Test Slot 2', 'Canada', 'QA Manual', 60, 'Team Lead', '5', 'B2 (Upper Intermediate)', 'SQL', 'Hello i am QA Manual Engineer'),
(1003,'All companies', 'Test Slot 3', 'Mexico', 'QA Manual', 15, 'Junior', '2', 'B1 (Entermediate)', 'GIT', 'Hello i am QA Manual Engineer'),
(1004,'Only verified', 'Test Slot 4', 'India', 'QA Manual', 10, 'Junior', '1', 'A2 (Pre-Entermediate)', 'GitHUB', 'Hello i am QA Manual Engineer'),
(1005,'All companies', 'Test Slot 5', 'Kyrgyzstan', 'QA Automation', 75, 'Senior', '5', 'B1 (Entermediate)', 'MySQL', 'Hello i am QA Automation Engineer');

INSERT INTO Find_Employee VALUE 
(2001,'All companies', 'United States', 'QA Manual', 'Hello i am QA Manual Engineer', 'Insurance', 5000, 'Middle', '5', 'C1 (Advanced)', 'MySQL'),
(2002,'All companies', 'Canada', 'QA Automation', 'Hello i am QA Automation Engineer', 'Insurance', 10000, 'Senior', '5', 'C1 (Advanced)', 'SQL'),
(2003,'All companies', 'Armenia', 'QA Manual', 'Hello i am QA Manual Engineer', 'Insurance', 4000, 'Team Lead', '8', 'A2 (Pre-Entermediate)', 'GitHUB'),
(2004,'Only verified', 'France', 'QA Automation', 'Hello i am QA Automation Engineer', 'Insurance', 4500, 'Junior', '2', 'B1 (Entermediate)', 'GIT'),  
(2005,'Only verified', 'China', 'QA Automation', 'Hello i am QA Automation Engineer', 'Insurance', 8000, 'Senior', '4', 'B1 (Entermediate)', 'MySQL');

INSERT INTO Publci_Marketplace VALUE 
(3001, null, 2001),
(3002, 1002, 2002),
(3003, null, 2003),
(3004, 1004, null),  
(3005, 1005, 2005);
