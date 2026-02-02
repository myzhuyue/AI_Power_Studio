

## Power BI Data Modeling Checklist

- Design for the user experience, not for developers  
	Structure the data model to enhance user experience, focusing on usability, performance, and clear business logic.

- Build star schemas  
	Whenever possible, organize data into fact and dimension tables with single-key, one-to-many relationships from dimensions to facts.

- Enforce dimension key uniqueness  
	Do not assume key values are unique—enforce uniqueness at the data source. Use grouping and duplicate removal in source views or Power Query to guarantee uniqueness.  
	Apply duplicate record checks and other integrity audits to source data, but never allow the data model to violate these rules.

- Avoid bi-directional filters and unnecessary bridge tables  
	These modeling patterns can negatively impact performance.

- Prefer DAX measures over complex or inefficient relationships

- Create custom columns in Power Query  
	Use Power Query for row-level calculated columns instead of DAX calculated columns to maintain a consistent and maintainable design pattern.

- Annotate code  
	Add in-line comments and annotations to all code, including SQL, M, and DAX, to explain calculation logic and provide author and revision details.

- Remove all unused fields—when in doubt, leave it out

- Hide all fields not intended for direct user interaction  
	This includes primary and foreign key columns, numeric columns used only in measures, and columns used solely for sorting.

- Use friendly field names  
	Rename all visible columns (preferably in Power Query) to concise, user-friendly names using mixed case and spaces.

- Set “Do Not Summarize” for appropriate columns  
	For any visible numeric columns not meant to be aggregated, set the “Do Not Summarize” property. Columns set to summarize are indicated with a Sigma icon.



## Power BI 数据建模检查清单

- 面向用户体验设计  
  将数据模型设计为易用、性能佳、业务逻辑清晰，服务于终端用户而非开发者偏好。

- 构建星型模式  
  尽可能将数据组织为事实表与维度表，使用单一键，维度到事实的一对多关系。

- 强制维度键唯一性  
  不要假设键值天然唯一——在数据源或 Power Query 中通过分组与去重来保证唯一性。  
  对源数据执行重复记录检查与完整性审计，但不要让数据模型违反唯一性规则。

- 避免双向筛选与不必要的桥接表  
  这些建模模式会增加歧义并降低性能，除非确有必要应避免使用。

- 优先使用 DAX 度量而非复杂或低效的关系

- 在 Power Query 中创建自定义列  
  行级派生列尽量在 Power Query 中实现，以保持一致的设计与更好的可维护性。

- 注释代码  
  在 SQL、M、DAX 代码中添加内联注释，说明计算逻辑并提供作者与修订信息。

- 移除所有未使用的字段——拿不准就删掉

- 隐藏不直接供用户使用的字段  
  包括主外键列、仅用于度量的数值列、以及仅用于排序的列。

- 使用友好的字段名称  
  在 Power Query 中将所有可见列重命名为简短、易懂的名称，采用大小写混排与空格。

- 将不应汇总的列设置为“不要汇总”  
  对不用于聚合的可见数值列设置“不要汇总”。已设置汇总的列在字段列表中会显示 Sigma 图标。

### 规则说明

- 面向用户体验：更易被采纳、减少误用并加快洞察交付。
- 星型模式：与 VertiPaq 引擎契合，筛选上下文更可预测，避免歧义关系与性能问题。
- 维度键唯一性：保障一对多关系与正确查找，避免重复导致的重复计算。
- 避免双向与桥接：双向筛选扩大筛选路径并带来歧义；优先单向关系，必要时用 DAX（如 `TREATAS`）实现定向跨筛选。
- 优先度量：将业务逻辑集中在可复用、上下文感知的度量中，减少脆弱的关系网。
- Power Query 自定义列：可折叠至数据源、在刷新时计算，降低模型体积与运行开销；仅在必须依赖模型关系的场景使用 DAX 列。
- 注释代码：便于评审与交接，防止逻辑丢失。
- 移除未使用字段：更小的模型压缩更好、加载更快，字段列表更干净。
- 隐藏非用户字段：避免用户误将键、排序或辅助列拖入可视化，提升报表质量。
- 友好字段名：提升可发现性与自助分析体验，减少培训负担。
- “不要汇总”：防止对标识、单价、比率等进行错误聚合，避免误导性的总计与平均值。