# My-Python-Learning-Journey

## 一、项目简介

本仓库用于记录本学期 Python 课程的课堂练习与课后练习代码，通过 Git 进行版本管理并托管在 GitHub 上。项目中的程序围绕 Python 基础语法展开，包括条件判断与逻辑运算符（and / or / not）的使用练习，用于巩固课堂所学的编程基础。

## 二、文件说明

| 文件名 | 用途 |
| --- | --- |
| `sale.py` | 手机店打折活动资格判断：根据输入的星期和时间段，判断是否满足活动参与条件 |
| `Logical_operator.py` | 逻辑运算符练习：演示 and、or、not 三种逻辑运算符在条件判断中的用法 |
| `README.md` | 项目说明文档 |

## 三、代码说明

### sale.py

- 使用 `input()` 接收用户输入的星期和小时数；
- `input()` 返回的是字符串，小时数通过 `int()` 转换为整数；
- 使用 `if` 条件语句，配合 `and`、`or` 组合判断活动条件；
- 活动规则：星期二 10:00–11:00，或星期五 14:00–15:00 可参与；
- 满足条件输出获奖资格提示，否则输出未参与提示。

核心判断代码：

```python
if (strWeek == "星期二" and (intTime >= 10 and intTime <= 11)) \
or (strWeek == "星期五" and (intTime >= 14 and intTime <= 15)):
    print("恭喜您，获得了折扣活动参与资格，快快选购吧！")
else:
    print("对不起，您来晚一步，期待下次活动……")

### Logical_operator.py

- 分别演示 `and`、`or`、`not` 三种逻辑运算符：
  - `and`：两个条件同时成立时，整体条件才成立；
  - `or`：两个条件至少一个成立，整体条件即成立；
  - `not`：对条件结果取反；
- 通过 `if` 语句判断并打印对应结果；`not` 分支条件不成立，对应语句不会执行。

核心代码：

```python
# and
if x > 0 and y > 0:
    print("Both conditions are true.")

# or
if x > 0 or y > 0:
    print("At least one condition is true.")

# not
if not x == 5:
    print("This statement will not be executed.")
```


## 四、学习心得与规划

通过本次搭建 GitHub 仓库、完成代码上传与提交记录管理的过程，我初步理解了版本控制在个人项目管理中的作用。浏览 GitHub 上其他 Python 项目后我发现，规范的目录结构、清晰的 README 和明确的提交记录，是展示个人技能的重要窗口：它既方便他人快速了解项目，也能体现自己的代码规范与学习轨迹。

这次任务也让我意识到，项目展示不只是把代码存上去，还要通过文档说明每个文件的用途和核心逻辑。未来我计划继续用这个仓库记录后续课程练习和课后小项目：每完成一个练习就及时提交并写清提交说明，定期补充 README 中的文件说明，逐步积累一个能体现自己 Python 学习进度的个人代码作品集。
