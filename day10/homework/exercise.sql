-- 删除表
drop table if exists score;
drop table if exists course;
drop table if exists student;
drop table if exists teacher;
drop table if exists class;


-- 建立班级表
create table class(cid int primary key auto_increment,caption char(6) not null);
-- 建立老师表
create table teacher(tid int primary key auto_increment,tname char(6) not null);
-- 建立学生表
create table student(sid int primary key auto_increment,sname char(6) not null,gender enum('男','女') not null default '男',class_id int,foreign key(class_id) references class(cid) on delete cascade on update cascade);
-- 建立课程表
create table course(cid int primary key auto_increment,cname char(6) not null,teacher_id int,foreign key(teacher_id) references teacher(tid) on delete cascade on update cascade);
-- 建立成绩表
create table score(sid int primary key auto_increment,student_id int,course_id int,number int,foreign key(student_id) references student(sid) on delete cascade on update cascade,foreign key(course_id) references course(cid) on delete cascade on update cascade);

INSERT INTO class VALUES(1, '三年二班'), (2, '三年三班'), (3, '一年二班'), (4, '二年九班');
INSERT INTO teacher VALUES(1, '张磊老师'), (2, '李平老师'), (3, '刘海燕老师'), (4, '朱云海老师'), (5, '李杰老师');
INSERT INTO student(sid,gender,class_id,sname) VALUES(1, '男', 1, '理解'), (2, '女', 1, '钢蛋'), (3, '男', 1, '张三'), (4, '男', 1, '张一'), (5, '女', 1, '张二'), (6, '男', 1, '张四'), (7, '女', 2, '铁锤'), (8, '男', 2, '李三'), (9, '男', 2, '李一'), (10, '女', 2, '李二'), (11, '男', 2, '李四'), (12, '女', 3, '如花'), (13, '男', 3, '刘三'), (14, '男', 3, '刘一'),(15, '女', 3, '刘二'), (16, '男', 3, '刘四');
INSERT INTO course VALUES(1, '生物', 1), (2, '物理', 2), (3, '体育', 3), (4, '美术', 2);
INSERT INTO score VALUES(1, 1, 1, 10),(2, 1, 2, 9),(5, 1, 4, 66),(6, 2, 1, 8),(8, 2, 3, 68),(9, 2, 4, 99),(10, 3, 1, 77),(11, 3, 2, 66),(12, 3, 3, 87),(13, 3, 4, 99),(14, 4, 1, 79),(15, 4, 2, 11),(16, 4, 3, 67),(17, 4, 4, 100),(18, 5, 1, 79),(19, 5, 2, 11),(20, 5, 3, 67),(21, 5, 4, 100),(22, 6, 1, 9),(23, 6, 2, 100),(24, 6, 3, 67),(25, 6, 4, 100),(26, 7, 1, 9),(27, 7, 2, 100),(28, 7, 3, 67),(29, 7, 4, 88),(30, 8, 1, 9),(31, 8, 2, 100),(32, 8, 3, 67),(33, 8, 4, 88),(34, 9, 1, 91),(35, 9, 2, 88),(36, 9, 3, 67),(37, 9, 4, 22),(38, 10, 1, 90),(39, 10, 2, 77),(40, 10, 3, 43),(41, 10, 4, 87),(42, 11, 1, 90),(43, 11, 2, 77),(44, 11, 3, 43),(45, 11, 4, 87),(46, 12, 1, 90),(47, 12, 2, 77),(48, 12, 3, 43),(49, 12, 4, 87),(52, 13, 3, 87);

