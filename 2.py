import streamlit as st
import pymysql


# Connect to the MySQL database
conn = pymysql.connect(host="localhost", user="root", password="Mysql_password4", database="crud_new1")

# Create a cursor object

mycursor=conn.cursor()
print("connection established")
def main():
    st.title("mysql")
    #display options for crud operations
    option=st.sidebar.selectbox("select an operation",("create", "read", "update", "delete"))
    #perform selected crud operations
    if option=="create":
        st.subheader("create a record")
        name=st.text_input("enter name")
        email=st.text_input("enter mail")
        if st.button("Create"):
            sql = "insert into users(name,email) values(%s,%s)"
            val = (name, email)
            mycursor.execute(sql, val)
            conn.commit()
            st.success("Record Created Successfully!!!")

    elif option =="read":
        st.subheader("read a record")
        mycursor.execute("select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)
    elif option =="update":
        st.subheader("update a record")
        id = st.number_input("Enter ID", min_value=1)
        name = st.text_input("Enter New Name")
        email = st.text_input("Enter New Email")
        if st.button("Update"):
            sql = "update users set name=%s, email=%s where id =%s"
            val = (name, email, id)
            mycursor.execute(sql, val)
            conn.commit()
            st.success("Record Updated Successfully!!!")
    elif option =="delete":
        st.subheader("delete the record")
        id = st.number_input("Enter ID", min_value=1)
        if st.button("Delete"):
            sql = "delete from users where id =%s"
            val = (id)
            mycursor.execute(sql, val)
            conn.commit()
            st.success("Record Deleted Successfully!!!")


if __name__=="__main__":
    main()