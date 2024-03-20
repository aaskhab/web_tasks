from alchemy.class_work.data.users import User
from alchemy.class_work.data import db_session


def main():
    db_session.global_init('alchemy/class_work/db/blogs.db')
    db_sess = db_session.create_session()
    
    user = User(surname='Scott', name='Ridley',
                age=21, position='captain',
                speciality='research engineer',
                address='module 1', email='scott_chief@mars.org')
    db_sess.add(user)
    user = User(surname='Durov', name='Pavel', age=36,
                position='entrepreneur', speciality='telegram founder',
                address='Dubai', email='durov@gmail.com')
    db_sess.add(user)
    
    user = User(surname='Cuckerberg', name='Mark', age=40,
                position='entrepreneur', speciality='Meta founder',
                address='USA', email='mark@gmail.com')
    db_sess.add(user)
    
    user = User(surname='Jobs', name='Steve', age=50,
                position='programmer', speciality='Apple',
                address='USA', email='stevejobs@gmail.com')
    db_sess.add(user)
    db_sess.commit()

if __name__ == '__main__':
    main()