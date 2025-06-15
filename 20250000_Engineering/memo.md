
# Meeting Minutes for DQ Service


## Information

DQ Service Tools:

1. 能满足目前大部分RDA数据质量检查点，下面2点待完善：
    - sql中对于日期的偏移计算
    - 稳定性检查方面的枚举值检查）

2. DQ Service tools 目前的运行机制是通过API方法调用的，因此部分SQL函数暂不支持；（目前DQ Rule的运行是通过Spark Engine运行的，考虑增加Trino SQL）

3. DQ Service基于Spark和Trino运行的资源、性能对比，目前已有初步结论，当有复杂的Join的时候Trino优于Spark；

4. OneMesh当前生产环境的DQ Issue暂时无法一次性解决，待DQ Service Tool UAT后考虑迭代替换现有DQ方案；


## Follow Up Action:

1. DQ数据在未来DF的使用过程中，能够通过一个DQ API调用，并区分成功和失败的数据情况，通过配置将数据写入不同的数据表中； - **Owner: Haiyang，通过DF距离说明，如何实现根据DQ配置和数据开发过程将数据情况进行分发（如何一部分数据reject，一部分pass）**

2. 通过Launch to Engage (Interaction)，在UAT环境进行测试，验证OneMesh的各项功能是否能满足用户的Expectation；并在此过程中Evaluate 每个Pods的具体步骤和workload，最终评估完成OneMesh平台所有RDA所需的周期和资源；
- Owner: OneMesh, RDA, DQ, 时间安排：Start from Jun Sprint