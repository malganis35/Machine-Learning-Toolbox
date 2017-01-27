filename = 'data_train_competition.csv';

data = csvimport(filename,'delimiter',',');

%% Split header and data

header = data(1,:);
data(1,:)=[];

%% Split the data into 4 files

nb_data = size(data,1);
data1 = data(1:nb_data/4,:);
data2 = data(nb_data/4+1:nb_data/2,:);
data3 = data(nb_data/2+1:3*nb_data/4,:);
data4 = data(3*nb_data/4+1:end,:);


%% the data

data1 = [header; data1];
filename1 = 'data1.csv';
csvexport(filename1,data1);

data2 = [header; data2];
filename2 = 'data2.csv';
csvexport(filename2,data2);

data3 = [header; data3];
filename3 = 'data2.csv';
csvexport(filename3,data3);

data4 = [header; data4];
filename4 = 'data4.csv';
csvexport(filename4,data4);


%% small data

data_tmp = [header; data1(1:1000,:)];
filename1 = 'dataSmall.csv';
csvexport(filename1,data_tmp);

data_test = [header; data1(1001:2001,:)];
filename1 = 'dataTest.csv';
csvexport(filename1,data_test);