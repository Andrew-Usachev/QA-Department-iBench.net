
#INRO
#Before reading the test cases, please read this manual.
#1. It is recommended to remove the comment function from the text of the cases one by one.
#2. After you have checked the functionality of the test case, comment it out again
#3. The test case will not work unless you remove the /* value at the beginning of the test case and the value */ at the end of the test case


#Test Case №1.  Check if database exists
/*SELECT SCHEMA_NAME # Check DB
  FROM INFORMATION_SCHEMA.SCHEMATA
 WHERE SCHEMA_NAME = 'iBench_net_DB';*/
 
#Test Case №2. Check correctness of the data in database
/*SELECT * FROM Find_Contractors; #Show all data from Find_Contractors table
SELECT * FROM Find_Employee; #Show all data from Find_Empliyee table*/

#Test Case №3. Confirm data new data can be added and deleted
/*INSERT INTO Find_Contractors VALUE #Added new data in Find_Contractors table
(1006,'All companies', 'Test Slot 5', 'Kyrgyzstan', 'QA Automation', 75, 'Senior', '5', 'B1 (Entermediate)', 'MySQL', 'Hello i am QA Automation Engineer');
INSERT INTO Find_Employee VALUE #Added new data in Find_Employee table
(2006,'Only verified', 'China', 'QA Automation', 'Hello i am QA Automation Engineer', 'Insurance', 8000, 'Senior', '4', 'B1 (Entermediate)', 'MySQL');
SELECT * FROM Find_Contractors; #Show all data from Find_Contractors table
SELECT * FROM Find_Employee; #Show all data from Find_Empliyee table
DELETE FROM Find_Contractors WHERE Id_Contractors=1006; #Deletetd new data from Find_Contractors table
DELETE FROM Find_Employee WHERE Id_Employee=2006; #Deletetd new data from Find_Employee table
SELECT * FROM Find_Contractors; #Show all data from Find_Contractors table
SELECT * FROM Find_Employee; #Show all data from Find_Empliyee table*/

#Test Case №4. Confirm that 100 users can be added simultaneously without problem
/*INSERT INTO Find_Contractors SET Id_Contractors=1006, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1007, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1008, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1009, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1010, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1011, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1012, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1013, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1014, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1015, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1016, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1017, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1018, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1019, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1020, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1021, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1022, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1023, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1024, Project_Description='Text';INSERT INTO Find_Contractors SET Id_Contractors=1025, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1026, Project_Description='Text';INSERT INTO Find_Contractors SET Id_Contractors=1027, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1028, Project_Description='Text';INSERT INTO Find_Contractors SET Id_Contractors=1029, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1030, Project_Description='Text';INSERT INTO Find_Contractors SET Id_Contractors=1031, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1032, Project_Description='Text';INSERT INTO Find_Contractors SET Id_Contractors=1033, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1034, Project_Description='Text';INSERT INTO Find_Contractors SET Id_Contractors=1035, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1036, Project_Description='Text';INSERT INTO Find_Contractors SET Id_Contractors=1037, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1038, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1039, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1040, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1041, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1042, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1043, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1044, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1045, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1046, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1047, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1048, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1049, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1050, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1051, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1052, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1053, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1054, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1055, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1056, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1057, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1058, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1059, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1060, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1061, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1062, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1063, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1064, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1065, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1066, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1067, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1068, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1069, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1070, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1071, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1072, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1073, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1074, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1075, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1076, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1077, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1078, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1079, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1080, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1081, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1082, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1083, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1084, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1085, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1086, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1087, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1088, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1089, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1090, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1091, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1092, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1093, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1094, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1095, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1096, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1097, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1098, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1099, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1100, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1101, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1102, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1103, Project_Description='Text';
INSERT INTO Find_Contractors SET Id_Contractors=1104, Project_Description='Text'; INSERT INTO Find_Contractors SET Id_Contractors=1105, Project_Description='Text'; 

SELECT * FROM Find_Contractors; #Show all data from Find_Contractors table*/
/*DELETE FROM Find_Contractors WHERE Project_Description='Text' LIMIT 100;
SELECT * FROM Find_Contractors; #Show all data from Find_Contractors table*/

