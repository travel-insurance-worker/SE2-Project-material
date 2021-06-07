use Futuristic_Travel
Go


ALTER TABLE Customer ADD Username VARCHAR(50) NULL;

insert into Customer(ID,FirstName,LastName ,NationalCode ,BirthDate,EmailAddress,MembershipDate,[status] ,[Password],Username)
values('2021222222','Arman','Riasi','3678229065','1998-01-23','ArmanRiasi@yahoo.com','2020-10-17','Active','1111','AR123');
insert into Customer(ID,FirstName,LastName ,NationalCode ,BirthDate,EmailAddress,MembershipDate,[status] ,[Password],Username)
values('2021333333','Bahar','Broomand','1279774999','1999-01-03','baharbroomand@yahoo.com','2021-01-17','Active','1111','BB123');
insert into Customer(ID,FirstName,LastName ,NationalCode ,BirthDate,EmailAddress,MembershipDate,[status] ,[Password],Username)
values('2021555555','Peyman','Hosseini','7859004386','1995-01-03','Paymanhs@yahoo.com','2020-08-07','Active','1111','PH123');
insert into Customer(ID,FirstName,LastName ,NationalCode ,BirthDate,EmailAddress,MembershipDate,[status] ,[Password],Username)
values('2021444444','Ghazale','Zehtab','7859004386','1994-01-03','Ghazalzehtab@yahoo.com','2020-08-07','Active','1111','GZ123');


insert into Customer(Username)
values('Duki') where ID = '1911332431' ;

update Customer
set username = 'Duki'
where ID = '1911332431'

select * from Customer