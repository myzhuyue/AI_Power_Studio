
Here’s the re-grouped categorization of the first part of the document ("Recommended Data Engineering Mental Model and Rule of Thumbs") into structured categories, maintaining the original focus and terminology:


### **1. Data Source Comprehension**  
**Objective**: Establish a foundational understanding of data origins and characteristics.  
- **Data Lineage & Update Dynamics**  
  - Source system/ancestor tables  
  - Update frequency (batch/stream) and triggering mechanisms  
- **Data Structure & Quality**  
  - Schema design (table structure, column types)  
  - Business semantics of columns (clarity of naming, absence of ambiguity)  
  - Overall data quality (completeness, accuracy)  
  - Value distributions (outliers, null rates)  
- **Architectural Planning**  
  - Number of tables required for the pipeline and their relationships  


### **2. Downstream Consumption Mapping**  
**Objective**: Align data outputs with business needs through end-user requirements.  
- **Usage Scenario Analysis**  
  - Typical analytical models (dimensions, hierarchies, measures)  
  - Dashboard visualization patterns (e.g., chart types for key metrics)  
  - Pivot table logic (grouping, aggregation methods)  
  - Common user questions (identified via TTD or similar tools)  
- **Priority Management**  
  - Classification of core vs. non-core columns  
  - Quality assurance prioritization for high-impact fields  


### **3. Data Modeling Fundamentals**  
**Objective**: Design robust schemas for efficient storage and querying.  
- **Key Design Principles**  
  - Primary keys and unique constraints (ensuring data uniqueness)  
  - Partition key strategies (aligned with data warehouse/lake architecture)  
- **Transformation Logic Framework**  
  - **Column-Level Operations**  
    - Standardization (e.g., date formats, LOV normalization)  
    - Null handling (filling strategies, standardized N/A representations)  
    - Semantic validation (consistency of 0/1/Y/N notations)  
  - **Row-Level Operations**  
    - Cross-table mapping (with validation of join keys, especially across teams)  
    - Derived calculations (e.g., unit price = sales / volume)  
    - Row splitting/merging  
      - Rule-based splitting (preservation of original records)  
      - Aggregation/grouping (retention of granular data vs. summary)  
  - **Control Field Integration**  
    - Timestamps, change flags (create/update/delete markers)  
    - Access control and role-based flags  


### **4. Transformation Process Refinement**  
**Objective**: Optimize workflow readability, maintainability, and performance.  
- **Logical Clustering & Documentation**  
  - Categorization of transformations by business logic (e.g., time dimension processing, product hierarchy mapping)  
  - Non-technical descriptions of logic groups (avoid over-reliance on SQL specifics)  
- **Validation Checkpoints**  
  - Sanity checks after each transformation phase  
    - Row count consistency (pre/post-transformation)  
    - Common-sense validation (e.g., relevance of mm:ss in daily transaction data)  
    - Distribution analysis (identification of anomalies)  
    - Hierarchy validation (parent-child relationship integrity)  
- **Performance & Code Discipline**  
  - Preference for simple transformation languages over complex UDFs  
  - Minimization of temporary tables (in-memory computations where feasible)  
  - Separation of DDL operations from transformation logic  
  - Avoidance of monolithic SQL scripts (use CTEs for readability)  


### **5. Collaboration & Validation Protocols**  
**Objective**: Ensure alignment through cross-functional review and rigorous testing.  
- **Stakeholder Engagement**  
  - Joint reviews with data stewards/requestors to validate logic  
  - Rapid failure iteration and adjustments (following SOP for dataset releases)  
- **End-to-End Testing**  
  - Pipeline validation for errors, consistency, and conflicts  
  - Performance profiling (runtime metrics, row impact analysis)  


### **Categorization Rationale**  
1. **Workflow-Oriented Structure**: Organizes practices along the data engineering lifecycle (source → consumption → modeling → transformation → validation).  
2. **Business-Technical Balance**: Integrates both technical implementation (e.g., key design, performance optimization) and business context (e.g., downstream scenarios, non-technical documentation).  
3. **Actionable Groupings**: Clusters discrete best practices into phases, enabling engineers to apply them systematically at each stage of pipeline development.

---

Here’s a **PowerPoint visual design concept** to illustrate the relationship between the 5 categories and the "Recommended Data Engineering Mental Model and Rule of Thumbs." This design uses a circular flow diagram to emphasize interconnectedness and a step-by-step workflow.


