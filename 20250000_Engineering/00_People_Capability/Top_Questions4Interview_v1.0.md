
# Top Engineering Questions for Interview

> Version 1.0
> 
> Created Date: 2025-04-02
> 
> - This documents will introduce hot questions in most recent ***Data Engineering*** related interviews, with corresonding reference linkage or documents. 
> 
> - Keep in mind, all below questions could dive into more deeper based on different roles and responsiblities. 
> 
> - Please priorize the questions, fit your needs.
>
> - If you need Chinese version of this document, please ask Concierge to translate it.

- [Top Engineering Questions for Interview](#top-engineering-questions-for-interview)
  - [Big Data Theory](#big-data-theory)
  - [Data Warehouse \& Modeling](#data-warehouse--modeling)
  - [Programming \& Visualization](#programming--visualization)
    - [SQL](#sql)
    - [Python](#python)
    - [Spark](#spark)
    - [Power BI DAX](#power-bi-dax)
  - [Soft Skills and Problem-Solving](#soft-skills-and-problem-solving)

## Big Data Theory

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

## Data Warehouse & Modeling

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

## Programming & Visualization

### SQL

1. [Article Views I](./SQL_Questions/Article%20Views%20I.md)
2. [Average Selling Price](./SQL_Questions/Average%20Selling%20Price.md)
3. [Average Time of Process per Machine](./SQL_Questions/Average%20Time%20of%20Process%20per%20Machine.md)
4. [Big Countries](./SQL_Questions/Big%20Countries.md)
5. [Confirmation Rate](./SQL_Questions/Confirmation%20Rate.md)
6. [Customer Who Visited but Did Not Make Any Transactions](./SQL_Questions/Customer%20Who%20Visited%20but%20Did%20Not%20Make%20Any%20Transactions.md)
7. [Employee Bonus](./SQL_Questions/Employee%20Bonus.md)
8. [Find Customer Refree](./SQL_Questions/Find%20Customer%20Refree.md)
9. [Immediate Food Delivery II](./SQL_Questions/Immediate%20Food%20Delivery%20II.md)
10. [Invalid Tweets](./SQL_Questions/Invalid%20Tweets.md)
11. [Managers with at Least 5 Dirsct Reports](./SQL_Questions/Managers%20with%20at%20Least%205%20Direct%20Reports.md)
12. [Monthly Transactions I](./SQL_Questions/Monthly%20Transactions%20I.md)
13. [Not Boring Movies](./SQL_Questions/Not%20Boring%20Movies.md)
14. [Percentage of Users Attended a Contest](./SQL_Questions/Percentage%20of%20Users%20Attended%20a%20Contest.md)
15. [Product Sales Analysis 1](./SQL_Questions/Product%20Sales%20Analysis%201.md)
16. [Project Employees I](./SQL_Questions/Project%20Employees%20I.md)
17. [Queries Quality and Percentage](./SQL_Questions/Queries%20Quality%20and%20Percentage.md)
18. [Recycle and Low Fat Products](./SQL_Questions/Recycle%20and%20Low%20Fat%20Products.md)
19. [Replace Employee ID With The Unique Identifier](./SQL_Questions/Replace%20Employee%20ID%20With%20The%20Unique%20Identifier.md)
20. [Rising Temperature](./SQL_Questions/Rising%20Temperature.md)
21. [Students and Examinations](./SQL_Questions/Students%20and%20Examinations.md)

### Python
1. **Why is Python popular in data engineering?**

> Python is popular in data engineering due to:
> 
> - Ease of use and readability: Rich ecosystem of libraries and frameworks for data processing (e.g., Pandas, NumPy)
> - Support for big data technologies (e.g., PySpark): Integration with various data sources and APIs
> - Strong community support and documentation

### Spark

1. **What is PySpark?** 

> PySpark is the Python API for Apache Spark. It allows you to write Spark applications using Python, combining the simplicity of Python with the power of Spark for distributed data processing.

### Power BI DAX

1. **Write a DAX to showcase the percentage value trend with uparrow and downarrow characters**

``` sql
sales_mom%_trend = 
var a = switch(
    true(),
    sales_mom% > 0, unichar(129149) & " " & sales_mom%,
    sales_mom% < 0, unichar(129150) & " " & sales_mom%,
    " - "
)
return a
``` 

## Soft Skills and Problem-Solving

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