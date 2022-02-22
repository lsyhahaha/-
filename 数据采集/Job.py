class Job:
    def __init__(self):
        # 职位名称
        self.job_name = None
        # 薪资水平
        self.salaryLevel = None
        # 所在城市
        self.city = None
        # 详情页链接
        self.link = None
        # 学历
        self.education = None
        # 工作经验
        self.work_experience = None
        # 公司规模
        self.companySize = None
        # 融资阶段
        self.financing_stage = None
        # 职位描述
        descriptionOfjob = None

    def set(self, job_name, salaryLevel, city, link, education, work_experience, companySize, financing_stage):
        self.job_name = job_name
        self.salaryLevel = salaryLevel
        self.city = city
        self.link = link
        self.education = education
        self.work_experience = work_experience
        self.companySize = companySize
        self.financing_stage = financing_stage

    def toSql(self):
        sql = """INSERT INTO EMPLOYEE
                (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
         VALUES 
                ('Mac', 'Mohan', 20, 'M', 2000)"""

        return sql
