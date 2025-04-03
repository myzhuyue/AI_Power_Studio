
# Top Engineering Questions for Interview

> Version 1.0
> 
> Created Date: 2025-04-02
> 

- This documents will introduce hot questions in most recent ***Data Engineering*** related interviews, with corresonding reference linkage or documents. 
 
 - Keep in mind, all below questions could dive into more deeper based on different roles and responsiblities. 
 
 - Please priorize the questions, feel free to add more questions with answers for your own expertise.

 - If you need Chinese version of this document, please ask Concierge to translate it.

## Table of Content

- [Top Engineering Questions for Interview](#top-engineering-questions-for-interview)
  - [Table of Content](#table-of-content)
  - [How to Use](#how-to-use)
  - [Part 1 - Big Data Theory](#part-1---big-data-theory)
  - [Part 2 - Data Warehouse \& Modeling](#part-2---data-warehouse--modeling)
  - [Part 3 - Soft Skills and Problem-Solving](#part-3---soft-skills-and-problem-solving)
  - [Part 4 - Programming \& Visualization](#part-4---programming--visualization)
    - [SQL](#sql)
    - [Python](#python)
    - [Spark](#spark)
      - [Basic Knowledge](#basic-knowledge)
      - [Parctice 1 - Select](#parctice-1---select)
      - [Parctice 2 - Basic Joins](#parctice-2---basic-joins)
      - [Parctice 3 - Basic Aggregate Functions](#parctice-3---basic-aggregate-functions)
      - [Parctice 4 - Sorting and Grouping](#parctice-4---sorting-and-grouping)
      - [Parctice 5 - Advanced Select and Joins](#parctice-5---advanced-select-and-joins)
      - [Parctice 6 - Subqueries](#parctice-6---subqueries)
      - [Parctice 7 - Advanced String Functions / Regex / Clause](#parctice-7---advanced-string-functions--regex--clause)
    - [Power BI](#power-bi)
      - [Prepare the data](#prepare-the-data)
      - [Model the data](#model-the-data)
      - [Visualize \& analyze the data](#visualize--analyze-the-data)
      - [deploy \&  maintain assets](#deploy---maintain-assets)

## How to Use

- To be updated

---

## Part 1 - Big Data Theory

1. **What is Hadoop?**

> Hadoop is an open-source framework designed for distributed storage and processing of large datasets across clusters of computers. It consists of two main components:
>  - The Hadoop Distributed File System (HDFS) for storage
>  - MapReduce for processing.

2. **Explain the concept of MapReduce.**

> MapReduce is a programming model and processing technique for distributed computing. It consists of two main phases:
> 
> - Map: Divides the input data into smaller chunks and processes them in parallel.
> 
> - Reduce: Aggregates the results from the Map phase to produce the final output

3. **What is Apache Spark?** 

> Apache Spark is a fast, in-memory data processing engine with elegant and expressive development APIs to allow data workers to efficiently execute streaming, machine learning or SQL workloads that require fast iterative access to datasets.

4. **How does Spark differ from Hadoop MapReduce?**

> A: Key differences include:
> - Speed: Spark is generally faster due to in-memory processing
> - Ease of use: Spark offers more user-friendly APIs in multiple languages
> - Versatility: Spark supports various workloads beyond batch processing,including streaming and machine learning
> - Iterative processing: Spark is more efficient for iterative algorithms common in machine learning

5. **What the difference between Parquet and Orc file format**

6. **What is the difference between a data lake and a data warehouse?**

> A: Key differences include:
> - Data structure: Data warehouses store structured data, while data lakes can store structured, semi-structured, and unstructured data
> - Purpose: Data warehouses are optimized for analysis, while data lakes serve as a repository for raw data
> - Schema: Data warehouses use schema-on-write, while data lakes use schema-on-read
> - Users: Data warehouses are typically used by business analysts, while data lakes are often used by data scientists

7. **What is the Lambda architecture?**

> The Lambda architecture is a data processing architecture designed to handle massive quantities of data by taking advantage of both batch and stream processing methods. It consists of three layers:
> - Batch layer: Manages the master dataset and pre-computes batch views
> - Speed layer: Handles real-time data processing
> - Serving layer: Responds to queries by combining results from batch and speed layers

8. **Explain the concept of data partitioning.** 

> Data partitioning is the process of dividing a large dataset into smaller, more manageable pieces called partitions. This technique is used to improve query performance, enable parallel processing, and manage large datasets more effectively. Common partitioning strategies include:
> - Range partitioning
> - Hash partitioning
> - List partitioning

---

## Part 2 - Data Warehouse & Modeling

1. **What is data modeling?**

> - Data modeling is the process of creating a visual representation of data structures and relationships within a system. It helps in understanding, organizing, and standardizing data elements and their relationships.

2. **What are the three main types of data models?**

> The three main types of data models are:
> - Conceptual data model: High-level view of data structures and relationships
> - Logical data model: Detailed view of data structures, independent of any specific database management system
> - Physical data model: Representation of the data model as implemented in a specific database system

3. **What is star schema and snowflake schema?** 

> - Star schema is a data warehouse schema where a central fact table is surrounded by dimension tables. It's called a star schema because the diagram resembles a star, with the fact table at the center and dimension tables as points.
> - What is snowflake schema? 
Snowflake schema is a variation of the star schema where dimension tables are normalized into multiple related tables. This creates a structure that looks like a snowflake, with the fact table at the center and increasingly granular dimension tables branching out.

4. **What are the advantages and disadvantages of denormalization?**

> Advantages of denormalization:
> - Improved query performance
> - Simplifies queries
> - Reduces the need for joins
Disadvantages of denormalization:

Increased data redundancy
More complex data updates and inserts
Potential data inconsistencies

5. **What is the slowly changing dimension (SCD)?**

> Slowly changing dimension (SCD) is a concept in data warehousing that describes how to handle changes to dimension data over time. There are different types of SCDs, with the most common being:
> - Type 1: Overwrite the old value
> - Type 2: Create a new row with the changed data
> - Type 3: Add a new column to track changes

---

## Part 3 - Soft Skills and Problem-Solving

1. **What strategies do you use for optimizing query performance in large datasets?**

> Strategies for optimizing query performance include:
> - Proper indexing of frequently queried columns
> - Partitioning large tables
> - Using materialized views for complex, frequently-run queries
> - Query optimization and rewriting
> - Implementing caching mechanisms
> - Using columnar storage formats for analytical workloads
> - Leveraging distributed computing for large-scale data processing

2. **How do you approach data pipeline testing?**

> Approaches to data pipeline testing include:
> - Unit testing individual components
> - Integration testing to ensure components work together
> - End-to-end testing of the entire pipeline
> - Data validation testing to ensure data integrity
> - Performance testing under various load conditions
> - Fault injection testing to verify error handling
> - Regression testing after making changes

3. **What is your experience with data versioning and how do you implement it?**

> Data versioning involves tracking changes to datasets over time. Implementation strategies include:
> - Using version control systems for code and configuration files
> - Implementing slowly changing dimensions in data warehouses
> - Using data lake technologies that support versioning (e.g., Delta Lake)
> - Maintaining metadata about dataset versions
> - Implementing a robust backup and restore strategy

4. **What is your experience with data catalogs and metadata management?**

> Data catalogs and metadata management involve:
> - Implementing tools for documenting datasets, their schemas, and relationships
> - Establishing processes for metadata creation and maintenance
> - Integrating metadata across different systems and tools
> - Implementing data discovery and search capabilities
> - Supporting data governance and compliance initiatives
> - Facilitating self-service analytics for business users

5. **How do you handle schema evolution in data pipelines?**

> Approaches to handling schema evolution include:
> - Using schema-on-read formats like Parquet or Avro
> - Implementing backward and forward compatibility in schema designs
> - Versioning schemas and maintaining compatibility between versions
> - Using schema registries for centralized schema management
> - Implementing data migration strategies for major schema changes
> - Testing schema changes thoroughly before deployment

6.  **What is your approach to monitoring and alerting in data engineering systems?** 

> Effective monitoring and alerting involves:
> - Implementing comprehensive logging across all system components
> - Setting up real-time monitoring dashboards
> - Defining key performance indicators (KPIs) and service level objectives (SLOs)
> - Implementing proactive alerting for potential issues
> - Using anomaly detection techniques for identifying unusual patterns
> - Establishing an incident response process
> - Conducting regular system health checks and audits

7. **How do you ensure data consistency in distributed systems?**

> A: Strategies for ensuring data consistency include:
> - Implementing strong consistency models where necessary
> - Using eventual consistency for improved performance in certain scenarios
> - Implementing distributed transactions when needed
> - Using techniques like two-phase commit or saga pattern for complex operations
> - Implementing idempotent operations to handle duplicate requests
> - Designing for conflict resolution in multi-master systems

8. **What is your experience with data modeling for NoSQL databases?**

> A: Data modeling for NoSQL databases involves:
> - Understanding the specific NoSQL database type (document, key-value, column-family, graph)
> - Designing for query patterns rather than normalized data structures
> - Considering denormalization and data duplication for performance
> - Planning for scalability and partitioning
> - Implementing appropriate indexing strategies
> - Handling schema flexibility and evolution

9. **How do you approach data quality assurance in ETL processes?**

> A: Data quality assurance in ETL involves:
> - Implementing data validation rules at the source and target
> - Performing data profiling to understand data characteristics
> - Implementing data cleansing and standardization processes
> - Using data quality scorecards to track improvements over time
> - Implementing data reconciliation checks between source and target
> - Establishing a process for handling and resolving data quality issues

10. **What strategies do you use for managing technical debt in data engineering projects?**

> A: Strategies for managing technical debt include:
> - Regular code reviews and refactoring sessions
> - Implementing CI/CD practices for consistent deployments
> - Maintaining comprehensive documentation
> - Prioritizing critical updates and migrations
> - Allocating time for system improvements in project planning
> - Conducting periodic architecture reviews
> - Implementing automated testing to catch regressions

11. **How do you handle data privacy and compliance requirements in your projects?** 

> A: Approaches to handling data privacy and compliance include:
> - Implementing data classification and tagging
> - Applying appropriate data masking and encryption techniques
> - Implementing role-based access control (RBAC)
> - Maintaining audit logs for data access and modifications
> - Implementing data retention and deletion policies
> - Conducting regular privacy impact assessments
> - Staying updated with relevant regulations (e.g., GDPR, CCPA)

---

## Part 4 - Programming & Visualization

### SQL

1. [Article Views I](./sql-questions/Article%20Views%20I.md)
2. [Average Selling Price](./sql-questions/Average%20Selling%20Price.md)
3. [Average Time of Process per Machine](./sql-questions/Average%20Time%20of%20Process%20per%20Machine.md)
4. [Big Countries](./sql-questions/Big%20Countries.md)
5. [Confirmation Rate](./sql-questions/Confirmation%20Rate.md)
6. [Customer Who Visited but Did Not Make Any Transactions](./sql-questions/Customer%20Who%20Visited%20but%20Did%20Not%20Make%20Any%20Transactions.md)
7. [Employee Bonus](./sql-questions/Employee%20Bonus.md)
8. [Find Customer Refree](./sql-questions/Find%20Customer%20Refree.md)
9. [Immediate Food Delivery II](./sql-questions/Immediate%20Food%20Delivery%20II.md)
10. [Invalid Tweets](./sql-questions/Invalid%20Tweets.md)
11. [Managers with at Least 5 Dirsct Reports](./sql-questions/Managers%20with%20at%20Least%205%20Direct%20Reports.md)
12. [Monthly Transactions I](./sql-questions/Monthly%20Transactions%20I.md)
13. [Not Boring Movies](./sql-questions/Not%20Boring%20Movies.md)
14. [Percentage of Users Attended a Contest](./sql-questions/Percentage%20of%20Users%20Attended%20a%20Contest.md)
15. [Product Sales Analysis 1](./sql-questions/Product%20Sales%20Analysis%201.md)
16. [Project Employees I](./sql-questions/Project%20Employees%20I.md)
17. [Queries Quality and Percentage](./sql-questions/Queries%20Quality%20and%20Percentage.md)
18. [Recycle and Low Fat Products](./sql-questions/Recycle%20and%20Low%20Fat%20Products.md)
19. [Replace Employee ID With The Unique Identifier](./sql-questions/Replace%20Employee%20ID%20With%20The%20Unique%20Identifier.md)
20. [Rising Temperature](./sql-questions/Rising%20Temperature.md)
21. [Students and Examinations](./sql-questions/Students%20and%20Examinations.md)

### Python

1. **Why is Python popular in data engineering?**

> Python is popular in data engineering due to:
> 
> - Ease of use and readability: Rich ecosystem of libraries and frameworks for data processing (e.g., Pandas, NumPy)
> - Support for big data technologies (e.g., PySpark): Integration with various data sources and APIs
> - Strong community support and documentation

### Spark

#### Basic Knowledge

1. **What is PySpark?** 

> PySpark is the Python API for Apache Spark. It allows you to write Spark applications using Python, combining the simplicity of Python with the power of Spark for distributed data processing.

2. **What is UDF in Spark?**

#### Parctice 1 - Select

1. [Recyclable and Low Fat Products](pyspark-top-sql-50/1_Select/01_1757_Recyclable_and_Low_Fat_Products.ipynb)
2. [Find Customer Referee](pyspark-top-sql-50/1_Select/02_584_Find_Customer_Referee.ipynb)
3. [Big Countries](pyspark-top-sql-50/1_Select/03_595_Big_Countries.ipynb)
4. [Article Views I](pyspark-top-sql-50/1_Select/04_1148_Article_Views_I.ipynb)
5. [Invalid Tweets](pyspark-top-sql-50/1_Select/05_1683_Invalid_Tweets.ipynb)

#### Parctice 2 - Basic Joins

6. [Replace Employee ID With The Unique Identifier](pyspark-top-sql-50/2_Basic_Joins/06_1378_Replace_Employee_ID_With_The_Unique_Identifier.ipynb)
7. [Product Sales Analysis I](pyspark-top-sql-50/2_Basic_Joins/07_1068_Product_Sales_Analysis_I.ipynb)
8. [Customer Who Visited but Did Not Make Any Transactions](pyspark-top-sql-50/2_Basic_Joins/08_1581_Customer_Who_Visited_but_Did_Not_Make_Any_Transactions.ipynb)
9. [Rising Temperature](pyspark-top-sql-50/2_Basic_Joins/09_197_Rising_Temperature.ipynb)
10. [Average Time of Process per Machine](pyspark-top-sql-50/2_Basic_Joins/10_1661_Average_Time_of_Process_per_Machine.ipynb)
11. [Employee Bonus](pyspark-top-sql-50/2_Basic_Joins/11_577_Employee_Bonus.ipynb)
12. [Students and Examinations](pyspark-top-sql-50/2_Basic_Joins/12_1280_Students_and_Examinations.ipynb)
13. [Managers with at Least 5 Direct Reports](pyspark-top-sql-50/2_Basic_Joins/13_570_Managers_with_at_Least_5_Direct_Reports.ipynb)
14. [Confirmation Rate](pyspark-top-sql-50/2_Basic_Joins/14_1934_Confirmation_Rate.ipynb)

#### Parctice 3 - Basic Aggregate Functions

15. [Not Boring Movies](pyspark-top-sql-50/3_Basic_Aggregate_Functions/15_620_Not_Boring_Movies.ipynb)
16. [Average Selling Price](pyspark-top-sql-50/3_Basic_Aggregate_Functions/16_1251_Average_Selling_Price.ipynb)
17. [Project Employees I](pyspark-top-sql-50/3_Basic_Aggregate_Functions/17_1075_Project_Employees_I.ipynb)
18. [Percentage of Users Attended a Contest](pyspark-top-sql-50/3_Basic_Aggregate_Functions/18_1633_Percentage_of_Users_Attended_a_Contest.ipynb)
19. [Queries Quality and Percentage](pyspark-top-sql-50/3_Basic_Aggregate_Functions/19_1211_Queries_Quality_and_Percentage.ipynb)
20. [Monthly Transactions I](pyspark-top-sql-50/3_Basic_Aggregate_Functions/20_1193_Monthly_Transactions_I.ipynb)
21. [Immediate Food Delivery II](pyspark-top-sql-50/3_Basic_Aggregate_Functions/21_1174_Immediate_Food_Delivery_II.ipynb)
22. [Game Play Analysis IV](pyspark-top-sql-50/3_Basic_Aggregate_Functions/22_550_Game_Play_Analysis_IV.ipynb)

#### Parctice 4 - Sorting and Grouping

23. [Number of Unique Subjects Taught by Each Teacher](pyspark-top-sql-50/4_Sorting_and_Grouping/23_2356_Number_of_Unique_Subjects_Taught_by_Each_Teacher.ipynb)
24. [User Activity for the Past 30 Days I](pyspark-top-sql-50/4_Sorting_and_Grouping/24_1141_User_Activity_for_the_Past_30_Days_I.ipynb)
25. [Product Sales Analysis III](pyspark-top-sql-50/4_Sorting_and_Grouping/25_1070_Product_Sales_Analysis_III.ipynb)
26. [Classes More Than 5 Students](pyspark-top-sql-50/4_Sorting_and_Grouping/26_596_Classes_More_Than_5_Students.ipynb)
27. [Find Followers Count](pyspark-top-sql-50/4_Sorting_and_Grouping/27_1729_Find_Followers_Count.ipynb)
28. [Biggest Single Number](pyspark-top-sql-50/4_Sorting_and_Grouping/28_619_Biggest_Single_Number.ipynb)
29. [Customers Who Bought All Products](pyspark-top-sql-50/4_Sorting_and_Grouping/29_1045_Customers_Who_Bought_All_Products.ipynb)

#### Parctice 5 - Advanced Select and Joins

30. [The Number of Employees Which Report to Each Employee](pyspark-top-sql-50/5_Advanced_Select_and_Joins/30_1731_The_Number_of_Employees_Which_Report_to_Each_Employee.ipynb)
31. [Primary Department for Each Employee](pyspark-top-sql-50/5_Advanced_Select_and_Joins/31_1789_Primary_Department_for_Each_Employee.ipynb)
32. [Triangle Judgement](pyspark-top-sql-50/5_Advanced_Select_and_Joins/32_610_Triangle_Judgement.ipynb)
33. [Consecutive Numbers](pyspark-top-sql-50/5_Advanced_Select_and_Joins/33_180_Consecutive_Numbers.ipynb)
34. [Product Price at a Given Date](pyspark-top-sql-50/5_Advanced_Select_and_Joins/34_1164_Product_Price_at_a_Given_Date.ipynb)
35. [Last Person to Fit in the Bus](pyspark-top-sql-50/5_Advanced_Select_and_Joins/35_1204_Last_Person_to_Fit_in_the_Bus.ipynb)
36. [Count Salary Categories](pyspark-top-sql-50/5_Advanced_Select_and_Joins/36_1907_Count_Salary_Categories.ipynb)

#### Parctice 6 - Subqueries

37. [Employees Whose Manager Left the Company](pyspark-top-sql-50/6_Subqueries/37_1978_Employees_Whose_Manager_Left_the_Company.ipynb)
38. [Exchange Seats](pyspark-top-sql-50/6_Subqueries/38_626_Exchange_Seats.ipynb)
39. [Movie Rating](pyspark-top-sql-50/6_Subqueries/39_1341_Movie_Rating.ipynb)
40. [Restaurant Growth](pyspark-top-sql-50/6_Subqueries/40_1321_Restaurant_Growth.ipynb)
41. [Friend Requests II: Who Has the Most Friends](pyspark-top-sql-50/6_Subqueries/41_602_Friend_Requests_II_Who_Has_the_Most_Friends.ipynb)
42. [Investments in 2016](pyspark-top-sql-50/6_Subqueries/42_585_Investments_In_2016.ipynb)
43. [Department Top Three Salaries](pyspark-top-sql-50/6_Subqueries/43_185_Department_Top_Three_Salaries.ipynb)

#### Parctice 7 - Advanced String Functions / Regex / Clause

44. [Fix Names in a Table](pyspark-top-sql-50/7_Advanced_String_Functions_Regex_Clause/44_1667_Fix_Names_in_a_Table.ipynb)
45. [Patients With a Condition](pyspark-top-sql-50/7_Advanced_String_Functions_Regex_Clause/45_1527_Patients_With_a_Condition.ipynb)
46. [Delete Duplicate Emails](pyspark-top-sql-50/7_Advanced_String_Functions_Regex_Clause/46_196_Delete_Duplicate_Emails.ipynb)
47. [Second Highest Salary](pyspark-top-sql-50/7_Advanced_String_Functions_Regex_Clause/47_176_Second_Highest_Salary.ipynb)
48. [Group Sold Products By The Date](pyspark-top-sql-50/7_Advanced_String_Functions_Regex_Clause/48_1484_Group_Sold_Products_By_The_Date.ipynb)
49. [List the Products Ordered in a Period](pyspark-top-sql-50/7_Advanced_String_Functions_Regex_Clause/49_1327_List_the_Products_Ordered_in_a_Period.ipynb)
50. [Find Users With Valid E-Mails](pyspark-top-sql-50/7_Advanced_String_Functions_Regex_Clause/50_1517_Find_Users_With_Valid_E-Mails.ipynb)


### Power BI

#### [Prepare the data](./powerbi-questions/prepare-the-data.md)
#### [Model the data](./powerbi-questions/model-the-data.md)
#### [Visualize & analyze the data](./powerbi-questions/visualize&analyze-the-data.md)
#### [deploy &  maintain assets](./powerbi-questions/deploy&maintain-assets.md)