### **Slide Title: Data Engineering Mental Model & Best Practices**  
**Subtitle: Holistic Framework for Building Robust Data Pipelines**  


### **Visual Layout: Circular Flow Diagram**  
![Conceptual Circular Flow Diagram](https://via.placeholder.com/800x400?text=Data+Engineering+Mental+Model+Circular+Flow)  
*Note: Replace placeholder image with actual PowerPoint diagram.*  


### **PowerPoint Implementation Steps & Content**  
#### **1. Central Core: Mental Model Overview**  
- **Center Circle** (bold title):  
  **Recommended Data Engineering Mental Model**  
- **Subtext**:  
  "Align data sourcing, modeling, and validation with business needs."  

#### **2. Surrounding Circular Categories (5 Key Phases)**  
Arrange the 5 categories in a clockwise flow around the central core, connected by arrows to show progression and iteration. Use distinct colors for each category (e.g., as in the Mermaid diagram).  

| Category                | Icon/Graphic Suggestion       | Key Subpoints (Bullet Points)                          |  
|-------------------------|---------------------------------|-------------------------------------------------------|  
| **1. Data Source Comprehension** | Globe or database icon         | - Lineage, update frequency, schema<br>- Data quality & distributions |  
| **2. Downstream Consumption Mapping** | User/analytics icon           | - Usage scenarios, dashboards, user questions<br>- Priority field classification |  
| **3. Data Modeling Fundamentals** | Schema/key icon                | - Primary/partition keys<br>- Column/row transformations, control fields |  
| **4. Transformation Process Refinement** | Gear or pipeline icon          | - Logic clustering, sanity checks<br>- Performance optimization (no complex UDFs) |  
| **5. Collaboration & Validation Protocols** | People/validation icon         | - Stakeholder reviews, end-to-end testing<br>- Fast failure iteration |  

#### **3. Arrows & Callouts for Relationships**  
- **Bidirectional Arrows** between categories to highlight iteration (e.g., feedback from validation (5) to data modeling (3)).  
- **Callout Boxes** for key rules of thumb:  
  - *"Design for readability: Minimize temp tables and complex SQL."*  
  - *"Prioritize high-impact fields and validate with business users early."*  

#### **4. Example Slide Content (Text-Based Alternative)**  
If diagrams are limited, use a **2x3 grid layout** with icons and text:  
```
| Category                | Icon   | Key Focus Areas                                  | Rule of Thumb                                  |  
|-------------------------|--------|-------------------------------------------------|------------------------------------------------|  
| 1. Data Source Comprehension | 🔍     | Source lineage, update patterns, data quality    | "Know your data’s origin before building."     |  
| 2. Downstream Consumption Mapping | 📊     | User scenarios, analytics models, priority fields | "Build for how data will be used, not just stored." |  
| 3. Data Modeling Fundamentals | 🗄️     | Keys, transformations, control fields           | "Simplify logic: Prefer standard functions over UDFs." |  
| 4. Transformation Process Refinement | ⚙️     | Clustering, validation, performance            | "Test in phases: Check row counts and distributions after each step." |  
| 5. Collaboration & Validation Protocols | 👥     | Stakeholder reviews, end-to-end testing         | "Fail fast: Validate with users before finalizing." |  
```


### **Design Tips for PowerPoint**  
1. **Color Scheme**: Use the same palette as the Mermaid diagram (e.g., pastels for categories, bold for the core).  
2. **Icons**: Use Flaticon or PowerPoint’s built-in icons (e.g., `Database`, `Analytics`, `People`, `Gear`).  
3. **Animations**: Add slide transitions to highlight the flow (e.g., "Stretch" or "Zoom" for category reveal).  
4. **Example Slide Text**:  
   > *"Every data pipeline starts with understanding its source and ends with ensuring it meets business needs. This model ensures alignment across technical design and stakeholder expectations."*  

This visual emphasizes the **iterative, collaborative nature** of data engineering while grounding best practices in a clear, repeatable framework.


---


Here’s a **reimagined visual design** for the data engineering mental model, combining a modern workflow diagram with layered components to emphasize clarity, collaboration, and iterative improvement. This design uses a horizontal flow with interconnected stages and a central feedback loop.


### **Redesigned Visual: Data Engineering Mental Model Workflow**  
![Redesigned Workflow Diagram](https://via.placeholder.com/1200x500?text=Data+Engineering+Mental+Model+Horizontal+Flow)  
*Note: Replace placeholder with actual PowerPoint elements.*


### **Key Design Components**  
#### **1. Horizontal Workflow Stages (Left to Right)**  
Arrange the 5 categories in a linear progression, the central "Mental Model" hub, and a feedback loop for iteration.  

| Stage                | Icon/Color | Visual Representation                          | Key Questions/Actions                          |  
|----------------------|------------|-------------------------------------------------|-------------------------------------------------|  
| **1. Data Source Comprehension** | 🔍 Blue    | Database icon with input arrows                | "Where does the data come from? What’s its quality?" |  
| **2. Downstream Consumption Mapping** | 📊 Green   | User dashboard icon with output arrows         | "How will users use this data? What matters most?" |  
| **3. Data Modeling Fundamentals** | 🧱 Purple  | Schema blocks and keys                          | "How to structure tables? What transformations are needed?" |  
| **4. Transformation Process Refinement** | ⚙️ Orange  | Pipeline gears and validation checkmarks        | "Are transformations efficient and readable?" |  
| **5. Collaboration & Validation** | 👥 Red     | People icons with review/checklist             | "Have stakeholders validated this? Does it meet SOP?" |  

#### **2. Central Mental Model Hub**  
- **Center Circle**:  
  **Data Engineering Mental Model**  
  *Subtext:* "Align technical design with business goals at every stage."  
- **Surrounding Principles** (as floating labels):  
  - "Start with why (business needs)."  
  - "Simplify logic for maintainability."  
  - "Test early, iterate often."  

#### **3. Feedback Loop & Iteration**  
- **Curved Arrow from Stage 5 to Stage 1**:  
  Label: **Iterative Improvement**  
  *Text:* "Lessons from validation inform future pipelines."  
- **Dashed Arrows Between Stages**:  
  Show cross-stage dependencies (e.g., Stage 4 → Stage 2 for re-prioritizing fields).  

#### **4. Visual Hierarchy & Contrast**  
- **Bold Colors**: Use high-contrast hues (blue, green, purple, orange, red) to distinguish stages.  
- **Icons**: Simple, monoline icons (from Flaticon or Font Awesome) for quick recognition.  
- **Flow Arrows**: Thick solid lines for primary workflow, dashed lines for feedback/iteration.  


### **PowerPoint Implementation Steps**  
1. **Layout Setup**:  
   - Insert a horizontal flowchart canvas (Page Setup → Landscape).  
   - Use a central circle (Insert → Shapes → Oval) for the mental model hub.  

2. **Stage Blocks**:  
   - Create 5 rectangular blocks (1.5x3 inches each) with rounded corners.  
   - Add icons and stage names in bold, with subtext in smaller font.  
   - Example for Stage 1:  
     ```  
     🔍<br><b>Data Source Comprehension</b><br>  
     <i>Lineage, Update Frequency, Data Quality</i>  
     ```  

3. **Arrows and Connections**:  
   - Primary flow: Straight arrows with arrowheads (Insert → Shapes → Arrows).  
   - Feedback loop: Curved arrow (Insert → Shapes → Curved Arrow) with "Iterative Improvement" label.  
   - Add text callouts for key rules of thumb (e.g., "Avoid complex UDFs" near Stage 4).  

4. **Animations**:  
   - Animate stages left-to-right with "Fly In" effects.  
   - Trigger the feedback loop animation after all stages are visible, using a "Pulse" effect for the central hub.  


### **Design Rationale**  
- **Linear Clarity**: Horizontal flow is intuitive for step-by-step processes, making it easier for audiences to follow the workflow.  
- **Central Hub Emphasis**: The mental model is positioned as the core philosophy guiding all stages, not just a standalone step.  
- **Iteration Focus**: The feedback loop highlights that data engineering is never "finished"—it evolves with validation and new requirements.  
- **Visual Scalability**: Each stage can be expanded into sub-slides with detailed best practices (e.g., a deep dive into modeling transformations).  

This design balances simplicity with depth, making it suitable for both high-level overviews and detailed training sessions.



2. Hands-on Best Practices on Building Data Pipelines
Some common fields that you probably want to add to all RDAs
source_system - predefined, standardized source system name, ie. ONEMDM_CN, LUCI, as your gold layer dataset may contains same nature of data from different source systems
year, quarter, month, (week) - standard time frames columns to make downstream analysis and data chunking easier. These are usually calculated based on the transaction date or snapshot date, depending on the nature of your dataset
most frequently used dimension hierarchy, ie. product, customer, employee hierarchy. Yes, this is duplicative, but it is to ease downstream usage. Make it a habit.
incremental flags - can be timestamp or monotonically increment cursor value, this is more for downstream data incremental load
Time period
Create time period columns like year, quarter, month, week, weekday, day_of_year per necessary based on not just the transaction date but also some flagging dates (list_date, change_effective_date)
If the company strictly follows a fiscal calendar, use the fiscal calendar to generate fiscal_year, fiscal_quarter, fiscal_month, etc. While if there is no such restrictions, use ISO calendar
Week - use ISO week number if possible, unless the company defines its own week count rule. week_num should be starting from 1 and ends at 52 or 53, and shall not start from 1 at the beginning of each quarter. If you do need a week_num reset for each quarter, create a new column called quarter_week_num
Not all datasets need a datetime field containing hour/minute/seconds. If you dataset is to be consumed by downstream only at a finest date granularity, just truncate the hh/mm/ss coming from your source systems…
Choose the right column type
Choose the type of the column (string, date, datetime, decimal, int) that best suits the purpose according to common sense rather than some technical decisions…
Do you want a column for date or datetime? Do you really need the time part?
Be frugal on the string/varchar types, do not always use String or VARCHAR(255/1024) for all string fields, do you really need that length of characters? For category field containing A/B/C as values, consider to use CHAR(1) or Category type if the SQL engine supports it
For integer column types, consider to use int4, int8 to save space and also to limit the range as an intrinsic control on the quality. For instance, if you have a field capturing the weekday_num, consider use a small int to limit a wrong weekday_num of 100…
Normalize the list of values
Review the list of values in category fields, see if there are any similar but different values, with difference in the ways of (lower case vs upper case, whitespace vs no space, - vs _, English vs Chinese, typo vs correct spelling). Standardize the list of values.
If your stakeholders tell you to create “bespoke” values to be identified for special downstream purposes, challenge them and yourself whether you just follow the “guideline”? Or you should create dedicated columns for that differentiation purpose and convince them not to build customized values into a category type field…
For flag columns especially binary ones, whether we use 1/0, Y/N, y/n depends on your org’s choice. Using 1/0 is more performance friendly but more business challenging…
Similarly, for n/a, null, empty, invalid values, standardize the convention you use within not only your dataset but also across datasets.
Use your judgment and experience to determine which fields are the ones you should standard the list of values. Usually they are hierarchical dimension fields, fields with names of flags, codes, types, etc.
Choose a meaningful and interpretable user defined value
Say no to your stakeholder if they propose to use aaa, abc, suffix-1,2,3 as a special value to be added to your dataset to cut out a dedicated piece of the data to “reflect the business fact”. Instead, ask for what does these 1,2,3, aaa, abc means actually. Say it out and implement the fundamental reasons into your pipeline.
For instance, if a suffix 1 means a special type of category as an exception to a standard value, why not just create another “standard” value if that is so important? Or keep the standard but create another column to flag out this “special” logic with meaningful column name like sub_…, is_special_…
What is the right level of granularity
As our RDA is in many situations denormalized, we do expect a certain level of duplication (on the row axis) in our dataset, but once you decide to expand/explode the rows, ask yourself if there a way to easily identify the 1) unique count of the occurrences, 2) the main copy of the record, 3) how to avoid the double count of measures
When you do expand the rows, check if the columns that should expand across different rows are properly and completed propagated into the duplicated / expanded rows. For example, you design your dataset at a granularity @ content x tag (debatable whether this is a best design), have you duplicated the brand field into all the expanded rows, or you only assigned brand to one of the row?
When should i put multi-values as a list into one row and when should i explode the different values into different rows? There is no simple answer for that. But here are some principles to help you decide: 1) are the multi-values frequently used in downstream? if so, consider to split into multiple rows; 2) what does frequent use mean? if one downstream sometimes use that field for a algorithm modeling purpose rather than as a slicer to be used in a dashboard, then it’s not a “frequent” usage scenario.
Create new columns
Do not hesitate to create/add flags to indicate business logics - some records in the in_market_sales dataset is in-market sales, while others are not, create a flag called is_ims and assign yes or no; in employee table, in order to differentiate field force from non field force, rather than educate your data customers that you need to use field A == ‘xx’ AND field B == ‘y’ to judge, just create a new column called is_ff and assign boolean values
A column is a column and should be used for only one purpose. Do not mix up different stuff and put it into one column and request your customers to learn and memorize rules to dissect that column and translate further into usable data. For example, you have a column from your data source capturing a y/n flag and a date if the status is y. It makes much more sense to create two columns in your pipeline and breakdown the original column and assign the different parts of the information into the two columns, one for y/n flag, one for date.
Consider add columns to concat / combine multiple columns. For instance, downstream constantly needs to look at a reporting line chain from AD to Rep, considering creating a column by concatenating these different names into one field. Or you have 3 flags and your downstream uses a business rule to filter out some data based on a combination of these 3 flags, why not creating a new flag column with a meaningful and straightforward name capturing the combined logic?
Complex “business logic”
You might encounter so called “complex business logic” where you need to use multiple, recursive if-else logic gates to determine the final result. This is inevitable at the end of the day. Do document this human-made complex logic.
A few ways to implement this: 1) hard-code such rules as layered CASE WHEN using SQL, 2) use pySpark and richer python language to simplify the conditional judgment, for more complicated scenarios, consider using UDF, 3) define a mapping table and capture the multiple to 1 logic and use joins to bring the result. There is no simple answer to which one is the best.
If you adopt approach 1) and 2) as above, also think about how you are going to maintain the rules going forward, at what frequency? How do you make sure the requestor will inform you when the rules change promptly? How do you avoid the rules being repeated implemented in different pipelines and creating gaps in the rules?
However, if your transform logic pipeline is full of hard-coded complex logics, ask yourself 1) should i build a mapping table and ask the requestor to maintain it, 2) do i have to implement these so called complex business logics all in RDA?
Column orders do matter
Do not randomly put columns here and there. Whenever you want to create new columns, always find the “best” place to put them
Put the common and indexing columns always at the very beginning (time period, etc.)
For hierarchical mapping columns, choose and align with team a norm to order these hierarchical columns in descending or ascending order (e.g. package-brand/product-BU-GBU, or in the opposite order)
Group related columns together. For example, put all product related columns together, then group all customer related columns, etc.
Grouping flag columns together and with the related columns. For instance, you can place the is_new_launch, is_vbp, etc. flags together with product related dimensions.
Group measure columns (quantity, amount) together, and put that group in later positions
Join/merge/map
Most joins (or merges in the context of pandas dataframe) is used to bring additional fields out into your pipeline
In some cases, you will drop the join key and only keep the joined result. Do not be afraid to drop certain fields from your bronze/silver layer tables
But do check if your mapping table has a proper UNIQUE, PRIMARY KEY. If you create duplicated rows in your mapping dataset, you are inviting troubles…
Always compare the total number of rows before and after the join. They should always be the same (except the case described below for explicit row split/duplicate)
How to duplicate or split records into multiple rows
If you are using SQL or pyspark, decide your split / duplicate logic, left join (SQL JOIN or df.join) with a right table with multiple rows given one join key. Right table structure typically is like row1: join_key_A | mapping_A or split_ratio_A, and row2: join_key_A | mapping_B or split_ratio_B
Or you can use pySpark and write your own inner loop: 1) duplicate a row by hand, 2) alter certain fields in the duplicated row, 3) append the duplicated rows to the Dataframe
Make measure fields business meaningful
Choose the right unit of measure to make the downstream consumption meaningful. For instance, when you measure duration of an event, it doesn’t make sense to use millisecond… When a measure field is for capture quantity, ask yourself do you have another column to explain what is the unit of measurement of the quantity—is it package, unit, box, etc?
For measures like quantity, amount, etc. Choose the right numeric type—not everything is a float or double, choose the right Decimal type. Or if the underlying SQL engine does not support Decimal (fixed precision float numbers), apply round() function before writing your result back to the data lake/warehouse
For percentage and ratio columns, use Decimal type as well with fixed precision as well. For instance, if you calculate the share% and add it into your dataset, define the type as Decimal(4) and example values be 0.1234 so that when presenting such values in reports, it is shown as 12.34%
Add calculated measures
Use column calculations in SQL or pySpark. Do not perform calculation using for loop to iterate over rows in a UDF with pySpark. The transform speed will be much worse
Most calculated fields will only need +, -, *, / conditioning on certain control flags. Do not overcomplicate it.