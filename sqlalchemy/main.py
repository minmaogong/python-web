import datetime

from base import Base
from database import engine, SessionLocal
from models import Employee, Department



# 创建表
def create_table():
    print("注册的表名:", Base.metadata.tables.keys())
    # 创建所有模型对应的表
    Base.metadata.create_all(bind=engine)
    print("表创建成功")

def insert_data():
    # 获取数据库会话
    db = SessionLocal()

    try:
        # 第一步：新增部门
        new_dept = Department(
            name="研发部", # 部门名称（唯一）
            location="北京总部" # 部门位置
        )
        db.add(new_dept) # 将部门对象加入会话
        db.commit() # 提交到数据库（执行 INSERT 语句）
        db.refresh(new_dept) # 刷新对象，获取自增的id等字段

        # 第二部：新增关联的员工
        emp1 = Employee(
            name="张三",
            age=30,
            hire_date=datetime.date(2023, 1, 1), # 入职日期
            department_id=new_dept.id, # 关联部门ID（外键）
        )
        emp2 = Employee(
            name="李四",
            age=28,
            hire_date=datetime.date(2023, 3, 15),  # 入职日期
            department_id=new_dept.id,  # 关联部门ID（外键）
        )

        # 批量添加员工（也可逐个add）
        db.add_all([emp1, emp2])
        db.commit() # 提交员工数据
        # 刷新员工对象，获取自增ID
        db.refresh(emp1)
        db.refresh(emp2)

        print(f"新增部门： ID={new_dept.id}, Name={new_dept.name}, 位置={new_dept.location}")
        print(f"新增员工1： ID={emp1.id}, Name={emp1.name}, Age={emp1.age}, Hire Date={emp1.hire_date}, Department ID={emp1.department_id}")
        print(f"新增员工2： ID={emp2.id}, Name={emp2.name}, Age={emp2.age}, Hire Date={emp2.hire_date}, Department ID={emp2.department_id}")

        # 验证关联关系（通过ORM关联查询）
        print("\n【验证关联关系】")
        # 从员工查部门
        print(f"员工{emp1.name}的部门名称：{emp1.department.name}")
        # 从部门查员工
        dept_employees = new_dept.employees
        print(f"部门{new_dept.name}的员工列表：{[emp.name for emp in dept_employees]}")

    except Exception as e:
        db.rollback() # 出错就回滚
        print(f"新增失败：{e}")
    finally:
        db.close() # 关闭会话


def delete_data():
    session = SessionLocal()
    try:
        # 删除单个员工
        emp = session.query(Employee).filter(Employee.name == "李四").first()
        if emp:
            session.delete(emp)
            session.commit()
            print(f"已删除员工：{emp.name}")
    except Exception as e:
        session.rollback()
        print(f"删除失败：{e}")
    finally:
        session.close()

def update_data():
    session = SessionLocal()
    try:
        # 更新员工年龄
        emp = session.query(Employee).filter(Employee.name == "张三").first()
        if emp:
            emp.age = 31 # 修改年龄
            session.commit() # 提交修改
            print(f"已更新员工：{emp.name} 的年龄为 {emp.age}")
    except Exception as e:
        session.rollback()
        print(f"更新失败：{e}")
    finally:
        session.close()

def read_data():
    session = SessionLocal()
    try:
       dept = session.get(Department, 1)
       print(f"部门ID={dept.id}, Name={dept.name}, Location={dept.location}")

       rd_employees = session.query(Employee).filter(Employee.department_id == 1).all()
       print(f"研发部门员工:{[emp.name for emp in rd_employees]}")


    except Exception as e:
        print(f"查询失败：{e}")
    finally:
        session.close()


if __name__ == '__main__':
    # create_table()
    # insert_data()
    # delete_data()
    update_data()