#Test Case №5. Confirm Data can be filtered and slice with proper requested results
/*SELECT Id_Contractors,Verified_companies,Slot_name,Developers_location,Job_title FROM Find_Contractors
ORDER BY Slot_name ASC; #Filter by specific results and sort in ascending order
SELECT Benefits, Salary_month, Position_level,Experience,English_level,Skills FROM Find_Employee
ORDER BY Experience DESC; #Filter by specific results and sort in descending order

SELECT Benefits 
FROM (SELECT Benefits, Salary_month, Position_level,Experience,English_level,Skills FROM Find_Employee) as newtable; #Filter by specific results in a new table

SELECT distinct Job_title FROM Find_Contractors; #Removing duplicates
SELECT distinct Position_level FROM Find_Employee; #Removing duplicates

SELECT * FROM Find_Contractors 
WHERE (Maximum_hourly_rate <> 75 AND Position_level = 'Junior'); #Composite filter

SELECT * FROM Find_Employee WHERE NOT((Position_level = 'Middle' OR English_level <> 'C1 (Advanced)') AND Experience <> '8'); #Composite filter

SELECT Experience, count(*) FROM Find_Contractors 
GROUP BY Experience; #grouping

SELECT Position_level, sum(Experience) FROM Find_Contractors 
GROUP BY Position_level; #Summation and Grouping

SELECT Position_level, sum(Experience) as Summa FROM Find_Contractors 
GROUP BY Position_level 
HAVING Position_level in ('Senior', 'Junior'); #Summation, Grouping and Filtering

SELECT Benefits, Salary_month, Position_level,Experience,English_level,Skills FROM Find_Employee
ORDER BY right(Experience, 3); #Sort by right three characters

SELECT Benefits, Salary_month, Position_level,Experience,English_level,Skills FROM Find_Employee
ORDER BY 3; #Sort by field Position_level

SELECT Maximum_hourly_rate FROM Find_Contractors
WHERE Maximum_hourly_rate BETWEEN 10 AND 60; #Filter by results between specific values

SELECT Benefits, Salary_month, Position_level,Experience,English_level,Skills FROM Find_Employee
WHERE LEFT (Position_level, 1) = 'S'; #Filter by values that start with a specific symbol

SELECT Benefits, Salary_month, Position_level,Experience,English_level,Skills FROM Find_Employee
WHERE Position_level LIKE '_e%i%'; #Filter by values that contain specific symbols

SELECT Benefits, Salary_month, Position_level,Experience,English_level,Skills FROM Find_Employee
WHERE Position_level REGEXP '^[SM]'; #Filter using regular expressions - displays values that do not start with S and M*/

#Test Case №6. Confirm Data can be join with other schemas for info extraction
/*SELECT Id_Marketplace
FROM Publci_Marketplace JOIN Find_Employee
on Publci_Marketplace.Id_Employee = Find_Employee.Id_Employee; #Join tables

SELECT Verified_companies,Slot_name,Developers_location,Job_title FROM Find_Contractors
JOIN Publci_Marketplace on Publci_Marketplace.Id_Contractors = Find_Contractors.Id_Contractors; #Join tables

SELECT Verified_companies,Slot_name,Developers_location,Job_title FROM Find_Contractors
JOIN Publci_Marketplace on Publci_Marketplace.Id_Contractors = Find_Contractors.Id_Contractors
WHERE Find_Contractors.Job_title = 'QA Manual'; #Join tables and filter

SELECT Verified_companies,Slot_name,Developers_location,Job_title FROM Find_Contractors
JOIN Publci_Marketplace on Publci_Marketplace.Id_Contractors = Find_Contractors.Id_Contractors
WHERE Find_Contractors.Job_title = 'QA Manual'
AND Developers_location <> 'India'; #Join tables and filter

SELECT Verified_companies,Slot_name,
CONCAT(Find_Contractors.Developers_location , ' ' , Find_Contractors.Job_title) location_and_Title 
FROM Find_Contractors
JOIN Publci_Marketplace on Publci_Marketplace.Id_Contractors = Find_Contractors.Id_Contractors; #Joining tables and concatenating columns

SELECT Id_Contractors, Developers_location, Position_level FROM Find_Contractors
UNION
SELECT Id_Employee, Developers_location, Position_level FROM Find_Employee; #Combining queries*/





