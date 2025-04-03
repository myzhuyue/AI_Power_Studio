
5. **From the Power Query editor, what data profiling tool (Data Preview) allows you to only see the percentage of
empty values in each column?**

&emsp;&emsp;&emsp; A. Monospaced

&emsp;&emsp;&emsp; B. Column quality

&emsp;&emsp;&emsp; C. Column distribution

&emsp;&emsp;&emsp; D. Column profile

> B, Column quality

2. **How would you complete the following DAX calculated table expression, so it returns a table of the top 25 customers based on Total Revenue?**

![Calculate Function](./images/pbi_calculate_top25.jpeg)

``` sql
[Top 25 Customers] = 
  CALCULATETABLE(
    TOPN(
      25, 'CYCLE SALES',
      [Total Revenue], DESC
  )
)
``` 

3. **Write a DAX to showcase the percentage value trend with uparrow and downarrow characters**

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
4. **You are creating a Power BI report to analyze consumer purchasing patterns from a tablenamed Transactions. The Transactions table contains a numeric field named Spend. Youneed to include a visual that identifies which fields have the greatest impact on Spend.Which type of visual should you use?**

&emsp;&emsp;&emsp; A. decomposition tree

&emsp;&emsp;&emsp; B. Q&A

&emsp;&emsp;&emsp; C. smart narrative

&emsp;&emsp;&emsp; D. key influences

> D, key influences