-- 吴超老师网页中的练习题
-- 1、查询所有的课程的名称以及对应的任课老师姓名
select course.cname as '课程名称',teacher.tname as '老师姓名' from course left join teacher on course.teacher_id=teacher.tid;
-- 2、查询学生表中男女生各有多少人
select  student.gender as '性别',count(student.gender) as '计数' from student group by student.gender;
-- 3、查询物理成绩等于100的学生的姓名
select student.sname as '姓名',score.number as '成绩' from student,course,score where score.number=100 and course.cname='物理' and score.student_id=student.sid and score.course_id=course.cid;
-- 4、查询平均成绩大于八十分的同学的姓名和平均成绩
select student.sname as '姓名',avg(score.number) as '平均值' from student inner join score on student.sid=score.student_id group by student.sname having avg(score.number)>80;
-- 5、查询所有学生的学号，姓名，选课数，总成绩
select student.sid as '学号',student.sname as '姓名',count(score.course_id) as '选课数',sum(score.number) as '总成绩' from student inner join score on student.sid=score.student_id group by student.sname order by student.sid asc;
-- 6、 查询姓李老师的个数
select count(teacher.tid)as '姓李老师个数' from teacher where teacher.tname like '李%';
-- 7、 查询没有报李平老师课的学生姓名
select sname as '姓名' from student where sname not in (select distinct student.sname from student,teacher,score,course where student.sid=score.student_id and teacher.tid=course.teacher_id and score.course_id=course.cid and teacher.tname='李平老师');
-- 8、 查询物理课程比生物课程高的学生的学号
select student_id from student, score where (select number from score where student.sid=student_id and  course_id=(select course.cid from course where course.cname='物理'))>(select number from score where student.sid=student_id and  course_id=(select course.cid from course where course.cname='生物')) and student.sid=student_id group by student_id;
-- 9、 查询没有同时选修物理课程和体育课程的学生姓名
select sname from student where sname not in (select wuli.sname from (select student.sname from student, score where student.sid=score.student_id and score.course_id=(select course.cid from course where course.cname='物理')) as wuli,(select student.sname from student, score where student.sid=score.student_id and score.course_id=(select course.cid from course where course.cname='体育')) as tiyu where wuli.sname=tiyu.sname);
-- 10、查询挂科超过两门(包括两门)的学生姓名和班级
select student_id,student.sname,class.caption from score,student,class where score.student_id=student.sid and student.class_id=class.cid and number <60 group by student_id having count(student_id)>=2;
-- 11 、查询选修了所有课程的学生姓名
select * from student,course,score where student.sid=score.student_id and course.cid=score.course_id group by student.sname having count(score.course_id)=(select count(*) from course);
-- 12、查询李平老师教的课程的所有成绩记录
select course.cname,score.number from teacher ,course ,score  where teacher.tid=course.teacher_id and course.cid=score.course_id and  teacher.tname='李平老师'; 
-- 13、查询全部学生都选修了的课程号和课程名
select score.course_id,course.cname from score inner join course on score.course_id=course.cid group by score.course_id having count(score.course_id)=(select count(student.sid) from student);
-- 14、查询每门课程被选修的次数
select count(score.course_id) from score group by score.course_id;
-- 15、查询之选修了一门课程的学生姓名和学号
select student.sname,score.student_id from student inner join score on student.sid=score.student_id group by score.student_id having count(score.course_id)=1;
-- 16、查询所有学生考出的成绩并按从高到低排序（成绩去重）
select distinct score.number from score order by score.number desc;
-- 17、查询平均成绩大于85的学生姓名和平均成绩
select student.sname,avg(score.number) from student inner join score on student.sid=score.student_id group by score.student_id having avg(score.number)>85;
-- 18、查询生物成绩不及格的学生姓名和对应生物分数
select student.sname,number from student inner join score on student.sid=score.student_id where score.course_id=(select course.cid from course where course.cname='生物') and score.number<60;
-- 19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名
select student.sname,avg(score.number) as num from student inner join score on student.sid=score.student_id where score.course_id in (select course.cid from course where course.teacher_id in (select teacher.tid from teacher where teacher.tname='李平老师')) group by score.student_id order by num desc limit 1;
-- 20、查询每门课程成绩最好的前两名学生姓名
select sname,chengji.course_id,chengji.number from student inner join (select student_id,course_id,number from score s1 where (select count(1) from score s2 where s1.course_id=s2.course_id and s1.number<s2.number)<2 order by s1.course_id,s1.number desc) as chengji on student.sid=chengji.student_id;
-- 21、查询不同课程但成绩相同的学号，课程号，成绩
select * from score as s1 where (select count(1) from score s2 where s1.number=s2.number and s1.course_id!=s2.course_id) order by number;
-- 22、查询没学过“李平”老师课程的学生姓名以及选修的课程名称；
select student.sname,course.cname from score,student,course where student.sid=score.student_id and course.cid=score.course_id and   student_id in (select sid from student where student.sid not in (select student_id from score where score.course_id  in (select cid from course where course.teacher_id  in  (select teacher.tid from teacher where teacher.tname='李平老师')) group by student_id));
-- 23、查询所有选修了学号为1的同学选修过的一门或者多门课程的同学学号和姓名；

-- 24、任课最多的老师中学生单科成绩最高的学生姓名
