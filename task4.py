import datetime
from alchemy.class_work.data.jobs import Jobs
from alchemy.class_work.data import db_session


def main():
    db_session.global_init('alchemy/class_work/db/blogs.db')
    db_sess = db_session.create_session()
    
    job = Jobs(team_leader=1, job='deployment of residential modules 1 and 2', work_size=15,
               collaborators='2, 3', start_date=datetime.datetime.now(),
               is_finished=False)
    db_sess.add(job)
    db_sess.commit()

if __name__ == '__main__':
    main()